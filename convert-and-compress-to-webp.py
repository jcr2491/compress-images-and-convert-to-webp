import os
import subprocess
from tkinter import Tk, filedialog, BooleanVar, Checkbutton, Button, Label, Entry, StringVar, messagebox
from PIL import Image

def convert_and_compress_images_to_webp(input_folder, output_folder, quality=80, include_subfolders=True):
    """
    Convierte imágenes a formato WEBP y las comprime para optimizar su peso.

    Args:
        input_folder (str): Carpeta de entrada con las imágenes originales.
        output_folder (str): Carpeta de salida para las imágenes convertidas.
        quality (int): Calidad de la imagen WEBP (1-100). Valores más bajos reducen el peso.
        include_subfolders (bool): Si se deben incluir subcarpetas en la conversión.
    """
    valid_extensions = [".jpg", ".jpeg", ".png"]
    converted_count = 0

    for root, dirs, files in os.walk(input_folder):
        if not include_subfolders and root != input_folder:
            continue
        for file in files:
            file = file.strip()
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in valid_extensions:
                file_path = os.path.join(root, file)
                with Image.open(file_path) as img:
                    if img.mode in ("P", "L"):
                        img = img.convert("RGB")
                    relative_path = os.path.relpath(root, input_folder)
                    output_dir = os.path.join(output_folder, relative_path)
                    os.makedirs(output_dir, exist_ok=True)
                    output_file_path = os.path.join(output_dir, os.path.splitext(file)[0] + ".webp")
                    # Si el archivo ya existe, se reemplaza
                    img.save(output_file_path, "WEBP", quality=quality)
                    converted_count += 1

    return converted_count


def select_input_folder():
    folder = filedialog.askdirectory(title="Seleccionar carpeta de entrada")
    if folder:
        input_folder_var.set(folder)
        # Actualizar automáticamente la carpeta de salida con la subcarpeta "imagenes-convertidas"
        output_folder_var.set(os.path.join(folder, "imagenes-convertidas"))


def select_output_folder():
    folder = filedialog.askdirectory(title="Seleccionar carpeta de salida")
    if folder:
        output_folder_var.set(folder)


def start_conversion():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    include_subfolders = include_subfolders_var.get()

    if not input_folder or not output_folder:
        print("Por favor, selecciona las carpetas de entrada y salida.")
        return

    os.makedirs(output_folder, exist_ok=True)
    converted_count = convert_and_compress_images_to_webp(input_folder, output_folder, quality=75, include_subfolders=include_subfolders)

    # Mostrar mensaje con el número de imágenes convertidas
    if converted_count > 0:
        messagebox.showinfo("Conversión completada", f"Total de imágenes convertidas: {converted_count}")
    else:
        messagebox.showinfo("Conversión completada", "No se encontraron imágenes para convertir.")

    # Abrir la carpeta de salida al finalizar la conversión
    if os.path.isdir(output_folder):
        subprocess.Popen(['explorer', os.path.abspath(output_folder)])
    else:
        messagebox.showerror("Error", "La carpeta de salida no es válida o no existe.")


if __name__ == "__main__":
    root = Tk()
    root.title("Convertir y Comprimir Imágenes a WEBP")

    input_folder_var = StringVar()
    output_folder_var = StringVar()
    include_subfolders_var = BooleanVar(value=True)

    Label(root, text="Carpeta de entrada:").grid(row=0, column=0, sticky="w")
    Entry(root, textvariable=input_folder_var, width=50).grid(row=0, column=1)
    Button(root, text="Seleccionar", command=select_input_folder).grid(row=0, column=2)

    Label(root, text="Carpeta de salida:").grid(row=1, column=0, sticky="w")
    Entry(root, textvariable=output_folder_var, width=50).grid(row=1, column=1)
    Button(root, text="Seleccionar", command=select_output_folder).grid(row=1, column=2)

    Checkbutton(root, text="Examinar subcarpetas", variable=include_subfolders_var).grid(row=2, column=0, columnspan=2, sticky="w")

    Button(root, text="Iniciar conversión", command=start_conversion).grid(row=3, column=0, columnspan=3)

    root.mainloop()