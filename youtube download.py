# ============================================================
# High Quality YouTube Video Downloader
# Downloads the best available video and audio
# Author: Dhiraj
# ============================================================

import yt_dlp
import os

# ------------------------------------------------------------
# Function to download video
# ------------------------------------------------------------
def download_video(video_url):
    try:
        print("\nFetching video information...")

        # Download options
        ydl_opts = {
            # Best video + best audio
            'format': 'bestvideo+bestaudio/best',

            # Output filename
            'outtmpl': 'downloads/%(title)s.%(ext)s',

            # Merge video and audio into MP4
            'merge_output_format': 'mp4',

            # Show progress
            'progress_hooks': [progress_hook],

            # Ignore playlist
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print("\nDownload completed successfully!")

    except Exception as e:
        print(f"\nError: {e}")


# ------------------------------------------------------------
# Progress callback
# ------------------------------------------------------------
def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get('_percent_str', '0%')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')

        print(
            f"\rDownloading: {downloaded} | Speed: {speed} | ETA: {eta}",
            end=""
        )

    elif d['status'] == 'finished':
        print("\nMerging video and audio...")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
if __name__ == "__main__":

    print("=" * 60)
    print(" HIGH QUALITY YOUTUBE DOWNLOADER ")
    print("=" * 60)

    # Create downloads folder
    os.makedirs("downloads", exist_ok=True)

    # Take URL input
    video_url = input("\nEnter YouTube Video URL: ").strip()

    if not video_url:
        print("Please enter a valid URL.")
    else:
        download_video(video_url)
      
