# Descripción del script 

Este script, `dna_nucleotide_argcounter.py` es un script de Python diseñado para contar la frecuencia de nucleótidos específicos en una secuencia de ADN. Permite al usuario especificar opcionalmente los nucleótidos de interés a través de argumentos de línea de comandos.


## Uso

Para usar este script, debe ejecutarse desde la línea de comandos, especificando el archivo de secuencia de ADN y opcionalmente los nucleótidos que desea contar:

python count_atgc.py <archivo_de_secuencia> [-n A C G T]

Ejemplo: 

python count_atgc.py dna_sequence.txt -n A T 


## Salida

El script imprimirá en la consola el recuento de cada nucleótido especificado. Si no se especifican nucleótidos, se contará y mostrará la frecuencia de todos los nucleótidos (A, C, G, T).

## Control de errores

El script maneja varios errores comunes, incluyendo:
- Archivo no encontrado: emite un mensaje "Sorry, couldn't find the file".
- Archivo vacío: emite un mensaje "Sorry, the file is empty".
- Caracteres inválidos en la secuencia de ADN: informa sobre caracteres no nucleotídicos.

## Pruebas

Se recomienda realizar pruebas con diferentes configuraciones de entrada para asegurar la correcta funcionalidad del script. Ejemplos de pruebas pueden incluir: 

- Uso de un archivo con todas las letras válidas.
- Uso de un archivo con letras no válidas para verificar el manejo de errores.
- Uso de un archivo vacío para probar la detección de archivo vacío.

## Datos

El script procesa archivos de texto que contienen secuencias de ADN, las cuales deben estar compuestas únicamente por los caracteres válidos. 

## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte el código fuente y los comentarios incluidos en él.

## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia Apache. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite de la siguiente manera:
"Cristo Martínez, S. (2024). `dna_nucleotide_argcounter.py`. GitHub repository, https://github.com/silvanaycristo/python-class/tree/main/count-atcg-arg

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: silvanac@lcg.unam.mx. 
 