from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import StreamingResponse, FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import shutil
import os
from fastapi.responses import JSONResponse
from vehicle import detect_and_stream, uploaded_video_path

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open(uploaded_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return JSONResponse(content={"message": "Video uploaded successfully."})


@app.get("/stream")
def stream():
    if not os.path.exists(uploaded_video_path):
        return {"error": "No uploaded video found. Please upload one first."}
    return StreamingResponse(detect_and_stream(uploaded_video_path), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/download")
def download_video():
    if not os.path.exists(uploaded_video_path):
        return {"error": "No processed video available."}
    return FileResponse(path=uploaded_video_path, media_type='video/mp4', filename="processed_output.mp4")
