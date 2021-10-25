import requests
import pygame

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

def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "fe8271c563c049a0948a2071ed7ff98e"
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    article = open_bbc_page["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        print(i + 1, results[i])
    
if __name__== '__main__':
   NewsFromBBC()

while run:
    pygame.time.delay (100)
    display_surface.fill(white)

    news=font.render(NewsFromBBC(),False,(0,0,0))
    display_surface.blit(news,(100,100))

    for event in pygame.event.get () :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.display.update ()
    

pygame.quit