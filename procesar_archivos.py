import os
from docx import Document

# Nombre del archivo de salida
OUTPUT_FILE = "resultado.txt"

def leer_txt(ruta):
    """Lee un archivo de texto y devuelve su contenido."""
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()

def leer_docx(ruta):
    """Lee un archivo DOCX y devuelve su contenido."""
    try:
        doc = Document(ruta)
        return "\n".join([p.text for p in doc.paragraphs])
    except Exception as e:
        return f"Error al leer {ruta}: {e}"

def procesar_archivos():
    """Recorre las carpetas y procesa los archivos .txt y .docx"""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as salida:
        # Recorrer cada carpeta en el directorio actual
        for carpeta in next(os.walk('.'))[1]:  
            print(f"Procesando carpeta: {carpeta}")
            
            # Buscar archivos dentro de la carpeta
            for archivo in os.listdir(carpeta):
                ruta_archivo = os.path.join(carpeta, archivo)
                
                if archivo.endswith(".txt"):
                    contenido = leer_txt(ruta_archivo)
                elif archivo.endswith(".docx"):
                    contenido = leer_docx(ruta_archivo)
                else:
                    continue  # Omitir archivos que no sean .txt o .docx
                
                print(f"Procesando archivo: {archivo}")
                
                # Escribir en el archivo de salida
                salida.write(f"===== {archivo} =====\n")
                salida.write(contenido + "\n\n")

    print(f"Proceso terminado. Revisa el archivo {OUTPUT_FILE}")

if __name__ == "__main__":
    procesar_archivos()
