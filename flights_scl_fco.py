import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_flight_data():
    # Configurar opciones de Chrome
    options = Options()
    options.add_argument('--headless') # Modo sin cabeza
    options.add_argument('--disable-gpu') # Desactivar la aceleración por hardware
    options.add_argument('--start-maximized') # Maximizar ventana
    options.add_argument('--no-sandbox') # Evitar problemas de sandbox
    options.add_argument('--disable-dev-shm-usage') # Desactivar el uso de memoria compartida
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--ignore-certificate-errors')

    # Configurar servicio y driver de Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Realizar solicitud HTTP
    url = 'https://www.kiwi.com/cl/search/results/santiago-de-chile/roma-italia'
    driver.get(url)

    # Esperar a que cargue la página y cerrar el mensaje de cookies
    time.sleep(5) # Esperar 5 segundos a que cargue la página
    driver.find_element_by_id('cookie-notif-button').click()

    # Obtener los elementos de vuelo
    flight_elements = driver.find_elements_by_xpath('//div[@class="result" and not(contains(@style,"display:none;"))]')

    # Crear una lista para almacenar los datos de vuelo
    flight_data = []

    for flight_element in flight_elements:
        # Extraer información de vuelo y precio
        flight_info = {}

        # Extraer datos del vuelo de salida
        departure_airport_element = flight_element.find_element_by_xpath('.//div[@class="airport"]')
        flight_info['departure_airport'] = departure_airport_element.text.strip()

        departure_time_element = flight_element.find_element_by_xpath('.//div[@class="time"]')
        flight_info['departure_time'] = departure_time_element.text.strip()

        departure_date_element = flight_element.find_element_by_xpath('.//div[@class="date"]')
        flight_info['departure_date'] = departure_date_element.text.strip()

        departure_city_element = flight_element.find_element_by_xpath('.//div[@class="city"]')
        flight_info['departure_city'] = departure_city_element.text.strip()

        # Extraer datos del vuelo de llegada
        arrival_airport_element = flight_element.find_element_by_xpath('.//div[@class="destination-airport"]')
        flight_info['arrival_airport'] = arrival_airport_element.text.strip()

        arrival_time_element = flight_element.find_element_by_xpath('.//div[@class="destination-time"]')
        flight_info['arrival_time'] = arrival_time_element.text.strip()

        arrival_date_element = flight_element.find_element_by_xpath('.//div[@class="destination-date"]')
        flight_info['arrival_date'] = arrival_date_element.text.strip()

        arrival_city_element = flight_element.find_element_by_xpath('.//div[@class="destination-city"]')
        flight_info['arrival_city'] = arrival_city_element.text.strip()

        # Extraer precio
        price_element = flight_element.find_element_by_xpath('.//div[@class="price-text"]/span')
        flight_info['price'] = price_element.text.strip()

        # Agregar los datos de vuelo a la lista
        flight_data.append(flight_info)

    # Cerrar el driver de Chrome
    driver.quit()

    # Imprimir la lista de datos de vuelo
    print(flight_data)

    # Devolver la lista de datos de vuelo
    return flight_data


def save_flight_data_to_csv(data, filename):
    # Crear un DataFrame de pandas a partir de los datos de vuelo
    df = pd.DataFrame(data)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv(filename, index=False)


# Obtener los datos de vuelo
flight_data = get_flight_data()

# Guardar los datos de vuelo en un archivo CSV
save_flight_data_to_csv(flight_data, 'flight_data.csv')