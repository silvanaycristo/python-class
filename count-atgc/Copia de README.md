# Descripción del script 

Este script, `dna_nucleotide_counter.py`, es una herramienta de análisis de secuencia de ADN diseñada para contar las ocurrencias de cada uno de los cuatro nucleótidos (adenina (A), citosina (C), guanina (G) y timina (T)) en una secuencia de ADN proporcionada a través de un archivo de texto.


## Uso

Para usar este script, necesitará tener Python instalado en su sistema. El script se ejecuta desde la línea de comandos de la siguiente manera:

python dna_nucleotide_counter.py <path/to/archivo.txt>

Donde `<path/to/archivo.txt>` debe ser reemplazado por la ruta al archivo que contiene la secuencia de ADN a analizar.


## Salida

El script imprimirá en la consola el conteo de cada nucleótido presente en la secuencia de ADN, de la siguiente forma:

El símbolo A aparece X veces.
El símbolo C aparece X veces.
El símbolo G aparece X veces.
El símbolo T aparece X veces.


## Control de errores

Actualmente, el script no maneja explícitamente errores relacionados con la entrada de archivos no existentes o formatos de archivo incorrectos. Se asume que el archivo de entrada está bien formado y contiene únicamente caracteres válidos para una secuencia de ADN (A, C, G, T).


## Pruebas

Las pruebas manuales se han realizado con varias secuencias de ADN para garantizar la precisión de los conteos de nucleótidos. No se han implementado pruebas automáticas en la versión actual del script.


## Datos

El script espera como entrada un archivo de texto plano (.txt) que contenga una secuencia de ADN sin espacios ni líneas nuevas adicionales.


## Metadatos y documentación

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script, consulte la sección de comentarios dentro del código fuente.


## Código fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Términos de uso

Este script está disponible bajo la licencia Apache. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor cite de la siguiente manera:

"Cristo Martínez, S. (2024). dna_nucleotide_counter.py. GitHub repository, https://github.com/silvanaycristo/python-class/tree/main/count-atgc"

## Contáctenos

Si tiene problemas o preguntas, por favor abra un problema en este repositorio o póngase en contacto con nosotros en: silvanac@lcg.unam.mx.   