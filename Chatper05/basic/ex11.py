from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload/multiple")
async def upload_multiple(files: list[UploadFile] = File(...)):
    filenames = [f.filename for f in files]
    return {"filenames": filenames}