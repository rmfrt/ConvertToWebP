import os
from PIL import Image

# Dossier contenant les images à convertir
input_folder = "input"
# Dossier où les images WebP seront enregistrées
output_folder = "output"

# Assurez-vous que le dossier de sortie existe
os.makedirs(output_folder, exist_ok=True)

# Parcourir toutes les images dans le dossier d'entrée
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        output_path = os.path.join(
            output_folder, os.path.splitext(filename)[0] + ".webp"
        )

        # Ouvrir l'image source
        image = Image.open(image_path)

        # Convertir et enregistrer l'image au format WebP
        image.save(output_path, "WEBP")

        print(f"{filename} a été convertie et enregistrée à {output_path}")

print("Conversion terminée.")
