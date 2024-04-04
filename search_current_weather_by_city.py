import os
import platform
import pip._vendor.requests 
import json


#Funciones extras para ejecutar el menú y para limpiar consola
def clean_console():
    operating_system = platform.system()
    if operating_system == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def request_option():
    global option
    option = int(input("Ingrese el número de la opción que desea: "))
    while option not in [1,2]:
        print("La opción seleccionada no es válida")
        option = int(input("Ingrese el número de la opción que desea: "))
    return option

#Función principal
def get_weather_data():
    cities = input("Ingrese la ciudad o la lista de ciudades que desea buscar (en caso de que sean más de una, separalas por una coma): ")
    cities_list =  cities.split(",") 

    for city in cities_list:
        #Geolocalización
        r = pip._vendor.requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={SECRET_KEY}")
        j = r.json()
        lat = j[0]['lat']
        lon = j[0]['lon']
        country = j[0]['country']

        #Información sobre el clima
        u =  pip._vendor.requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=es&appid={SECRET_KEY}")
        o = u.json()

        #De Kelvin a ºC: se resta 273.15    
        main = o['main']
        current = main["temp"]
        current_temp = round((current - 273.15), 1)
        max = main['temp_max']
        temp_max = round((max - 273.15), 1)
        min = main['temp_min']
        temp_min = round((min - 273.15), 1)

        weather = o['weather']
        weather_description = weather[0]['description']
        
        response = {
            "Nombre de la ciudad": city,
            "País": country,
            "Temperatura actual": current_temp,
            "Temperatura máxima": temp_max,
            "Temperatura minima": temp_min,
            "Descripción del clima": weather_description
        }

        final_response = "; ".join(f"{clave}: {valor}" for clave, valor in response.items())

        print("")
        print(final_response)
        print("")
        

#Ejecución del menú
print("MENÚ DE OPCIONES \n", "1 - Obtener datos climáticos a partir de una ciudad buscada\n", "0 - Salir")
option = request_option()

while option == 1:
    get_weather_data()
    print("Temperaturas expresadas en grados Celsius")
    print("")
    print("¿Desea buscar una nueva ciudad? (1- Si / 0- No)" ) 
    option = request_option()

input("Ingrese enter para salir...")
clean_console()
