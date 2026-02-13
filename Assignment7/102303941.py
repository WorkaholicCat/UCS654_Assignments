import sys
import os
import yt_dlp
from moviepy import VideoFileClip
from pydub import AudioSegment


def download_videos(singer, num_videos):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }
    os.makedirs("downloads", exist_ok=True)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_query = f"ytsearch{num_videos}:{singer} songs"
        ydl.download([search_query])
def convert_and_trim(duration):
    os.makedirs("audio", exist_ok=True)
    trimmed_files = []
    for file in os.listdir("downloads"):
        if file.endswith(".mp4"):
            video_path = os.path.join("downloads", file)
            video = VideoFileClip(video_path)

            audio_path = os.path.join("audio", file.replace(".mp4", ".mp3"))
            video.audio.write_audiofile(audio_path)
            video.close()

            audio = AudioSegment.from_mp3(audio_path)
            trimmed = audio[:duration * 1000]

            trimmed_path = os.path.join("audio", "trimmed_" + file.replace(".mp4", ".mp3"))
            trimmed.export(trimmed_path, format="mp3")
            trimmed_files.append(trimmed_path)
    return trimmed_files

def merge_audio(files, output_file):
    final_audio = AudioSegment.empty()
    for file in files:
        audio = AudioSegment.from_mp3(file)
        final_audio += audio

    final_audio.export(output_file, format="mp3")
    return output_file

def create_mashup(singer, num_videos, duration, output_file):
    download_videos(singer, num_videos)
    trimmed_files = convert_and_trim(duration)
    return merge_audio(trimmed_files, output_file)

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]
    num_videos = int(sys.argv[2])
    duration = int(sys.argv[3])
    output_file = sys.argv[4]

    if num_videos <= 10:
        print("NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    try:
        create_mashup(singer, num_videos, duration, output_file)
        print("Mashup created successfully:", output_file)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
