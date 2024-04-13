# Descripción del script 

Fecha: Sábado, 13 de Abril de 2024

**Participantes**:

- Silvana Yalú Cristo Martínez: silvanac@lcg.unam.mx 

## Descripción del Problema

El análisis de secuencias de ADN requiere identificar y contar las frecuencias de los nucleótidos. La tarea manual no solo es propensa a errores sino también ineficiente, especialmente con secuencias largas.

## Especificación de Requisitos

Requisitos funcionales

- Requisito 1: El programa debe leer una secuencia de ADN desde un archivo de texto.
- Requisito 2: El programa debe permitir al usuario especificar qué nucleótidos contar.
- Requisito 3: El programa debe reportar la frecuencia de cada nucleótido especificado.

Requisitos no funcionales

- Requisito 1: El script debe ser ejecutable en cualquier sistema con Python instalado, sin necesidad de dependencias externas.
- Requisito 2: El programa debe ser fácil de usar desde la línea de comandos.
- Requisito 3: El programa debe manejar errores de entrada de manera efectiva, proporcionando mensajes claros de error.

## Análisis y Diseño

```
# Logica del código 

El script utiliza argparse para el manejo de argumentos de línea de comandos, maneja errores de archivos y cuenta los nucleótidos especificados, mostrando los resultados en la consola.

```

Formato de los archivos input que recibe el programa, así como el formato de los archivos output o mensajes a imprimir en pantalla.

- **Formato de entrada**: Archivo de texto con secuencia de ADN (A, T, C, G).
- **Formato de salida**: Mensajes en la consola que indican la cantidad de cada nucleótido contado.


#### Caso de uso: Contar Nucleótidos



```
         +---------------+
         |   Usuario     |
         +-------+-------+
                 |
                 | 1. Proporciona archivo de entrada con secuencia de ADN 
                 v
         +-------+-----------------------+
         | Programa                      |   
         | dna_nucleotide_argcounter.py  |
         +-------------------------------+
```

- **Actor**: Usuario
- **Descripción**: El usuario proporciona un archivo de entrada que contiene una secuencia de ADN y especifica los nucleótidos a contar. 

- **Flujo principal**:

1. El usuario inicia el programa desde la línea de comandos con los argumentos necesarios.
2. El programa valida el archivo y la entrada.
3. El programa cuenta los nucleótidos especificados.
4. El programa imprime los resultados en la consola.
	
- **Flujos alternativos**:

- Si no se proporciona un archivo entonces el programa deberá imprimir un mensaje de error indicando que no se encontró el archivo.
- Si el archivo está vacío, el programa deberá imprimir un mensaje de error indicando que el archivo no contiene datos.
- Si el formato del archivo contiene caracteres no válidos, el programa imprimirá un mensaje de error específico.

 
                

