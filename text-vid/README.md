# Subtitle Video Generator

This Python script generates a video with subtitles from an input audio file and a text file containing subtitle content. It allows you to add an intro and outro video to the final output as well.

## Prerequisites

Before running the script, ensure you have the following prerequisites:

1. Python 3.x installed on your system.
2. Required Python libraries, which can be installed using pip:
   - moviepy
   - pydub

You can install these libraries using the following commands:

```bash
pip install moviepy
pip install pydub
```

## Usage

1. Place your input audio file (e.g., `sample_audio.mp3`) in the same directory as the script.
2. Create a text file (e.g., `subtitles.txt`) containing the subtitle content. Each line in the text file represents a subtitle.
3. Prepare the intro and outro video files you want to add to the final video.
4. Run the script with the following command:

```bash
python subtitle_video_generator.py --audio sample_audio.mp3 --textfile subtitles.txt --intro intro_video.mp4 --outro outro_video.mp4
```

Replace the arguments with your specific file paths.

- `--audio`: Specifies the input audio file.
- `--textfile`: Specifies the text file containing subtitle content.
- `--intro`: Specifies the intro video file.
- `--outro`: Specifies the outro video file.

The script will generate a video with subtitles and save it as `output_video_with_intro_outro_black_background.mp4`.

## Customization

You can customize the appearance of the subtitles by modifying the `create_subtitles` function in the script. You can adjust font size, text color, background color, and other visual elements to match your preferences.

## License

This script is provided under the MIT License. Feel free to modify and use it according to your needs.

## Acknowledgments

- This script uses the MoviePy library for video editing and the PyDub library for audio processing.


Make sure to replace `subtitle_video_generator.py` with the actual filename of your script. 