# Casos de prueba o escenarios

Esta plantilla de casos de prueba proporciona un conjunto de escenarios diseñados para verificar y asegurar el correcto funcionamiento del script dna_nucleotide_argcounter.py, el cual cuenta la frecuencia de nucleótidos en secuencias de ADN. Estos casos de prueba son esenciales para probar sistemáticamente cada aspecto del script, incluyendo su capacidad para manejar datos de entrada esperados e inesperados, y asegurar que el script se comporte de manera predecible y precisa bajo diferentes condiciones.

Propósitos clave de los casos de prueba:

Validación de Funcionalidad: Comprueba que el script cumple con todas las funcionalidades esperadas, como leer un archivo, contar nucleótidos específicos y manejar argumentos de línea de comandos.

Manejo de errores: Evalúa la capacidad del script para identificar y manejar adecuadamente errores comunes, como archivos no encontrados, archivos vacíos o la presencia de caracteres no válidos en la secuencia de ADN.

Robustez: Asegura que el script pueda gestionar situaciones atípicas sin detenerse inesperadamente, proporcionando mensajes de error claros y útiles.

Guía para el usuario:

Preparar datos de prueba: Para cada caso de prueba, prepare un archivo de texto (archivo.txt) con la secuencia de ADN a analizar y colóquelo en el mismo directorio que el script.

Ejecutar pruebas: Corra el script con los argumentos y datos preparados, observando cuidadosamente la salida.

Verificar resultados: Compare los resultados obtenidos con los resultados esperados definidos en los casos de prueba para confirmar si el script se comporta como se espera.

Ojetivo de la plantilla: 

Esta plantilla tiene como objetivo ayudar a detectar posibles errores en el código, garantizar que se cumplen los requisitos de funcionalidad y proporcionar una clara documentación de las pruebas realizadas. Se anima a los usuarios y colaboradores a añadir nuevos casos de prueba si encuentran situaciones únicas no cubiertas por los casos existentes, mejorando así la robustez y fiabilidad del script.
    
    
### Caso de prueba 1: Archivo con todos los nucleótidos válidos

- **Descripción**: Prueba con un archivo que contiene todos los nucleótidos válidos sin repetición para verificar el conteo correcto.
- **Entrada**: `ATCG`
- **Salida esperada**:

The nucleotide A appears 1 times.
The nucleotide C appears 1 times.
The nucleotide G appears 1 times.
The nucleotide T appears 1 times.
 


### Caso de prueba 2: Archivo con caracteres no válidos

- **Descripción**: Verificar que el script maneje correctamente los caracteres no válidos.
- **Entrada**: `ATXG`
- **Salida esperada**:

Sequence contains X, it is an invalid character



### Caso de prueba 3: Archivo vacío

- **Descripción**: Asegurar que el script detecte y maneje un archivo vacío adecuadamente.
- **Entrada**: Archivo vacío
- **Salida esperada**:

Sorry, the file is empty



### Caso de prueba 4: Filtro específico de nucleótidos

- **Descripción**: Prueba la funcionalidad de filtrado para contar solo algunos nucleótidos específicos.
- **Entrada**: `AAGGCCCC`
- **Argumentos adicionales**: `-n A C`
- **Salida esperada**:

The nucleotide A appears 2 times.
The nucleotide C appears 4 times.



### Caso de prueba 5: Archivo no encontrado

- **Descripción**: Verificar el manejo de errores cuando el archivo especificado no existe.
- **Entrada**: Nombre de archivo inexistente
- **Salida esperada**:

Sorry, couldn't find the file
 

        
        