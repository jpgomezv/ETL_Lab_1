# Reflection Questions - ETL Lab 1

### 1. What is the role of each ETL stage in this laboratory?

*   **Extraction:** Básicamente es recolectar la info. En este lab leemos archivos de diferentes formatos (CSV, JSON, XML) y los convertimos a algo que podamos manejar fácil en Python (un DataFrame de Pandas), así nos olvidamos de qué tipo de archivo eran originalmente.
*   **Transformation:** Aquí es donde "pulimos" los datos. En este caso fue sencillo, solo redondeamos los precios de los carros a dos decimales, pero el punto es dejar la 'data' limpia y consistente para usarla después.
*   **Load:** Es el paso final donde entregamos el trabajo. Guardamos los datos ya procesados en un CSV y en una base de datos SQLite para que sea fácil hacer consultas y análisis después.

### 2. What problems could arise if the transformation step is skipped?

En este laboratorio no tiene demasiada relevancia, ya que solo redondeamos los precios de los carros a dos decimales por conveniencia de lectura (de hecho, redondear los precios podria ser hasta contraproducente si se quiere tener precision absoluta). Sin embargo, en un escenario real, saltarse la transformación podría generar problemas como:
*   Datos sucios
*   Datos duplicados
*   Datos con formatos que no cuadran
*   Datos inconsistentes

### 3. Why is it useful to load data into a database instead of keeping multiple raw files?

Usar una base de datos es mil veces más práctico:
*   **Orden:** Tienes todo centralizado en un solo sitio, en vez de tener archivos regados por ahí.
*   **Consultas:** Con SQL puedes filtrar, sumar y cruzar datos rapidísimo. Intentar hacer eso abriendo archivos de texto uno por uno sería muy lento y complicado.
*   **Confianza:** Las bases de datos ayudan a que la info se mantenga estructurada y segura.

### 4. How does this ETL pipeline support future analytics or AI tasks?

Para hacer IA de verdad necesitas datos buenos, no sirve de nada tener el mejor modelo si lo alimentas con basura. Este pipeline automatiza el "trabajo sucio" de juntar y limpiar la info. Así, cuando quieras entrenar un modelo, ya tienes datos estructurados y te ahorras el tiempo que normalmente se pierde limpiando datasets manualmente.
