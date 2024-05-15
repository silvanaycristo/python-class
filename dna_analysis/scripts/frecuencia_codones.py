'''
frecuencia_codones.py.py: Script para calcular la frecuencia de codones en una secuencia de ADN. 

Este script analiza una secuencia de ADN proporcionada a través de un archivo de texto para calcular y mostrar la frecuencia de cada codón presente en la secuencia. Los codones son tríos de nucleótidos, y su frecuencia puede ofrecer información valiosa para estudios genéticos y bioinformáticos.

Uso: 
  python codon_frequency_script.py <path_to_dna_file>

Argumentos:
  <path_to_dna_file>: Ruta al archivo de texto que contiene la secuencia de ADN.
'''


# codon_frequency_script.py

import argparse
from dna_analysis.operations.codon_frequency import calculate_codon_frequency
from dna_analysis.utils.file_io import read_dna_sequence

def main():
    parser = argparse.ArgumentParser(description="Calcula la frecuencia de codones en una secuencia de ADN.")
    parser.add_argument("file", type=str, help="Archivo de ADN del cual leer la secuencia.")

    args = parser.parse_args()
    file_path = args.file

    try:
        # Leer la secuencia del archivo utilizando la función de file_io
        sequence = read_dna_sequence(file_path)

        # Calcular la frecuencia de codones
        codon_freq = calculate_codon_frequency(sequence)

        # Mostrar las frecuencias de codones
        for codon, freq in codon_freq.items():
            print(f"{codon}: {freq}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
