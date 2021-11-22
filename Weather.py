import json
import requests

def vejret ():
    url_woe = "https://www.metaweather.com/api/location/554890/" #woeid for copenhagen is 554890
    api_link = requests.get(url_woe) #Request data from the url with woeid
    api_data = api_link.json() #convert the data to json

#get the specific data from api_data

    vejrtilstand = api_data['consolidated_weather'][0]['weather_state_name']
    temperatur = api_data['consolidated_weather'][0]['the_temp']
    vindhastighed = api_data['consolidated_weather'][0]['wind_speed']*1609.344/3600
    kilde = api_data['sources'][1]['title']

    Info_LIST = {
        "weather_state_name" : vejrtilstand,
        "the_temp" : temperatur,
        "wind_speed" : vindhastighed,
        "title" : kilde
    }

    CPH_Weather = f'{Info_LIST["weather_state_name"]}. \nTemperature: {Info_LIST["the_temp"]:.1f}\N{DEGREE SIGN}C. \nWindspeed {Info_LIST["wind_speed"]:.1f} m/s.\n{Info_LIST["title"]}'
    return CPH_Weather
    


