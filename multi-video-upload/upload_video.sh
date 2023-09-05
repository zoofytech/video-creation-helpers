#!/usr/bin/env bash

# Set the video file path
video_file_path=$1

# Set the maximum video duration for TikTok and Instagram (in seconds)
MAX_VIDEO_DURATION=60

# Set the YouTube API credentials
client_secret_file=$2
scopes='https://www.googleapis.com/auth/youtube.upload'
api_service_name='youtube'
api_version='v3'

# Set the Instagram API credentials
instagram_username=$3
instagram_password=$4

# Set the TikTok API credentials
tiktok_username=$5
tiktok_password=$6

# Check the video duration
video_duration=$(get_video_duration "$video_file_path")

# Split the video into multiple videos if necessary for Instagram and TikTok
if [[ "$video_duration" -gt "$MAX_VIDEO_DURATION" ]]; then
    split_video "$video_file_path" "$MAX_VIDEO_DURATION"
fi

# Upload the video to YouTube if it's not split
if [[ "$video_duration" -le "$MAX_VIDEO_DURATION" ]]; then
    youtube_upload "$video_file_path" "$client_secret_file" "$scopes" "$api_service_name" "$video_title" "$video_description"
fi

# Upload the video to Instagram
instagram_upload "$video_file_path" "$instagram_username" "$instagram_password"

# Upload the video to TikTok
tiktok_upload "$video_file_path" "$tiktok_username" "$tiktok_password"

# Function to get the video duration using FFmpeg
get_video_duration() {
    local video_file_path="$1"
    local duration
    duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$video_file_path")
    echo "$duration"
}

# Function to split the video into multiple parts
split_video() {
    local video_file_path="$1"
    local max_duration="$2"
    local video_duration
    video_duration=$(get_video_duration "$video_file_path")
    local num_videos
    num_videos=$((video_duration / max_duration))
    for ((i = 0; i <= num_videos; i++)); do
        local start_time=$((i * max_duration))
        local end_time=$((start_time + max_duration))
        local out_file="${video_file_path%.*}_part_${i}.mp4"
        ffmpeg -i "$video_file_path" -ss "$start_time" -to "$end_time" -c copy "$out_file" -y
    done
}
