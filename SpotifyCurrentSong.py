import requests
import time
import pygame
from pprint import pprint

"""pygame.init()

display_surface = pygame.display.set_mode((1000,500))
pygame.display.set_caption ("spotify")
font = pygame.font.SysFont ('Helvetica',32)"""

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQDBM5tzbC8SZgoiIFBsiQMM-Rt4cVIDvI_oB-40IoDEupkikF7EuCnJM7xJ-LP10mb6UIdrgRjM-9QVhhMZYivpCXh736d-JDXmBwxTtaENgu-kfR05gvaNaSvfvYtAitVEB8OSnYYeck19Jx0'


def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = [artist for artist in json_resp['item']['artists']]

    link = json_resp['item']['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
    	"id": track_id,
    	"track_name": track_name,
    	"artists": artist_names,
    	"link": link
    }
    stringsong = current_track_info["track_name"] + " - " + current_track_info["artists"]

    return stringsong

#def music():
	#current_track_id = None
	#current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
	#current_track_id = current_track_info['id']
    #return current_track_info["id"]
"""
if __name__ == '__main__':
    run = True
    while(run):
        musik = font.render(get_current_track(SPOTIFY_ACCESS_TOKEN),False,(0,0,0))
        display_surface.fill((255,255,255))
        display_surface.blit(musik,(5,50))
        pygame.display.flip()
        pygame.time.delay(1000)
        
        for event in pygame.event.get () :
            if event.type == pygame.QUIT :
                 run = False

pygame.quit"""