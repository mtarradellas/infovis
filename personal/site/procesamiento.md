# Procesamiento de Datos

Se tomaron los datos de Youtube Music a traves de Google Takeout, seleccionando solamente datos del historial, en formato JSON.

Al archivo original se le tuvieron que realizar transformaciones, las cuales todas fueron hechas con scripts en Python

Primero, el archivo venia incluyendo historial de reproducciones de videos de YouTube, las cuales tuvieron que ser filtradas para quedarse solamente con el historial de Youtube Music.

Una vez conseguidas las canciones, de estas se quitaron algunas que tienen fecha de reproducción anteriores a marzo, para solo quedarse con 2 meses completos (marzo y abril 2022)

3 datos se obtuvieron de este archivo: título de canción, artista, y fecha de reproducción. La fecha luego se cambió de formato a MM/DD/YYY para mayor compatibilidad en los sistemas gráficos.

Los 2 datos faltantes, género y duración de la canción, se completaron generando primero otro archivo JSON en donde se indica para cada canción única su género y duración en segundos, de donde luego el script consulta para generar el archivo principal con los 5 datos del análisis.

Por último, en lugar de generar un archivo de valores separados por coma "," se separaron los valores con punto-y-coma (;) ya que varias canciones tienen coma en su titúlo.

### Archivos extra

Además del archivo principal con los 5 datos (y el JSON de información faltante), se generaron otros 3 archivos para adaptar los datos a distintos gráficos, todos formados con scripts en Python.

[Todos estos graficos se pueden ver en el repositorio bajo la carpeta "dataset"](https://github.com/mtarradellas/infovis/tree/main/personal/dataset)

-   watch-history.json => archivo original de google takeout

-   song-data.json => archivo de información extra (género y duración)

-   song-data.csv => archivo de información extra en formato csv

-   parsed-history.csv => archivo con los 5 datos principales

-   flourishrace.csv => se utilizó para generar el gráfico Bar Chart Race en Flourish. Indica para cada fecha cuantos minutos totales se escucharon del artista hasta el momento. Usa tab (\t) como delimitador.

-   flourish-genres.csv => se utilizó para generar el gráfico Streamgraph en Flourish. Indica en cada fecha cuantos minutos se escucharon del género ese día. Los géneros se agruparon manualmente en los mas importantes: Rock, Metal, Jazz y el resto. Usa coma (,) como delimitador.

-   datawrapper-time.csv => se utilizó para generar el gráfico de linea en DataWrapper. Indica en cada fecha cuantos minutos se escucharon. Usa coma (,) como delimitador.
