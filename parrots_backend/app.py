import os
from uuid import uuid4

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
FILE_PATH = "beaks"


class FilePath(BaseModel):
    index: str


@app.on_event("startup")
def check_dir():
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)


@app.post("/upload")
def upload(file: UploadFile = File()):
    random_key = str(uuid4())
    _, ext = os.path.splitext(file.filename)
    filename = random_key + ext
    fullpath = os.path.join(FILE_PATH, filename)
    bytes = file.file.read()
    with open(fullpath, "wb") as f:
        f.write(bytes)

    return FilePath(index=filename)


@app.get("/download/{index}")
def download(index: str):

    if not os.path.exists(os.path.join(FILE_PATH, index)):
        raise HTTPException(status_code=404, detail="Item not found")

    fullpath = os.path.join(FILE_PATH, index)

    return FileResponse(fullpath)
