#!/usr/bin/env bash

# Set the video file path
video_file_path=$1

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

# Set the video title and description
video_title=$7
video_description=$8

# Function to get video duration using FFmpeg
get_video_duration() {
    local duration=$(ffmpeg -i "$1" 2>&1 | grep Duration | awk '{print $2}' | tr -d ,)
    echo "$duration"
}

# Function to calculate the maximum video duration for TikTok
get_max_tiktok_duration() {
    local tiktok_duration=60  # Default maximum TikTok duration in seconds

    # You can add logic here to fetch TikTok's maximum duration dynamically if available.
    # Example: tiktok_duration=$(curl -s https://api.tiktok.com/v1/config/ | jq '.max_video_duration')

    echo "$tiktok_duration"
}

# Function to calculate the maximum video duration for Instagram
get_max_instagram_duration() {
    local instagram_duration=60  # Default maximum Instagram duration in seconds

    # You can add logic here to fetch Instagram's maximum duration dynamically if available.
    # Example: instagram_duration=$(curl -s https://graph.instagram.com/v12.0/instagram_max_video_duration)

    echo "$instagram_duration"
}

# Calculate the maximum video duration for Instagram and TikTok
max_instagram_duration=$(get_max_instagram_duration)
max_tiktok_duration=$(get_max_tiktok_duration)

# Determine the minimum of the two maximum durations
max_video_duration=$((max_instagram_duration < max_tiktok_duration ? max_instagram_duration : max_tiktok_duration))

# Check the video duration
video_duration=$(get_video_duration "$video_file_path")

# Split the video into multiple videos if necessary based on the calculated maximum duration
if [ "$video_duration" -gt "$max_video_duration" ]; then
    echo "Video duration exceeds the maximum allowed duration for Instagram and TikTok. Splitting video..."
    python3 video_upload.py "$video_file_path" "$max_video_duration"
fi

# Upload the video to YouTube
python3 video_upload.py "$video_file_path" "$client_secret_file" "$scopes" "$api_service_name" "$api_version" "$video_title" "$video_description"

# Upload the video to Instagram
python3 video_upload.py "$video_file_path" "$instagram_username" "$instagram_password"

# Upload the video to TikTok
python3 video_upload.py "$video_file_path" "$tiktok_username" "$tiktok_password"
