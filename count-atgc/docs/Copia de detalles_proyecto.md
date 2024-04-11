# Descripción del script 

Fecha: Jueves, 04 de Abril de 2024

**Participantes**:

- Silvana Yalú Cristo Martínez: silvanac@lcg.unam.mx 

## Descripción del Problema

La necesidad de contar la ocurrencia de cada nucleótido (adenina (A), citosina (C), guanina (G) y timina (T)) en secuencias de ADN es fundamental para diversas aplicaciones en bioinformática y genética. Este script automatiza el proceso, proporcionando una herramienta rápida y eficiente para el análisis de secuencias de ADN.



## Especificación de Requisitos

Requisitos funcionales

Requisito 1: El script debe leer secuencias de ADN desde un archivo de texto plano.
Requisito 2: El script debe contar la ocurrencia de cada uno de los nucleótidos (A, C, G, T) en la secuencia.
Requisito 3: El script debe imprimir el conteo de cada nucleótido en la consola.

Requisitos no funcionales

Requisito 1: El script debe ser ejecutable en cualquier sistema con Python instalado, sin necesidad de dependencias externas.
Requisito 2: El script debe manejar archivos de cualquier tamaño, optimizando el uso de la memoria.
Requisito 3: El script debe proveer mensajes de error claros para archivos no encontrados o formatos de archivo inválidos.


## Análisis y Diseño

```
# Logica del código 

El script inicia abriendo el archivo especificado por el usuario, leyendo su contenido en una cadena de texto. Utiliza un diccionario para contar las ocurrencias de cada nucleótido y luego imprime los resultados.

```

Formato de los archivos input: Archivo de texto plano (.txt) con una secuencia de ADN sin espacios ni caracteres especiales, excepto los nucleótidos A, C, G, T.

Formato de los archivos output o mensajes a imprimir en pantalla: Mensajes de consola que indican el número de ocurrencias de cada nucleótido en el formato El símbolo X aparece Y veces.


#### Caso de uso: 

```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada con secuencia de ADN
                 v
         +-------+--------------------+
         |  Programa                  |
         | dna_nucleotide_counter.py  |
         +----------------------------+
```

- **Actor**: Usuario
- **Descripción**: El usuario proporciona un archivo de entrada con una secuencia de ADN para su análisis.

- **Flujo principal**:

1. El usuario ejecuta el script desde la línea de comandos, especificando el archivo de entrada.
2. El script lee la secuencia de ADN del archivo.
3. El script cuenta las ocurrencias de cada nucleótido.
4. El script imprime el conteo de cada nucleótido en la consola.
	
- **Flujos alternativos**:

- Si no se proporciona un archivo, entonces el programa deberá imprimir un mensaje de error especificando que se necesita un archivo de entrada.
- Si el formato del archivo no es correcto (por ejemplo, contiene caracteres no válidos), imprimir a pantalla un mensaje de error que indique el problema.
- Si el archivo está vacío, el programa imprimirá el conteo de cada nucleótido como 0. 
                

