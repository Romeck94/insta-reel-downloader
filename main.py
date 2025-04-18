from fastapi import FastAPI, Request
import subprocess
import os

app = FastAPI()

@app.post("/download")
async def download_video(request: Request):
    data = await request.json()
    url = data.get("url")

    if not url:
        return {"error": "No URL provided"}

    filename = "video.mp4"
    cmd = ["yt-dlp", url, "-o", filename]

    try:
        subprocess.run(cmd, check=True)
        return {"status": "success", "file": filename}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "details": str(e)}
