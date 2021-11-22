import pygame
import calendar
import datetime

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

year = 2021
month = 10

display_surface = pygame.display.set_mode((700,600))
font = pygame.font.Font('freesansbold.ttf', 32)


text = font.render(calendar.month(2021,10, 5,10), False, green, blue)



pygame.display.set_caption('Calendar')

while run:
    pygame.time.delay (100)
    display_surface.fill(white)
    display_surface.blit(text,(20,20))
    
    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.display.update ()

pygame.quit