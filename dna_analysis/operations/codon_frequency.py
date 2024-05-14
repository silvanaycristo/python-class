"""
codon_frequency.py: Módulo para calcular la frecuencia de codones en secuencias de ADN.

Este módulo analiza la frecuencia con la que aparecen los codones en una secuencia de ADN dada.
La información es útil para estudios de genética y bioinformática que requieren entender el uso de codones.

Funciones:
- calculate_codon_frequency(sequence): Devuelve un diccionario con la frecuencia de cada codón.
"""

def calculate_codon_frequency(sequence):
    """
    Calcula la frecuencia de cada codón en una secuencia de ADN.

    Args:
        sequence (str): La secuencia de ADN a analizar.

    Returns:
        dict: Un diccionario donde las claves son los codones y los valores son sus frecuencias.

    Raises:
        ValueError: Si la secuencia contiene caracteres no válidos o es demasiado corta para formar codones.
    """
    from ..utils.validators import validate_dna_sequence
    validate_dna_sequence(sequence)  # Validar usando la función de validators.py
    
    if len(sequence) < 3:
        raise ValueError("La secuencia debe tener al menos tres nucleótidos para formar un codón.")
    
    # Inicializar el diccionario de frecuencia de codones
    codon_freq = {}
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3].upper()
        if codon in codon_freq:
            codon_freq[codon] += 1
        else:
            codon_freq[codon] = 1
    
    return codon_freq

if __name__ == "__main__":
    # Prueba de funcionalidad.
    test_sequence = "ATGCGTATGCCGTAATG"
    print(f"Frecuencia de codones: {calculate_codon_frequency(test_sequence)}")
