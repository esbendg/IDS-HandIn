import requests
import time
import pygame
from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQCKXn1j1G9NkIaw3-0VPTKuD1xswTcH3TUDNUH_uQuAyv3zq4pNo-QRnXpl1fyt2IrKHKSXeaVauJBzsG4SWENhEo_a1mo87n34M0utgeVRTj6H7f3DiLaAYFqJ0Xui7B8RJfmulgQhnOjoq4g'


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
