import uuid
from pathlib import Path
import os

from fastapi import UploadFile, HTTPException

IMAGES_DIR = Path("images")
IMAGES_URL = "/images"
ALLOWED_TYPES = {
    "image/jpeg":"jpg",
    "image/png":"png",
    "image/bmp":"bmp",
    "image/webp":"webp"
}

IMAGES_DIR.mkdir(exist_ok=True)

def save_image(file: UploadFile, folder:str):
    extension = ALLOWED_TYPES.get(file.content_type)
    if not extension:
        raise HTTPException(status_code=415, detail="Only JPG, PNG, BMP, and WEBP images are allowed.")

    content = file.file.read()
    folder_path = IMAGES_DIR/folder
    folder_path.mkdir(exist_ok=True)
    file_name = f"{uuid.uuid4().hex}.{extension}"
    (folder_path/file_name).write_bytes(content)

    return f"{IMAGES_URL}/{folder}/{file_name}"


