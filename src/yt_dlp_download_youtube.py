import yt_dlp

def download_video(url, output_path, file_name):
    ydl_opts = {
        'outtmpl': f'{output_path}/{file_name}',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=MNn9qKG2UFI"
    output_path = "../data/traffic"
    file_name = "video.mp4"
    download_video(url, output_path, file_name)