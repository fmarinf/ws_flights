# Scraping de datos de vuelos

Este es un script de Python que utiliza la librería Selenium para obtener datos de vuelos desde la página web de kiwi.com y guardarlos en un archivo CSV.

## Funcionamiento

Se utilizan opciones de configuración para ejecutar el script en modo "headless" y evitar problemas de sandbox. El script espera a que la página cargue y cierra el mensaje de cookies antes de extraer los datos de vuelo, que incluyen información sobre los aeropuertos, las fechas, los horarios y los precios.

## Uso

Para obtener los datos de vuelo, simplemente llama a la función get_flight_data().


```flight_data = get_flight_data()```

Luego, puedes guardar los datos en un archivo CSV utilizando la función save_flight_data_to_csv(). Por ejemplo:```


```save_flight_data_to_csv(flight_data, 'flight_data.csv')```

## Requisitos

El script requiere la instalación de las siguientes librerías:

  - pandas
  - selenium
  - webdriver_manager

Además, se debe tener instalado el navegador Google Chrome y el driver correspondiente para la versión del navegador.

## Contribución

Siéntete libre de contribuir a este proyecto y hacer mejoras en el script.
