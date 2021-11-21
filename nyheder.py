import requests
import pygame
from newsapi import NewsApiClient

"""
pygame.init()

x = 250
y = 100
I = 400
J = 400
width = 40
height = 60
vel = 5
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
run = True

display_surface = pygame.display.set_mode((1000,800))
pygame.display.set_caption ("news")
font = pygame.font.SysFont ('Helvetica',32)"""

def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "fe8271c563c049a0948a2071ed7ff98e"
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    print (open_bbc_page)
    article = open_bbc_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    #for i in range(len(results)):
    #    i + 1, results[i]
    return results


if __name__ == '__main__':
    NEWS_DATA = NewsFromBBC()

"""
news=font.render(NEWS_DATA[0],False,(0,0,0))
tick = 6000
news_nr = 0

while run:
    bbc = font.render("BBC News:", False, (0,0,0))
    display_surface.fill(white)
    display_surface.blit(bbc,(100,y*7.5))
    display_surface.blit(news,(x,y*7.5))

    if (pygame.time.get_ticks() >= tick):
        tick = tick + 6000
        news_nr = news_nr + 1
        news=font.render(NEWS_DATA[news_nr],False,(0,0,0))
        if(news_nr == 9):
            news_nr = 0

    if(pygame.time.get_ticks() > 1800000):
        NEWS_DATA = NewsFromBBC()

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.display.update ()
    

pygame.quit"""
