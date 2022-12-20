# multi-video-upload
Code that helps upload videos to TikTok Instagram and YouTube
If the video duration is long, it will automatically split the video into multiple videos and upload them all
# Requirements  
1. ffmpeg - https://ffmpeg.org/download.html 
2. requirements.txt - `pip install -r requirements.txt `
3. YouTube Client Secret - To use the YouTube API to upload a video, you will need to obtain a client secret file that contains the necessary authentication information. Here are the steps to obtain a client secret file:

    1. Go to the Google Cloud Console (https://console.cloud.google.com/).
    1. Click the "Select a project" dropdown menu and create a new project or 1. select an existing project.
    1. Click the "APIs & Services" menu and then click the "Library" link.
    1. Search for the "YouTube Data API" and click on the API to open the details page.
    1. Click the "Enable" button to enable the API.
    1. Click the "Credentials" menu and then click the "Create credentials" button.
    1. Select "OAuth client ID" as the type of credential to create.
    1. Select "Web application" as the application type.
    1. Enter a name for the client and specify the authorized redirect URIs.
    1. Click the "Create" button to create the client ID.
    1. Click the "Download JSON" button to download the client secret file.

## Usage

To use this script, you can simply run it from the command line with the following arguments:

```
./upload_video.sh path/to/video.mp4 3600 client_secret.json instagram_username instagram_password tiktok_username tiktok_password video_title video_description
```

This will upload the video located at `path/to/video.mp4` to YouTube, Instagram, and TikTok. If the video duration is more than 3600 seconds (1 hour), it will be split into multiple videos before uploading. The script will use the specified client secret file, Instagram username and password, and TikTok username and password to authenticate the API requests.