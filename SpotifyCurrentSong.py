import requests
import time
import pygame
from pprint import pprint

pygame.init()

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQAF_IlsDexOUueLNJzIhAVmF8VBtXx-0EAL9V5iCVcoFNTq-78s2NMxmBrKT5G8ckZZ6ZBm0l_tuNOULeX3Oz_ErfQaKYPhMP6eIruOJa3Yz92b1tjXn3cjHnbIb961huerCmfSnWhzmlTRaUM'


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

    return current_track_info

def music():
	current_track_id = None
	while True:
	    current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)

	    if current_track_info['id'] != current_track_id:
		    pprint(
		    	current_track_info,
		    	indent=4,
		    )
		    current_track_id = current_track_info['id']
    
	    time.sleep(1)
    

if __name__ == '__main__':
    music()

