import os
import yt_dlp

def download_playlist_audio(playlist_url, output_path='downloads'):
    """
    Download audio files from a YouTube playlist.

    :param playlist_url: URL of the YouTube playlist
    :param output_path: Directory to save downloaded audio files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Configuration for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Best audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract audio
            'preferredcodec': 'mp3',  # Convert to MP3
            'preferredquality': '192',  # 192 kbps quality
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  # Output template
        'nooverwrites': True,  # Don't overwrite existing files
        'no_color': True,  # Disable color output
        'no_warnings': True,  # Suppress warnings
    }

    # Download playlist
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        print(f"Successfully downloaded playlist from: {playlist_url}")
    except Exception as e:
        print(f"Error downloading playlist: {e}")

def main():
    # Get playlist URL from user
    playlist_url = ""

    # Optional: Specify custom download path
    output_path = ""

    # Download playlist
    download_playlist_audio(playlist_url, output_path)

if __name__ == '__main__':
    main()