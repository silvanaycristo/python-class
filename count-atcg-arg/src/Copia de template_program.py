'''
NAME
    dna_nucleotide_argcounter.py

VERSION
    1.1

AUTHOR
    Silvana Yalú Cristo Martínez

DESCRIPTION
    Este script permite contar la frecuencia de nucleótidos específicos en una secuencia de ADN proporcionada a través de un archivo. El usuario puede especificar opcionalmente qué nucleótidos desea contar mediante argumentos de línea de comandos.

CATEGORY
    Análisis de secuencia de ADN/Bioinformática 

USAGE
    % python count_atgc.py filename [-n A C G T]

ARGUMENTS
    filename          Obligatorio. Archivo que contiene la secuencia de ADN a analizar.
    -n, --nucleotides Opcional. Lista de nucleótidos a contar (por defecto: A, C, G, T).

METHOD
    El script procesa un archivo de entrada para leer una secuencia de ADN, verifica la validez de los caracteres, y cuenta las ocurrencias de los nucleótidos especificados o de todos si no se especifica ninguno.

SEE ALSO
    Otros programas de análisis de ADN pueden incluir alineamiento de secuencias, predicción de genes, etc. 
'''

# ===========================================================================
# =                            imports
# ===========================================================================
import argparse

# ===========================================================================
# =                            Command Line Options
# ===========================================================================
# La configuración de las opciones de línea de comando se realiza utilizando argparse para manejar argumentos de entrada.

# ===========================================================================
# =                            functions
# ===========================================================================
# Todas las funcionalidades principales están implementadas directamente en el bloque principal, por lo que no se definen funciones adicionales.

# ===========================================================================
# =                            main
# ===========================================================================

# step 1. Configurar y parsear argumentos de línea de comandos
import argparse

parser = argparse.ArgumentParser(description='Count the occurrences of nucleotides in a DNA sequence.')
parser.add_argument('filename', type=str, help='The file containing the DNA sequence.')
parser.add_argument('-n', '--nucleotides', type=str, nargs='+', default=['A', 'C', 'G', 'T'],
                    help='The nucleotides to count. Default is all nucleotides (A, C, G, T).')
args = parser.parse_args()

# step 2. Abrir y leer el archivo de entrada, manejar errores
try:
    with open(args.filename, 'r') as file:
        dna_sequence = file.read().strip().upper()
        if not dna_sequence:
            print("Sorry, the file is empty")
            exit()
except FileNotFoundError:
    print("Sorry, couldn't find the file")
    exit()

# step 3. Verificar la validez de los caracteres en la secuencia de ADN
valid_nucleotides = {'A', 'C', 'G', 'T'}
if not all(char in valid_nucleotides or char.isspace() for char in dna_sequence):
    invalid_chars = set(char for char in dna_sequence if char not in valid_nucleotides and not char.isspace())
    print(f"Sequence contains {', '.join(invalid_chars)}, it is an invalid character")
    exit()

# step 4. Inicializar el diccionario para contar nucleótidos
nucleotide_counts = {nucleotide: 0 for nucleotide in args.nucleotides if nucleotide in valid_nucleotides}

# step 5. Contar las ocurrencias de cada nucleótido especificado
for nucleotide in dna_sequence:
    if nucleotide in nucleotide_counts:
        nucleotide_counts[nucleotide] += 1

# step 6. Imprimir los resultados
for nucleotide, count in nucleotide_counts.items():
    print(f'The nucleotide {nucleotide} appears {count} times.')






