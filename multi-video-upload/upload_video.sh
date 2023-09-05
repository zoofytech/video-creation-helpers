#!/usr/bin/env bash

# Set the video file path
video_file_path=$1

# Set the maximum video duration
MAX_VIDEO_DURATION=$2

# Set the YouTube API credentials
client_secret_file=$3
scopes='https://www.googleapis.com/auth/youtube.upload'
api_service_name='youtube'
api_version='v3'

# Set the Instagram API credentials
instagram_username=$4
instagram_password=$5

# Set the TikTok API credentials
tiktok_username=$6
tiktok_password=$7

# Check the video duration
video_duration=$(get_video_duration "$video_file_path")

# Split the video into multiple videos if necessary
if [[ "$video_duration" -gt "$MAX_VIDEO_DURATION" ]]; then
    split_video "$video_file_path"
fi

# Upload the video to YouTube
youtube_upload "$video_file_path" "$client_secret_file" "$scopes" "$api_service_name" "$api_version" "$video_title" "$video_description"

# Upload the video to Instagram
instagram_upload "$video_file_path" "$instagram_username" "$instagram_password"

# Upload the video to TikTok
tiktok_upload "$video_file_path" "$tiktok_username" "$tiktok_password"
