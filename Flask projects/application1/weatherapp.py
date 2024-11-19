from flask import render_template
import json
import urllib.request

API_KEY = '3acb4b35092a220d530dbf7b5a1cb379'

def weather(city='delhi'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        weather_data = {
            "city": data['name'],
            "country_code": data['sys']['country'],
            "temp_cell": f"{temperature_celsius:.2f} °C",
            "humidity": data['main']['humidity'],
        }
        return render_template('w2.html', data=weather_data)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('w2.html', error=error_message)