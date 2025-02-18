#!/bin/bash

# Archivo de salida
OUTPUT_FILE="resultado.txt"
> "$OUTPUT_FILE"  # Vaciar el archivo si existe

# Recorrer cada carpeta en el directorio actual
for folder in */; do
    [ -d "$folder" ] || continue  # Verificar que es una carpeta

    echo "Procesando carpeta: $folder"

    # Procesar archivos .txt y .docx dentro de la carpeta
    for file in "$folder"*.txt "$folder"*.docx; do
        [ -e "$file" ] || continue  # Saltar si no hay archivos

        echo "Procesando archivo: $file"
        echo "===== $file =====" >> "$OUTPUT_FILE"

        case "$file" in
            *.txt)
                cat "$file" >> "$OUTPUT_FILE"
                ;;
            *.docx)
                pandoc "$file" -t plain >> "$OUTPUT_FILE"
                ;;
        esac

        echo -e "\n" >> "$OUTPUT_FILE"
    done
done

echo "Proceso terminado. Revisa el archivo $OUTPUT_FILE"
