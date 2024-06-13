import os
from PIL import Image

input_folder = "input"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder, os.path.splitext(filename)[0] + ".webp"
        )

        image = Image.open(image_path)

        image.save(output_path, "WEBP")

        print(f"{filename} a été convertie et enregistrée à {output_path}")

print("Conversion terminée.")
