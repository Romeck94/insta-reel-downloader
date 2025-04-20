from fastapi import FastAPI, Request
import subprocess
import threading
import time
import os

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
        # Récupère l'URL du reel envoyée dans la requête
        data = await request.json()
        url = data.get("url")
        print(f"➡️ URL reçue : {url}")

        # Vérifie si une URL a été fournie
        if not url:
            print("❌ Aucune URL reçue.")
            return {"error": "No URL provided"}

        # Nom du fichier vidéo téléchargé
        filename = "video.mp4"

        # Commande pour télécharger la vidéo
        cmd = ["yt-dlp", url, "-o", filename]

        print("🚀 Lancement du téléchargement...")
        subprocess.run(cmd, check=True)
        print("✅ Téléchargement terminé.")

        # Obtient le chemin absolu du fichier vidéo téléchargé
        file_path = os.path.abspath(filename)
        print(f"📁 Fichier téléchargé à : {file_path}")

        # Retourne la réponse avec l'URL du fichier et son chemin complet
        return {"status": "success", "file": filename, "file_path": file_path}

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
