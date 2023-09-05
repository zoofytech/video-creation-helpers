#!/usr/bin/env python3

import os
import sys
import subprocess
import moviepy.editor as mp
import google.auth
import googleapiclient.discovery
import googleapiclient.errors
import instagram_private_api
import pytiktok
from googleapiclient.http import MediaFileUpload

def main():
    # Get the arguments passed by the shell wrapper script
    video_file_path = sys.argv[1]
    client_secret_file = sys.argv[2]
    scopes = sys.argv[3]
    api_service_name = sys.argv[4]
    api_version = sys.argv[5]
    username_instagram = sys.argv[6]
    password_instagram = sys.argv[7]
    username_tiktok = sys.argv[8]
    password_tiktok = sys.argv[9]
    video_title = sys.argv[10]
    video_description = sys.argv[11]
    
    # Check the video duration
    video_duration = get_video_duration(video_file_path)

    # Split the video into multiple videos if necessary
    max_video_duration = int(sys.argv[12])
    if video_duration > max_video_duration:
        split_video(video_file_path, max_video_duration)

    # Upload the video to YouTube
    youtube_upload(video_file_path, client_secret_file, scopes, api_service_name, api_version, video_title, video_description)

    # Upload the video to Instagram
    instagram_upload(video_file_path, username_instagram, password_instagram)

    # Upload the video to TikTok
    tiktok_upload(video_file_path, username_tiktok, password_tiktok)

def get_video_duration(video_file_path):
    # Use FFmpeg to get the duration of the video in seconds
    command = ['ffmpeg', '-i', video_file_path]
    output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = output.stderr.decode()
    duration = 0
    for line in output.split('\n'):
        if 'Duration' in line:
            duration_str = line.split(',')[0].split('Duration: ')[1]
            duration = sum(float(x) * int(t) for x, t in zip(duration_str.split(':'), [3600, 60, 1]))
            break
    return duration

def split_video(video_file_path, max_duration):
    # Use moviepy to split the video into multiple videos
    video = mp.VideoFileClip(video_file_path)
    num_videos = int(video.duration // max_duration) + 1
    for i in range(num_videos):
        start_time = i * max_duration
        end_time = min((i + 1) * max_duration, video.duration)
        subclip = video.subclip(start_time, end_time)
        subclip.write_videofile(f'{video_file_path}_part_{i}.mp4', codec="libx264", fps=24)

def youtube_upload(video_file_path, client_secret_file, scopes, api_service_name, api_version, video_title, video_description):
    # Load the client secrets file
    creds = google.auth.credentials.Credentials.from_authorized_user_info(info=client_secret_file, scopes=scopes)

    # Create the YouTube API client
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=creds)

    # Get the video file size
    video_size = os.path.getsize(video_file_path)

    # Set the metadata for the video
    body = {
        'snippet': {
            'title': video_title,
            'description': video_description,
            'tags': ['video', 'upload', 'test'],
            'categoryId': 28
        },
        'status': {
            'privacyStatus': 'private'
        }
    }

    # Create the request to upload the video
    request = youtube.videos().insert(part=','.join(body.keys()), body=body, media_body=MediaFileUpload(video_file_path, chunksize=1024*1024, resumable=True))

    # Upload the video in chunks
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f'Uploaded {int(status.progress() * video_size)} bytes')
    print(f'Video uploaded: {response["id"]}')

def instagram_upload(video_file_path, username, password):
    # Create an Instagram API client
    api = instagram_private_api.Client(username, password)

    # Read the video file and upload it to Instagram
    with open(video_file_path, 'rb') as file:
        api.upload_video(file, caption='Video Caption')
        print('Video uploaded to Instagram')

def tiktok_upload(video_file_path, username, password):
    # Create a TikTok API client
    api = pytiktok.Client(username, password)

    # Read the video file and upload it to TikTok
    with open(video_file_path, 'rb') as file:
        api.upload(file, caption='Video Caption')
        print('Video uploaded to TikTok')

if __name__ == '__main__':
    main()