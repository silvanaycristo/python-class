'''
NAME
    dna_nucleotide_counter.py

VERSION
    1.0

AUTHOR
    Silvana Yalú Cristo Martínez

DESCRIPTION
    Este programa lee una secuencia de ADN desde un archivo y cuenta las ocurrencias de cada nucleótido (A, C, G, T).

CATEGORY
    Análisis de secuencia de ADN/Bioinformática 

USAGE
    % python dna_nucleotide_counter.py <archivo.txt>

ARGUMENTS
    archivo.txt: El archivo que contiene la secuencia de ADN a analizar.

METHOD
    Se lee la secuencia de ADN desde un archivo y se cuentan las ocurrencias de cada uno de los nucleótidos mediante un diccionario.

SEE ALSO
    Otros programas de análisis de ADN pueden incluir alineamiento de secuencias, predicción de genes, etc. 
'''

# ===========================================================================
# =                            imports
# ===========================================================================
# No se requieren módulos externos para este programa.

# ===========================================================================
# =                            Command Line Options
# ===========================================================================
# Este programa actualmente no procesa opciones de línea de comandos, pero se podrían agregar para especificar el archivo de entrada, por ejemplo.

# ===========================================================================
# =                            functions
# ===========================================================================
# No se definen funciones adicionales en esta versión del programa.

# ===========================================================================
# =                            main
# ===========================================================================

# step 1. Abrir el archivo y leer la secuencia de ADN
with open('archivo.txt', 'r') as file:
    dna_sequence = file.read()

# step 2. Inicializar el diccionario para contar nucleótidos
nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# step 3. Contar las ocurrencias de cada nucleótido
for nucleotide in dna_sequence:
    if nucleotide in nucleotide_counts:
        nucleotide_counts[nucleotide] += 1

# Imprimir los resultados
for nucleotide, count in nucleotide_counts.items():
    print(f'El símbolo {nucleotide} aparece {count} veces.')




