from flask import Flask, render_template, request, redirect, url_for, flash
import os
from downloader import download_video

app = Flask(__name__)
app.secret_key = "supersecretkey"  # 플래시 메시지에 필요한 비밀 키


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["url"]
        download_path = request.form["path"]

        if not video_url or not download_path:
            flash("Please provide both a URL and a download path.")
        else:
            try:
                download_video(video_url, download_path)
                flash(f"Download completed! Video saved to {download_path}")
            except Exception as e:
                flash(f"An error occurred: {e}")

        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

