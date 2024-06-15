import os
from PIL import Image


def convert_to_webp(input_path, output_path):
    # Ouvrir l'image en utilisant Pillow
    image = Image.open(input_path)
    # Sauvegarder l'image au format WebP
    image.save(output_path, format="WEBP")
    print(f"Image converted and saved to {output_path}")


def batch_convert_to_webp(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(
            (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".tif")
        ):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(
                output_directory, f"{os.path.splitext(filename)[0]}.webp"
            )
            convert_to_webp(input_path, output_path)


if __name__ == "__main__":
    input_directory = "input"  # Remplacez par le chemin de votre répertoire d'images
    output_directory = "output"  # Remplacez par le chemin du répertoire de sortie

    batch_convert_to_webp(input_directory, output_directory)
