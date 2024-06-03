import requests


class Weather:
    @staticmethod
    def get_weather(city):
        base_url = f"http://wttr.in/{city}?format=j1"

        response = requests.get(base_url)

        if response.status_code == 200:
            data = response.json()

            current_condition = data['current_condition'][0]
            weather_desc = current_condition['weatherDesc'][0]['value']
            temperature = current_condition['temp_C']
            feels_like = current_condition['FeelsLikeC']
            humidity = current_condition['humidity']
            pressure = current_condition['pressure']

            print(f"\nWeather in {city.capitalize()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Feels like: {feels_like}°C")
            print(f"Humidity: {humidity}%")
            print(f"Pressure: {pressure} hPa")
            print(f"Description: {weather_desc}")
            return True
        else:
            print("City not found, please check the city name and try again.")
            return False
