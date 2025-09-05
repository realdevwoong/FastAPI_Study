from fastapi import HTTPException, FastAPI,  File, UploadFile
app = FastAPI()

@app.post("/upload/image-only")
async def upload_image(file: UploadFile = File(...)):
    if not (file.filename.endswith(".jpg") or file.filename.endswith(".png")):
        raise HTTPException(status_code=400, detail="Only .jpg and .png allowed")
    return {"filename": file.filename}