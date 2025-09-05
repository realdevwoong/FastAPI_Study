from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload/filename")
async def upload_filename(file: UploadFile = File(...)):
    return {"filename": file.filename}