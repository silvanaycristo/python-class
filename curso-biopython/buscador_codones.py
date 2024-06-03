'''
NAME: 
       Buscador de Codones para marcos de lectura

VERSION: 1.0

AUTHOR: Silvana Martinez

DESCRIPCIÓN: 
        Este script lee un archivo FASTA que contiene secuencias de ADN y encuentra todos los codones para los 6 marcos de lectura.
        Los codones para cada marco de lectura se imprimen en formato FASTA en archivos separados nombrados según los marcos.

CATEGORY:
        Análisis de secuencias de ADN/Bioinformática

USAGE:

    % python buscador_codones.py -i seq.nt.fa
    

ARGUMENTS:
    -i : Archivo FASTA de entrada que contiene las secuencias de ADN.

METHOD:
    El script usa SeqIO de Biopython para leer las secuencias del archivo de entrada y encontrar los codones para los seis marcos de lectura.
    Genera una función que toma el marco de lectura, la secuencia y el nombre del archivo de salida como parámetros y llama a esta función para cada secuencia.

'''

# ===========================================================================
# =                            imports
# ===========================================================================
from Bio import SeqIO
from Bio.Seq import Seq
import argparse

# ===========================================================================
# =                            Command Line Options
# ===========================================================================
parser = argparse.ArgumentParser(description='Encuentra codones para los 6 marcos de lectura a partir de un archivo FASTA.')
parser.add_argument('-i', '--input', required=True, help='Archivo FASTA de entrada')
args = parser.parse_args()

# ===========================================================================
# =                            functions
# ===========================================================================
def find_codons(frame, sequence, output_file_name):
    codons = []
    seq_len = len(sequence)
    for i in range(frame, seq_len, 3):
        if i + 3 <= seq_len:
            codon = str(sequence[i:i+3])  # Convertir cada codón a cadena de texto
            codons.append(codon)
    with open(output_file_name, 'w') as output_file:
        output_file.write(f">Frame_{frame+1}\n")
        output_file.write(" ".join(codons) + "\n")
    print(f"Archivo {output_file_name} creado con éxito.")  # Mensaje de confirmación

# ===========================================================================
# =                            main
# ===========================================================================
if __name__ == "__main__":
    # Leer el archivo de entrada
    input_file = args.input
    sequences = SeqIO.parse(input_file, "fasta")
    
    # Procesar cada secuencia
    for record in sequences:
        seq = str(record.seq)
        seq_obj = Seq(seq)  # Convertir la cadena en un objeto Seq
        # Paso 1 y 2: Procesar los 6 marcos de lectura
        for frame in range(3):
            find_codons(frame, seq, f"Frame_{frame+1}.fa")
            find_codons(frame, seq_obj.reverse_complement(), f"Frame_{frame+4}.fa")

    print("Proceso completado, puedes verificar los archivos de salida generados en el directorio donde ejecutaste el script.")  # Mensaje de confirmaciÃ³n final
