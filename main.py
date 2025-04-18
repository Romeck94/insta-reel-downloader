from fastapi import FastAPI, Request
import subprocess
import threading
import time

app = FastAPI()

# ✅ Route GET pour vérifier que le serveur répond
@app.get("/")
def read_root():
    return {"status": "online 🚀"}

# ✅ Route POST pour télécharger un reel
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

# 🔁 Keep Alive thread pour empêcher Render de s'endormir
def keep_alive_loop():
    while True:
        print("⏳ Keep alive actif...")
        time.sleep(60)

# 🟢 Lancer le keep-alive dès le démarrage
threading.Thread(target=keep_alive_loop, daemon=True).start()
