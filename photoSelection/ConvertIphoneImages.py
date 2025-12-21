'''
from config import heic_file,jpg_file,input_folder,output_folder
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()


def convert_heic_to_jpg(heic_filepath, jpg_filepath):
    """Converts a HEIC image to JPG format."""
    try:
        img = Image.open(heic_filepath)
        img.convert('RGB').save(jpg_filepath, 'jpeg')
        print(f"Converted '{heic_filepath}' to '{jpg_filepath}'")
    except Exception as e:
        print(f"Error converting '{heic_filepath}': {e}")


# Example usage:
#heic_file = 'image.heic'
#jpg_file = 'image.jpg'
convert_heic_to_jpg(heic_file, jpg_file)
'''
from config import heic_file,jpg_file,input_folder,output_folder
import os
from PIL import Image
import pillow_heif

# Set input and output folders
#input_folder = "path/to/your/heic/folder"
#output_folder = "path/to/your/output/folder"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Convert all HEIC files to JPG
for file in os.listdir(input_folder):
    if file.lower().endswith(".heic"):
        heic_file_path = os.path.join(input_folder, file)
        jpg_file_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".jpg")

        # Open HEIC image
        heif_image = pillow_heif.open_heif(heic_file_path)

        # Convert to PIL Image and save as JPG
        image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
        image.save(jpg_file_path, "JPEG")

        print(f"Converted: {file} -> {jpg_file_path}")

print("All HEIC files have been converted to JPG.")