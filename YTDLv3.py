import yt_dlp
import time
import sys
import os

if getattr(sys, 'frozen', False):
    # Running as compiled executable
    application_path = sys._MEIPASS
else:
    # Running as script
    application_path = os.path.dirname(os.path.abspath(__file__))

ffmpeg_path = os.path.join(application_path, 'ffmpeg.exe')

while True:    
    link = input("Enter URL, or type 'quit' to end: ")
    
    if link.upper() == "QUIT":
        print('have a good day')
        time.sleep(1)
        break
    

    file_path = input("Enter filepath to folder: ")
    
    

    ydl_opts = {
        'format': 'best',
        'ffmpeg_location': ffmpeg_path,
        'outtmpl': fr'{file_path}\%(title)s.%(ext)s',
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