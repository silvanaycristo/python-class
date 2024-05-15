'''
sitios_restriccion.py: Script para identificación de sitios de restricción. 

Este script identifica los sitios de restricción en una secuencia de ADN basándose en un patrón de reconocimiento de enzima específico. La secuencia de ADN se lee desde un archivo de texto, y el script devuelve las posiciones de inicio de cualquier sitio de restricción encontrado que coincida con el patrón dado.

Uso: 
  python restriction_sites_script.py <path_to_dna_file> <restriction_pattern>

Argumentos: 
  <path_to_dna_file>: Ruta al archivo que contiene la secuencia de ADN.
  <restriction_pattern>: Patrón de la enzima de restricción a buscar en la secuencia.
'''

# restriction_sites_script.py

import argparse
from dna_analysis.operations.restriction_sites import find_restriction_sites
from dna_analysis.utils.file_io import read_dna_sequence

def main():
    parser = argparse.ArgumentParser(description="Identifica los sitios de restricción en una secuencia de ADN según un patrón dado.")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")
    parser.add_argument("pattern", type=str, help="Patrón de la enzima de restricción a buscar en la secuencia.")

    args = parser.parse_args()
    file_path = args.file
    pattern = args.pattern

    try:
        # Leer la secuencia del archivo
        sequence = read_dna_sequence(file_path)

        # Buscar los sitios de restricción
        sites = find_restriction_sites(sequence, pattern)

        # Mostrar las posiciones de los sitios de restricción
        if sites:
            print(f"Sitios de restricción encontrados en las posiciones: {sites}")
        else:
            print("No se encontraron sitios de restricción.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
