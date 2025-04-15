import os
from PIL import Image

def convert_and_compress_images_to_webp(input_folder, quality=80):
    """
    Convierte imágenes a formato WEBP y las comprime para optimizar su peso.

    Args:
        input_folder (str): Carpeta de entrada con las imágenes originales.
        quality (int): Calidad de la imagen WEBP (1-100). Valores más bajos reducen el peso.
    """
    valid_extensions = [".jpg", ".jpeg", ".png"]
    converted_count = 0

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            file = file.strip()
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in valid_extensions:
                file_path = os.path.join(root, file)
                with Image.open(file_path) as img:
                    if img.mode in ("P", "L"):
                        img = img.convert("RGB")
                    output_file_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".webp")
                    img.save(output_file_path, "WEBP", quality=quality)
                    converted_count += 1

    print(f"Total de imágenes convertidas y comprimidas: {converted_count}")

if __name__ == "__main__":
    # Código ejecutable solo si se ejecuta directamente
    input_folder = r"D:\Proyectos-local\Proyectos Web\agropuma.com.pe\NUEVAS IMAGENES\FOTOS 03-04-25"
    output_folder = os.path.join(input_folder, "converted_webp")
    os.makedirs(output_folder, exist_ok=True)
    convert_and_compress_images_to_webp(input_folder, quality=75)