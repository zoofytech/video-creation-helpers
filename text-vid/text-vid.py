import argparse
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
from pydub import AudioSegment
import textwrap

# Define a function to parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Generate a video with subtitles.")
    parser.add_argument("--audio", type=str, required=True, help="Input audio file (e.g., sample_audio.mp3)")
    parser.add_argument("--textfile", type=str, required=True, help="Text file containing subtitles content")
    parser.add_argument("--intro", type=str, required=True, help="Intro video file")
    parser.add_argument("--outro", type=str, required=True, help="Outro video file")
    return parser.parse_args()

# Parse command line arguments
args = parse_args()

# Load the audio file and get its duration
audio = AudioSegment.from_file(args.audio)
audio_duration = len(audio) / 1000  # Convert milliseconds to seconds

# Read the text content from the specified file
with open(args.textfile, 'r') as text_file:
    text_content = text_file.read()

# Split the text into sentences
sentences = textwrap.wrap(text_content, width=50)  # Adjust the width as needed

# Create a function to generate subtitles as video frames
def create_subtitles(t):
    current_sentence = sentences[min(int(t), len(sentences) - 1)]
    text_clip = TextClip(current_sentence, fontsize=36, color='white')
    
    # Add a black background for the text
    text_clip = text_clip.on_color(size=(1920, 1080), color=(0, 0, 0), col_opacity=1)
    
    text_clip = text_clip.set_duration(2)  # Display each sentence for 2 seconds
    text_clip = text_clip.set_position(('center', 'bottom'))
    text_clip = text_clip.set_start(t)
    return text_clip

# Create an empty video with a black background and the same duration as the audio in 1080p resolution
video = VideoFileClip("empty_black_background_1080p.mp4").set_duration(audio_duration).resize(height=1080)

# Generate subtitles for the entire duration of the audio
subtitles = [create_subtitles(t) for t in range(0, int(audio_duration), 2)]

# Concatenate the intro video, subtitles, and outro video
intro_video = VideoFileClip(args.intro)
outro_video = VideoFileClip(args.outro)

final_video = concatenate_videoclips([intro_video, video] + subtitles + [outro_video])

# Set the audio of the final video
final_video = final_video.set_audio(audio)

# Write the final video to a file
final_video.write_videofile("output_video_with_intro_outro_black_background.mp4", codec='libx264', fps=24)
