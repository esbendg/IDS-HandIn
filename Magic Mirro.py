import pygame
import json
import requests

pygame.init()

cph_coordinates = (55.676311,12.569350) # lat, lon

# defining a params dict for the parameters to be sent to the API 
cph_coordinates = (55.676311,12.569350) # lat, lon

# format as comma separated lattitude and longitude
cph_coordinates_formatted = str(cph_coordinates).strip('(').strip(')')
payload = {'lattlong': cph_coordinates_formatted,}
  
# sending get request and saving the response as response object 
url = "https://www.metaweather.com/api/location/search/"
r = requests.get(url = "https://www.metaweather.com/api/location/search/", params = payload) 
  
# extracting data in json format 
response = r.json() 
response


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