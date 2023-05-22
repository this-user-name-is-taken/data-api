'''info'''

import sys
import urllib.parse
import requests

BASE_URI = "https://weather.lewagon.com"


def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    url = f"{BASE_URI}/geo/1.0/direct?q={urllib.parse.quote(query)}"
    response = requests.get(url).json()

    if not response:
        print("Sorry, no cities found for that query.")
        return None
    elif len(response) == 1:
        return response[0]
    else:
        print("Multiple cities found. Choose one:")
        for i, city in enumerate(response):
            print(f"{i+1}. {city['name']}, {city['country']}")
        while True:
            choice = input("> ")
            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(response):
                print("Invalid choice. Please enter a number between 1 and", len(response))
            else:
                return response[int(choice)-1]
print(response)

def weather_forecast(lat, lon):
    '''Return a 5-day weather forecast for the city, given its latitude and longitude.'''
    url = f"{BASE_URI}/data/2.5/forecast?lat={lat}&lon={lon}"
    response = requests.get(url).json()
    return response['forecast']

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)

    if city:
            print(f"Weather forecast for {city['name']}, {city['country']}:")

            forecast = weather_forecast(city['lat'], city['lon'])

            for day in forecast:
                date = datetime.datetime.fromisoformat(day['dt_txt']).strftime('%A %d %B %Y')
                print(f"{date}: {day['weather']}")
                break

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
