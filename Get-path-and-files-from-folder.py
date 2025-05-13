import os
import pandas as pd

# Define la ruta principal
directorio_principal = r'D:\FOTOS DE PRODUCTOS'

# Lista para almacenar los datos
data = []

# Recorrer cada carpeta dentro del directorio principal
for carpeta_categoria in os.listdir(directorio_principal):
    ruta_categoria = os.path.join(directorio_principal, carpeta_categoria)
    
    # Verificamos que sea una carpeta
    if os.path.isdir(ruta_categoria):
        ruta_converted_webp = os.path.join(ruta_categoria, 'converted_webp')
        
        # Verificar si existe la subcarpeta 'converted_webp'
        if os.path.isdir(ruta_converted_webp):
            for archivo in os.listdir(ruta_converted_webp):
                if archivo.lower().endswith('.webp'):
                    nombre_archivo = os.path.splitext(archivo)[0]  # Nombre sin extensión
                    data.append({'Nombre': nombre_archivo, 'Categoria': carpeta_categoria})

# Crear un DataFrame
df = pd.DataFrame(data)

# Definir ruta de salida del Excel
ruta_excel_salida = os.path.join(directorio_principal, 'listado_productos.xlsx')

# Guardar en Excel
df.to_excel(ruta_excel_salida, index=False)

print(f"Archivo Excel generado exitosamente en: {ruta_excel_salida}")
