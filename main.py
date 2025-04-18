from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

# ✅ Route de test GET /
@app.get("/")
def read_root():
    return {"status": "online 🚀"}

# ✅ Route principale POST /download
@app.post("/download")
async def download_video(request: Request):
    print("✅ Requête POST reçue sur /download")

    data = await request.json()
    url = data.get("url")

    print(f"➡️ URL reçue : {url}")

    if not url:
        print("❌ Aucune URL reçue dans le JSON")
        return {"error": "No URL provided"}

    filename = "video.mp4"
    cmd = ["yt-dlp", url, "-o", filename]

    try:
        print("🚀 Lancement du téléchargement avec yt-dlp...")
        subprocess.run(cmd, check=True)
        print("✅ Téléchargement terminé avec succès !")
        return {"status": "success", "file": filename}
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur pendant le téléchargement : {e}")
        return {"status": "error", "details": str(e)}
