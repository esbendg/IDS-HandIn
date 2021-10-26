import json
import requests
from datetime import datetime
def weatherAPI():
    url_woe = "https://www.metaweather.com/api/location/554890/" #copenhagen is 554890
    api_link = requests.get(url_woe) #Request data from the url with woeid
    api_data = api_link.json() #convert the data to json

#get the specific data from api_data
def weather_desc():
    return api_data['consolidated_weather'][0]['weather_state_name'] 
def temperatur():
    return api_data['consolidated_weather'][0]['the_temp']
def vind_hast():
    return api_data['consolidated_weather'][0]['wind_speed']
def kilder ():
    return api_data['sources'][1]['title']

def dato_tid():
    date_time = datetime.now()
    return date_time.strftime("%d/%m/%Y | %H:%M:%S")

    print (weather_description)
    print ('Vindhastighed:',float('{:.1f}'.format(vind_hastighed*1609.344/3600)), 'm/s')
    print ('Det er', float('{:.1f}'.format(temperatur)), 'grader C udenfor', sep=" ")
    print ('Kilde:', kilder)