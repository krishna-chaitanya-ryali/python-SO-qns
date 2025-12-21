import os
import shutil

# -----------------------------
# CONFIGURATION
# -----------------------------
# Path where all your iPhone folders exist (CHANGE THIS)
MAIN_FOLDER = r"D:\Iphone_data_nov25"

# Output folder
OUTPUT_FOLDER = os.path.join(MAIN_FOLDER, "All_Clean")

# Allowed formats
ALLOWED_EXT = {".jpg", ".jpeg", ".heic"}

# -----------------------------
# CREATE OUTPUT FOLDER
# -----------------------------
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------
# FUNCTION TO GENERATE UNIQUE FILE NAMES
# -----------------------------
def get_unique_path(dst_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_path = os.path.join(dst_folder, filename)

    # If file exists, generate a new name like IMG_001(1).jpg
    while os.path.exists(new_path):
        new_filename = f"{base}_{counter}{ext}"
        new_path = os.path.join(dst_folder, new_filename)
        counter += 1

    return new_path


# -----------------------------
# MAIN LOGIC
# -----------------------------
file_count = 0

print("🔍 Scanning folders...")

# Walk through every folder + subfolder
for root, dirs, files in os.walk(MAIN_FOLDER):
    for file in files:
        ext = os.path.splitext(file)[1].lower()

        # Check if extension is allowed
        if ext in ALLOWED_EXT:
            src_file = os.path.join(root, file)

            # Generate a unique file path
            dst_file = get_unique_path(OUTPUT_FOLDER, file)

            # Copy file
            shutil.copy2(src_file, dst_file)
            file_count += 1
            print(f"✔ Copied: {file}")

print("\n-----------------------------------")
print(f"🎉 Done! Total useful photos copied: {file_count}")
print(f"📁 Output folder: {OUTPUT_FOLDER}")
print("-----------------------------------")
