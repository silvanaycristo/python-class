# Casos de prueba o escenarios

Esta plantilla de casos de prueba está diseñada para guiar a los usuarios y desarrolladores en la validación y verificación del script dna_nucleotide_counter.py, el cual cuenta las ocurrencias de cada uno de los nucleótidos (A, C, G, T) en una secuencia de ADN proporcionada a través de un archivo. Los casos de prueba proporcionados aseguran que el script funcione correctamente en diversas situaciones, desde secuencias de ADN estándar hasta condiciones inusuales como archivos vacíos o secuencias con caracteres no válidos.

Guía para el usuario:

Preparación: Para cada caso de prueba, prepare un archivo de texto (archivo.txt) con la secuencia de ADN a analizar y colóquelo en el mismo directorio que el script.

Ejecución: Ejecute el script desde la línea de comandos usando python dna_nucleotide_counter.py archivo.txt, reemplazando archivo.txt por el nombre de su archivo de prueba.

Verificación: Compare la salida del script con la salida esperada especificada en el caso de prueba. Esto incluye la cantidad exacta de cada nucleótido presente en la secuencia de ADN.

Objetivo de la plantilla: 

Esta plantilla tiene como objetivo ayudar a detectar posibles errores en el código, garantizar que se cumplen los requisitos de funcionalidad y proporcionar una clara documentación de las pruebas realizadas. Se anima a los usuarios y colaboradores a añadir nuevos casos de prueba si encuentran situaciones únicas no cubiertas por los casos existentes, mejorando así la robustez y fiabilidad del script.


    
### Caso de prueba 1: Secuencia simple

- **Entrada**: Secuencia de ADN en el archivo contiene `AGCT`
- **Salida esperada**: 

El símbolo A aparece 1 veces.
El símbolo C aparece 1 veces.
El símbolo G aparece 1 veces.
El símbolo T aparece 1 veces.



### Caso de prueba 2: Secuencia larga con repeticiones

- **Entrada**: Secuencia de ADN en el archivo contiene `AAGGCTCTCTCTGGAACCTT`
- **Salida esperada**: 

El símbolo A aparece 5 veces.
El símbolo C aparece 5 veces.
El símbolo G aparece 5 veces.
El símbolo T aparece 5 veces.



### Caso de prueba 3: Archivo vacío

- **Entrada**: Archivo de entrada está vacío.
- **Salida esperada**: 

El símbolo A aparece 0 veces.
El símbolo C aparece 0 veces.
El símbolo G aparece 0 veces.
El símbolo T aparece 0 veces.



### Caso de prueba 4: Secuencia con caracteres no válidos

- **Entrada**: Secuencia de ADN en el archivo contiene `AGCTXAGB`
- **Salida esperada**: 

El símbolo A aparece 2 veces.
El símbolo C aparece 1 veces.
El símbolo G aparece 2 veces.
El símbolo T aparece 1 veces.



### Caso de prueba 5: Secuencia con solo un tipo de nucleótido

- **Entrada**: Secuencia de ADN en el archivo contiene `AAAAA`
- **Salida esperada**: 

El símbolo A aparece 5 veces.
El símbolo C aparece 0 veces.
El símbolo G aparece 0 veces.
El símbolo T aparece 0 veces.

        
        