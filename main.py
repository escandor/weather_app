import requests
import json
from api_keys import api_key

def toCelsius(kelvin):
    return round(kelvin - 273.15, 2)

def main():
    while True:
        city = input("Please enter a city: ")

        try:
            payload = {"q": city, "appid": api_key}
            r = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)
            r.raise_for_status()
            break

        except requests.exceptions.HTTPError:
            print(f'\'{city}\' does not exist.')

    data = json.loads(r.text)

    print('\n    {}, {}\n'.format(data["name"], data["sys"]["country"]))

    weather = data["weather"][0]["description"].title()
    curr_temp = toCelsius(data["main"]["temp"])
    temp_min = toCelsius(data["main"]["temp_min"])
    temp_max = toCelsius(data["main"]["temp_max"])

    print(f'    Weather: {weather}\n    Min Temp: {temp_min}\u00b0\n    Max Temp: {temp_max}\u00b0\n\n    Current Temp: {curr_temp}\u00b0\n')

if __name__ == '__main__':
    main()