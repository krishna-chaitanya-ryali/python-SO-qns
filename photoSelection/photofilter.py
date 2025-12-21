import cv2
import os
import shutil
import numpy as np
from pathlib import Path
from PIL import Image, ExifTags
from pillow_heif import register_heif_opener

# Register HEIC reader
register_heif_opener()

# BASE DIRECTORY
BASE = r"D:\Iphone_data_nov25\All_Sorted_By_Year"
NOF = Path(BASE) / "No_Faces"
UNK = Path(BASE) / "Unknown"

# LIBRARY: HAAR CASCADE FOR FACE DETECTION
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# ------------------------------------------------------------
# HEIC → JPG CONVERSION
# ------------------------------------------------------------
def convert_heic_to_jpg(src):
    jpg_path = src.with_suffix(".jpg")
    try:
        img = Image.open(src)
        img = img.convert("RGB")
        img.save(jpg_path, "JPEG", quality=95)
        src.unlink()  # delete HEIC
        return jpg_path
    except:
        return src


# ------------------------------------------------------------
# FACE + HUMAN-TRACE DETECTION
# ------------------------------------------------------------
def has_face_or_human(img_path):
    try:
        img = cv2.imread(str(img_path))
        if img is None:
            return False

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 1️⃣ FACE DETECTION
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        if len(faces) > 0:
            return True

        # 2️⃣ HUMAN TRACE (SKIN-TONE)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 30, 60], dtype=np.uint8)
        upper = np.array([20, 150, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)

        ratio = cv2.countNonZero(mask) / (img.shape[0] * img.shape[1])

        return ratio > 0.05  # if >5% skin-tone → human present
    except:
        return False


# ------------------------------------------------------------
# GET YEAR FROM EXIF (fallback = modified year)
# ------------------------------------------------------------
def get_year(img_path):
    try:
        img = Image.open(img_path)
        exif = img._getexif()

        if exif:
            for tag, val in exif.items():
                decoded = ExifTags.TAGS.get(tag, tag)
                if decoded == "DateTimeOriginal":
                    return val.split(":")[0]
    except:
        pass

    # fallback
    return str(Path(img_path).stat().st_mtime_ns)[:4]


# ------------------------------------------------------------
# MOVE IMAGE TO YEAR FOLDER
# ------------------------------------------------------------
def move_to_year(img_path):
    year = get_year(img_path)
    year_folder = Path(BASE) / year
    year_folder.mkdir(exist_ok=True)
    shutil.move(str(img_path), str(year_folder / img_path.name))


# ------------------------------------------------------------
# SPLIT EACH YEAR FOLDER INTO PARTS (3000)
# ------------------------------------------------------------
def split_year_folders(max_files=3000):
    for folder in Path(BASE).iterdir():
        if not folder.is_dir():
            continue

        if folder.name in ["No_Faces", "Unknown"]:
            continue

        files = sorted([f for f in folder.iterdir() if f.is_file()])
        total = len(files)

        if total <= max_files:
            continue

        print(f"Splitting {folder.name} ({total} files)...")
        part = 1

        for i in range(0, total, max_files):
            part_folder = folder / f"{folder.name}_part{part}"
            part_folder.mkdir(exist_ok=True)

            chunk = files[i:i + max_files]
            for img in chunk:
                shutil.move(str(img), str(part_folder / img.name))

            part += 1


# ------------------------------------------------------------
# MAIN PROCESS
# ------------------------------------------------------------
def process_folder(folder):
    for img in list(folder.iterdir()):
        if not img.is_file():
            continue

        ext = img.suffix.lower()

        # convert HEIC → JPG
        if ext == ".heic":
            img = convert_heic_to_jpg(img)

        # only process image types
        if img.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue

        # detect human
        if has_face_or_human(img):
            move_to_year(img)
        else:
            # stay in No_Faces
            if folder.name != "No_Faces":
                shutil.move(str(img), str(NOF / img.name))


# execute
print("Reprocessing No_Faces...")
process_folder(NOF)

print("Reprocessing Unknown...")
process_folder(UNK)

print("Splitting year folders...")
split_year_folders()

print("🎉 PROCESS COMPLETED SUCCESSFULLY!")
