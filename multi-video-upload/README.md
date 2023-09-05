# Multi-video Upload Helper

This project provides a set of scripts to simplify the process of uploading videos to YouTube, Instagram, and TikTok. It also handles video splitting if the duration exceeds the maximum allowed by Instagram and TikTok (60 seconds).

## Prerequisites

Before using these scripts, ensure you have the following:

1. **Python and Pip**: You need Python 3 and Pip installed. You can download Python from the official [Python website](https://www.python.org/downloads/). Pip usually comes pre-installed with Python.

2. **FFmpeg**: FFmpeg is required for video duration calculations and splitting. You can download it from the [FFmpeg website](https://www.ffmpeg.org/download.html) and follow the installation instructions for your operating system.

3. **YouTube API Credentials**: To upload videos to YouTube, you need to set up API credentials in a `client_secret.json` file. Follow these steps to create your API project and obtain the credentials:
    - Go to the [Google Developers Console](https://console.developers.google.com/).
    - Create a new project or select an existing one.
    - In the left sidebar, navigate to **APIs & Services > Credentials**.
    - Click on **Create Credentials > OAuth client ID**.
    - Choose "Other" as the application type.
    - Download the credentials JSON file and save it as `client_secret.json` in the project directory.

4. **Instagram and TikTok API Credentials**: You need to set up API credentials for Instagram and TikTok. Please follow the respective platform's documentation to obtain these credentials.

5. **Tags (Optional)**: If you want to include tags with your videos, create a file named `tags.txt` in the project directory. Each line in the file should contain a tag.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/video-upload-helpers.git
   cd video-upload-helpers
   ```

2. Install the required Python packages using Pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

- **Upload a Video**:

  ```bash
  ./upload_video.sh path/to/your/video.mp4
  ```

  - Replace `path/to/your/video.mp4` with the path to your video file.
  - The script will automatically split the video if it exceeds 60 seconds for Instagram and TikTok.

- **Upload a Video with Tags (Optional)**:

  Create a file named `tags.txt` in the project directory. Each line should contain a tag.

  ```bash
  ./upload_video.sh path/to/your/video.mp4
  ```

  - Replace `path/to/your/video.mp4` with the path to your video file.
  - The script will automatically split the video if it exceeds 60 seconds for Instagram and TikTok.
  - Tags will be read from the `tags.txt` file.

## Examples

Here are some examples of how to use the scripts:

1. Upload a video to YouTube:

   ```bash
   ./upload_video.sh path/to/your/video.mp4
   ```

2. Upload a video to Instagram and TikTok:

   ```bash
   ./upload_video.sh path/to/your/video.mp4
   ```

3. Upload a video with tags to Instagram and TikTok:

   ```bash
   ./upload_video.sh path/to/your/video.mp4
   ```

   - Make sure to have a `tags.txt` file with tags in the project directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.