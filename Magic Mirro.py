import pygame
import json
import requests
from datetime import datetime
import Weather

pygame.init()

print (Weather.vind_hast())

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

vejr=font.render(Weather.vind_hast(),False,(0,0,0))

while run:
    pygame.time.delay (100)
    display_surface.fill(white)
    display_surface.blit(vejr, (0,0,0))

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.draw.rect (display_surface, (255,0,0), (x,y,width,height))
    pygame.display.update ()

pygame.quit