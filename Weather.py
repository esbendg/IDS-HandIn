import json
from os import sep
import requests
from datetime import datetime
def vejret ():
    url_woe = "https://www.metaweather.com/api/location/554890/" #copenhagen is 554890
    api_link = requests.get(url_woe) #Request data from the url with woeid
    api_data = api_link.json() #convert the data to json

#get the specific data from api_data
    vejrtilstand = 'Vejret i dag i KBH:', api_data['consolidated_weather'][0]['weather_state_name'] #set variable to get correct info, and write "today, the weather in CPH is"
    temperatur = 'Temperatur:', float('{:.1f}'.format(api_data['consolidated_weather'][0]['the_temp'])), 'grader celcius' #set variable to get correct info, and write in celcius
    vindhastighed = 'Vindhastighed:', float('{:.1f}'.format(api_data['consolidated_weather'][0]['wind_speed']*1609.344/3600)) #set variable to get correct info, and write wind speed, and changing from mph to mps
    kilde = 'kilde', api_data['sources'][1]['title'] #set variable to get correct info, and write "source"
    list = [vejrtilstand, temperatur, vindhastighed, kilde] #set variables as a list.
    return ''.join(str(list)) #return the variables as a list.
