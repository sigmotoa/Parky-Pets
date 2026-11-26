import uuid
from pathlib import Path
import os
from fastapi import UploadFile, HTTPException
from dotenv import load_dotenv


load_dotenv()

STORAGE_BACKEND = os.getenv("STORAGE_BACKEND", "supabase")

def _supabase():
    from supabase import Client, create_client
    return create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SERVICE_KEY"])

IMAGES_DIR = Path("/tmp/images")
#IMAGES_DIR = Path("images")
IMAGES_URL = "/images"
ALLOWED_TYPES = {
    "image/jpeg":"jpeg",
    "image/jpg":"jpg",
    "image/png":"png",
    "image/bmp":"bmp",
    "image/webp":"webp",
    "image/heic":"heic"
}
ALLOWED_FOLDERS = {
    "animals", "users", "products"
}

IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def save_image(file:UploadFile, folder:str):
    if folder not in ALLOWED_FOLDERS:
        raise HTTPException(status_code=400, detail="Folder or model not allowed")
    extension = ALLOWED_TYPES.get(file.content_type)
    if not extension:
        raise HTTPException(status_code=415, detail="File extension not supported, DONKEY")
    content = file.file.read()

    file_name = f"{folder}_{uuid.uuid4().hex}.{extension}"
    if STORAGE_BACKEND == "supabase":
        bucket = os.environ["SUPABASE_BUCKET"]
        path = f"{folder}/{file_name}"
        client = _supabase()
        client.storage.from_(bucket).upload(path, content, {"content_type": file.content_type})
        return client.storage.from_(bucket).get_public_url(path)

    folder_path = IMAGES_DIR/folder
    folder_path.mkdir(exist_ok=True)

    (folder_path/file_name).write_bytes(content)

    return f"{IMAGES_URL}/{folder}/{file_name}"


