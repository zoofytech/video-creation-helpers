# Multi-video Upload Helper

This is a script for uploading videos to YouTube, Instagram, and TikTok. It can automatically split videos into parts if they exceed the maximum duration allowed by Instagram and TikTok. Additionally, you can provide tags for the video.

## Prerequisites

Before using this script, ensure that you have the following prerequisites in place:

1. **YouTube API Credentials**:
   - You need to set up API credentials for YouTube. Here's how to do it:
     - Go to the [Google Developers Console](https://console.developers.google.com/).
     - Create a new project or select an existing project.
     - Enable the YouTube Data API v3 for your project.
     - Create credentials for your project and download the client secret file (usually named `client_secret.json`).
     - Place the `client_secret.json` file in the same directory as the script.

2. **Instagram API Credentials**:
   - For Instagram, you'll need your Instagram username and password.
   - Ensure that your Instagram account is active and has permission to post videos.

3. **TikTok API Credentials**:
   - For TikTok, you'll need your TikTok username and password.
   - Ensure that your TikTok account is active and has permission to post videos.

4. **Python Dependencies**:
   - Install the required Python libraries by running the following command in your terminal:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

You can use the provided shell script to run the Python script with the necessary arguments. Here's how to use it:

```bash
./upload_video.sh <video_file_path> <max_video_duration> <client_secret_file> <scopes> <api_service_name> <api_version> <instagram_username> <instagram_password> <tiktok_username> <tiktok_password> <video_title> <video_description> [tag_file_path]
```

- `<video_file_path>`: Path to the video file you want to upload.
- `<max_video_duration>`: Maximum video duration allowed for Instagram and TikTok. The script will automatically split the video if it exceeds this duration.
- `<client_secret_file>`: Path to your YouTube API client secret file (`client_secret.json`).
- `<scopes>`: YouTube API scopes (e.g., `'https://www.googleapis.com/auth/youtube.upload'`).
- `<api_service_name>`: Name of the YouTube API service (e.g., `'youtube'`).
- `<api_version>`: YouTube API version (e.g., `'v3'`).
- `<instagram_username>`: Your Instagram username.
- `<instagram_password>`: Your Instagram password.
- `<tiktok_username>`: Your TikTok username.
- `<tiktok_password>`: Your TikTok password.
- `<video_title>`: Title for the uploaded video.
- `<video_description>`: Description for the uploaded video.
- `[tag_file_path]` (optional): Path to a file containing tags for the video (one tag per line). If not provided, tags will be omitted.

## Example Usage

```bash
./upload_video.sh my_video.mp4 60 client_secret.json 'https://www.googleapis.com/auth/youtube.upload' youtube v3 my_instagram_user my_instagram_pass my_tiktok_user my_tiktok_pass 'My Video Title' 'My Video Description' tags.txt
```

In this example, the script will upload `my_video.mp4` to YouTube, automatically split it into parts if needed, and upload it to Instagram and TikTok. The video title, description, and tags are provided, and tags are read from the `tags.txt` file.

Feel free to customize the script's parameters and use it to upload your videos to multiple platforms easily.