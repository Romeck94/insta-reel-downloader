from fastapi import FastAPI, Request
import subprocess
import threading
import time

app = FastAPI()

# ✅ Route GET pour tester que le serveur répond
@app.get("/")
def read_root():
    return {"status": "online 🚀"}

# ✅ Route POST pour télécharger un reel
@app.post("/download")
async def download_video(request: Request):
    print("✅ Re
