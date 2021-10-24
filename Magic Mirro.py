import pygame
import json
import requests

pygame.init()

#url = "https://www.metaweather.com/api/location/search/?lattlong="+cph_coordinates_formatted
url_woe = "https://www.metaweather.com/api/location/554890/" #copenhagen is 554890
api_link = requests.get(url_woe)
api_data = api_link.json()

print (api_data)
weather_description = api_data['consolidated_weather'][0]['weather_state_name']
temperatur = api_data['consolidated_weather'][0]['the_temp']
print (weather_description)
print ('det er', temperatur, 'grader C', sep=" ")
'''    
x = 50
y = 50
I = 400
J = 400
width = 40
height = 60
vel = 5
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
run = True
#create screen
display_surface = pygame.display.set_mode((700,600))
pygame.display.set_caption ("fun Mirror")
font = pygame.font.Font (None,32)
text = font.render ('what', True, blue, green)
textRect = text.get_rect()
textRect.center = (I // 2, J // 2)
while run:
    pygame.time.delay (100)
    display_surface.fill(white)
    display_surface.blit(text,textRect)

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.draw.rect (display_surface, (255,0,0), (x,y,width,height))
    pygame.display.update ()

pygame.quit
'''