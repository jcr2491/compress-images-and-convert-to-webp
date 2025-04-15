import os
from PIL import Image

def convert_and_compress_images_to_webp(input_folder, output_folder, quality=80):
    """
    Convierte imágenes a formato WEBP y las comprime para optimizar su peso.

    Args:
        input_folder (str): Carpeta de entrada con las imágenes originales.
        output_folder (str): Carpeta donde se guardarán las imágenes convertidas.
        quality (int): Calidad de la imagen WEBP (1-100). Valores más bajos reducen el peso.
    """
    valid_extensions = [".jpg", ".jpeg", ".png"]
    converted_count = 0

    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

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

    print(f"Total de imágenes convertidas y comprimidas en '{input_folder}': {converted_count}")

def process_subfolders(main_folder, quality=80):
    """
    Recorre las subcarpetas de una carpeta principal y convierte las imágenes
    en cada subcarpeta a formato WEBP optimizado.

    Args:
        main_folder (str): Ruta de la carpeta principal que contiene subcarpetas con imágenes.
        quality (int): Calidad de la imagen WEBP (1-100). Valores más bajos reducen el peso.
    """
    if not os.path.exists(main_folder):
        print(f"La carpeta principal '{main_folder}' no existe.")
        return

    for root, dirs, files in os.walk(main_folder):
        for subfolder in dirs:
            subfolder_path = os.path.join(root, subfolder)
            output_folder = os.path.join(subfolder_path, "converted_webp")
            print(f"Procesando subcarpeta: {subfolder_path}")
            convert_and_compress_images_to_webp(subfolder_path, output_folder, quality=quality)

if __name__ == "__main__":
    # Ruta de la carpeta principal (cambiar según sea necesario)
    main_folder = r"D:\FOTOS DE PRODUCTOS"  # Cambia esto por la ruta de tu carpeta principal

    # Llamar a la función para procesar las subcarpetas
    process_subfolders(main_folder, quality=75)  # Ajusta la calidad según tus necesidades