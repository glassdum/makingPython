import os
import yt_dlp


def download_video(video_url, download_path):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(download_path, "%(title)s.%(ext)s"),
        "merge_output_format": "mp4",
        "postprocessors": [{"key": "FFmpegMetadata"}],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        title = info_dict.get("title", "video").replace(" ", "_")
        ydl_opts["outtmpl"] = os.path.join(download_path, f"{title}.%(ext)s")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
