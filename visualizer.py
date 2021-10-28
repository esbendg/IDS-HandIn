import pygame
from datoTid import getDate, getTime
from nyheder import NewsFromBBC

pygame.init()

x = 250
y = 950
I = 400
J = 400
width = 40
height = 60
vel = 5
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
run = True

display_surface = pygame.display.set_mode((1000,1000))
pygame.display.set_caption ("SmartMirror")
font = pygame.font.SysFont ('consolas',32, True)

news=font.render(NewsFromBBC(0),False,(white))

while run:
    pygame.time.delay (100)
#fylder baggrund
    display_surface.fill(black)

# tegner nyheder
    bbc=font.render("BBC NEWS", False,(white))
    display_surface.blit(bbc,(x*2,y-30))
    display_surface.blit(news,(x,y))

#tegner dato og tid
    time=font.render(getTime(),False,(white))
    display_surface.blit(time,(20,20))
    date = font.render(getDate(),False,(white))
    display_surface.blit(date, (20,50))


    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.display.update ()
    

pygame.quit