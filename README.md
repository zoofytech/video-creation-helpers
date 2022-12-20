# multi-video-upload
Code that helps upload videos to TikTok Instagram and YouTube

# Requirements  
1. ffmpeg - https://ffmpeg.org/download.html 
2. requirements.txt - `pip install -r requirements.txt `
3. To use the YouTube API to upload a video, you will need to obtain a client secret file that contains the necessary authentication information. Here are the steps to obtain a client secret file:

    Go to the Google Cloud Console (https://console.cloud.google.com/).
    Click the "Select a project" dropdown menu and create a new project or select an existing project.
    Click the "APIs & Services" menu and then click the "Library" link.
    Search for the "YouTube Data API" and click on the API to open the details page.
    Click the "Enable" button to enable the API.
    Click the "Credentials" menu and then click the "Create credentials" button.
    Select "OAuth client ID" as the type of credential to create.
    Select "Web application" as the application type.
    Enter a name for the client and specify the authorized redirect URIs.
    Click the "Create" button to create the client ID.
    Click the "Download JSON" button to download the client secret file.
    
## Usage

To use this script, you can simply run it from the command line with the following arguments:

```
./upload_video.sh path/to/video.mp4 3600 client_secret.json instagram_username instagram_password tiktok_username tiktok_password video_title video_description
```

This will upload the video located at `path/to/video.mp4` to YouTube, Instagram, and TikTok. If the video duration is more than 3600 seconds (1 hour), it will be split into multiple videos before uploading. The script will use the specified client secret file, Instagram username and password, and TikTok username and password to authenticate the API requests.