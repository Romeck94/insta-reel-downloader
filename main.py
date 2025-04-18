from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

@app.post("/download")
async def download_video(request: Request):
    print("✅ Requête reçue !")

    data = await request.json()
    url = data.get("url")

    print(f"➡️ URL reçue : {url}")

    if not url:
        print("❌ Aucune URL reçue.")
        return {"error": "No URL provided"}

    filename = "video.mp4"
    cmd = ["yt-dlp", url, "-o", filename]

    try:
        print("🚀 Lancement du téléchargement...")
        subprocess.run(cmd, check=True)
        print("✅ Téléchargement terminé.")
        return {"status": "success", "file": filename}
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur pendant le téléchargement : {e}")
        return {"status": "error", "details": str(e)}
