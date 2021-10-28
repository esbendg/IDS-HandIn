import pygame
import requests
import json
from datetime import datetime

pygame.init()

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

display_surface = pygame.display.set_mode((700,600))
pygame.display.set_caption ("fun Mirror")
font = pygame.font.Font (None,32)

def getTime():
    now = datetime.now()
    current_time = now.strftime("%H,%M,%S")
    return current_time
#print (getTime())

def getDate():
    now = datetime.now()
    current_time = now.strftime("%D")
    return current_time


while run:
    pygame.time.delay (100)
    display_surface.fill(white)

    time=font.render(getTime(),False,(0,0,0))
    display_surface.blit(time,(20,20))
    date = font.render(getDate(),False,(0,0,0))
    display_surface.blit(date, (20,50))

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.display.update ()
    

pygame.quit
