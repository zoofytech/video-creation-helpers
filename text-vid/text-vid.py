#!/usr/bin/env python3
import argparse
from pydub import AudioSegment
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

class TextInserter:
  def __init__(self, video_file, transcript_file, output_file):
    # Open the video file and extract the audio
    self.video = VideoFileClip(video_file)
    self.audio = self.video.audio

    # Get the duration of the audio
    self.duration = self.audio.duration

    # Create a list to store the text clips
    self.text_clips = []

    # Open the transcript file and iterate through the lines
    with open(transcript_file) as f:
      for line in f:
        start, end, text = line.strip().split("\t")
        start_time = int(start) / 1000
        end_time = int(end) / 1000
        text_clip = TextClip(text, fontsize=24, color='white', bg_color='black').set_duration(end_time - start_time)
        text_clip = text_clip.set_pos('center').set_start(start_time)
        self.text_clips.append(text_clip)

    # Set the output file
    self.output_file = output_file

  def insert_text(self):
    # Combine the text clips, audio, and video
    final_clip = CompositeVideoClip(self.text_clips + [self.video.set_audio(self.audio)])

    # Write the final video to a file
    final_clip.write_videofile(self.output_file)

# Add command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("video_file", help="path to the input video file")
parser.add_argument("transcript_file", help="path to the transcript file")
parser.add_argument("output_file", help="path to the output video file")
args = parser.parse_args()

# Create a TextInserter object and insert the text
inserter = TextInserter(args.video_file, args.transcript_file, args.output_file)
inserter.insert_text()
