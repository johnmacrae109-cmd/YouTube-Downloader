import yt_dlp
from sys import argv

link = input("Enter URL: ")

ydl_opts = {
    'format': 'best',
    'outtmpl': r'C:\Users\johnm\OneDrive\Bureau\Coding\Python\YT_download\%(title)s.%(ext)s',
    'quiet': False,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Get video info first
        info = ydl.extract_info(link, download=False)
        print(f"Title: {info['title']}")
        print(f"Views: {info['view_count']:,}")
        
        # Now download
        print("\nDownloading...")
        ydl.download([link])
        print("Download complete!")
        
except yt_dlp.utils.DownloadError as e:
    print(f"Download error: {e}")
except Exception as e:
    print(f"Error: {e}")