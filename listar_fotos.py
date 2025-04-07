
import os
import pandas as pd



# Ruta de la carpeta que deseas listar
ruta_carpeta = "Steven"



# Recorrer todos los archivos en la carpeta
for archivo in os.listdir(ruta_carpeta):
    # Verificar si el archivo comienza con "_"
    if archivo.startswith("_"):
        # Crear el nuevo nombre eliminando el primer carácter
        nuevo_nombre = archivo[1:]
        
        # Generar las rutas completas (original y nueva)
        ruta_original = os.path.join(ruta_carpeta, archivo)
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)
        
        # Renombrar el archivo
        os.rename(ruta_original, ruta_nueva)
        print(f"Renombrado: {archivo} -> {nuevo_nombre}")


# Listar los archivos en la carpeta
archivos = os.listdir(ruta_carpeta)

# Filtrar solo archivos (opcional, en caso de que existan subcarpetas)
archivos = [archivo for archivo in archivos if os.path.isfile(os.path.join(ruta_carpeta, archivo))]

# Crear un DataFrame con la lista de archivos
df_archivos = pd.DataFrame(archivos, columns=["Nombre del archivo"])

# Exportar el DataFrame a un archivo Excel
ruta_salida = "archivos_listados.xlsx"
df_archivos.to_excel(ruta_salida, index=False)

print(f"Lista de archivos exportada a {ruta_salida}")
