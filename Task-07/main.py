import os
import argparse
import requests
import subliminal
from guessit import guessit
from dotenv import load_dotenv
from babelfish import Language
from subliminal.cli import MutexLock
from subliminal import download_best_subtitles, save_subtitles
from subliminal.providers.opensubtitles import OpenSubtitlesError
    
load_dotenv()

def initialize_providers():
    username = os.getenv("OPENSUBTITLES_USERNAME")
    password = os.getenv("OPENSUBTITLES_PASSWORD")
    if username and password:
        OpenSubtitles(username, password)

def search_subtitles(video_file, language="en"):
    """Search and list subtitles for a given video file."""
    video_metadata = guessit(video_file)
    title = video_metadata.get('title')
    print(f"Searching subtitles for: {title}")

    with MutexLock() as lock:
        # Scan the video file for subtitles
        video = subliminal.scan_video(video_file)
        subtitles = subliminal.search_subtitles({video}, {Language(language)})

        # List all available subtitles
        for idx, subtitle in enumerate(subtitles[video]):
            print(f"{idx + 1}. {subtitle.provider_name} - {subtitle.language} - {subtitle.download_link}")

        return subtitles[video]

def download_subtitle(video_file, subtitle_index, language="en"):
    """Download the selected subtitle for the video."""
    subtitles = search_subtitles(video_file, language)

    if 0 <= subtitle_index < len(subtitles):
        chosen_subtitle = subtitles[subtitle_index]
        print(f"Downloading subtitle: {chosen_subtitle.provider_name} - {chosen_subtitle.language}")

        # Downloading and saving the subtitles
        subliminal.download_subtitles({chosen_subtitle})
        save_subtitles(video_file, [chosen_subtitle], directory=os.path.dirname(video_file))
        print(f"Subtitle saved to {os.path.dirname(video_file)}")
    else:
        print("Invalid subtitle choice")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and download subtitles for a movie file.")
    parser.add_argument('video_file', type=str, help='Path to the mp4 video file')

    # Optional
    parser.add_argument('--language', type=str, default='en', help='Subtitle language (default: en)')
    parser.add_argument('--download', type=int, help='Index of the subtitle to download')

    args = parser.parse_args()
    initialize_providers()

    # To make sure the downloading has begun
    if args.download is not None:
        download_subtitle(args.video_file, args.download - 1, args.language)
    else:
        search_subtitles(args.video_file, args.language)
