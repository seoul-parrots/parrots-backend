import os
from uuid import uuid4

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from starlette.responses import FileResponse

app = FastAPI()
FILE_PATH = "beaks"


class FilePath(BaseModel):
    path: str


@app.on_event("startup")
def check_dir():
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)


@app.post("/upload")
def upload(file: UploadFile = File()):
    filename = os.path.join(FILE_PATH, str(uuid4()) + file.filename)
    bytes = file.file.read()
    with open(filename, "wb") as f:
        f.write(bytes)

    return FilePath(path=filename)


@app.post("/download")
def download(path: FilePath):
    return FileResponse(path.path)
