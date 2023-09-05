#!/usr/bin/env python3
import os
import sys
import subprocess

# Import the necessary libraries for uploading to YouTube, Instagram, and TikTok
import google.auth
import googleapiclient.discovery
import googleapiclient.errors
import instagram_private_api
import pytiktok

def main():
    # Get the arguments passed by the shell wrapper script
    video_file_path = sys.argv[1]
    MAX_VIDEO_DURATION = int(sys.argv[2])
    client_secret_file = sys.argv[3]
    scopes = sys.argv[4]
    api_service_name = sys.argv[5]
    api_version = sys.argv[6]
    instagram_username = sys.argv[7]
    instagram_password = sys.argv[8]
    tiktok_username = sys.argv[9]
    tiktok_password = sys.argv[10]
    video_title = sys.argv[11]
    video_description = sys.argv[12]
    
    # Check the video duration
    video_duration = get_video_duration(video_file_path)

    # Split the video into multiple videos if necessary for Instagram and TikTok
    if video_duration > MAX_VIDEO_DURATION:
        split_video(video_file_path, MAX_VIDEO_DURATION)
    
    # Upload the video to YouTube if it's not split
    if video_duration <= MAX_VIDEO_DURATION:
        youtube_upload(video_file_path, client_secret_file, scopes, api_service_name, api_version, video_title, video_description)

    # Upload the video to Instagram
    instagram_upload(video_file_path, instagram_username, instagram_password)

    # Upload the video to TikTok
    tiktok_upload(video_file_path, tiktok_username, tiktok_password)

def get_video_duration(video_file_path):
    # Use ffmpeg to get the duration of the video in seconds
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
    # Use ffmpeg to split the video into multiple videos
    video_duration = get_video_duration(video_file_path)
    num_videos = int(video_duration / max_duration) + 1
    for i in range(num_videos):
        start_time = i * max_duration
        end_time = start_time + max_duration
        out_file = f'{video_file_path}_part_{i}.mp4'
        command = ['ffmpeg', '-i', video_file_path, '-ss', str(start_time), '-to', str(end_time), '-c', 'copy', out_file]
        subprocess.run(command)

def youtube_upload(video_file_path, client_secret_file, scopes, api_service_name, api_version, video_title, video_description):
    # Load the client secrets file
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(info=client_secret_file, scopes=scopes)

    # Create the YouTube API client
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=creds)

    # Get the video file size
    video_size = os.path.getsize(video_file_path)

    # Set the metadata for the video
    body = {
        'snippet': {
            'title': video_title,
            'description': video_description,
            'tags': get_tags(video_file_path),  # Get tags from video or input file
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

def get_tags(video_file_path):
    # Implement logic to extract tags from the video or an input file (e.g., tags.txt)
    # Example: Read tags from a file called tags.txt, one tag per line
    tags = []
    if os.path.exists("tags.txt"):
        with open("tags.txt", "r") as tag_file:
            tags = [line.strip() for line in tag_file.readlines()]
    return tags

def instagram_upload(video_file_path, instagram_username, instagram_password):
    # Create an Instagram API client
    api = instagram_private_api.Client(instagram_username, instagram_password)

    # Read the video file and upload it to Instagram
    with open(video_file_path, 'rb') as file:
        api.upload_video(file, caption='Video Caption')
        print('Video uploaded to Instagram')

def tiktok_upload(video_file_path, tiktok_username, tiktok_password):
    # Create a TikTok API client
    api = pytiktok.Client(tiktok_username, tiktok_password)

    # Read the video file and upload it to TikTok
    with open(video_file_path, 'rb') as file:
        api.upload(file, caption='Video Caption')
        print('Video uploaded to TikTok')

if __name__ == '__main__':
    main()