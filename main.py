from fastapi import FastAPI, Request
import subprocess
import threading
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online 🚀"}

@app.post("/download")
async def download_video(request: Request):
    print("✅ Requête POST reçue sur /download")

    try:
        data = await request.json()
        url = data.get("url")
        print(f"➡️ URL reçue : {url}")

        if not url:
            print("❌ Aucune URL reçue.")
            return {"error": "No URL provided"}

        filename = "video.mp4"
        cmd = ["yt-dlp", url, "-o", filename]

        print("🚀 Lancement du téléchargement...")
        subprocess.run(cmd, check=True)
        print("✅ Téléchargement terminé.")
        return {"status": "success", "file": filename}

    except Exception as e:
        print(f"❌ Erreur : {e}")
        return {"status": "error", "details": str(e)}

def keep_alive_loop():
    while True:
        print("⏳ Keep alive actif...")
        time.sleep(60)

threading.Thread(target=keep_alive_loop, daemon=True).start()
