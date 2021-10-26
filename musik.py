import pygame
import requests
import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials

#Spotify er mega nederen

cid = '2979387358d646089e17a9f58f435b71'
secret = '38abc9ffc9a84a21b38c3928646685a3'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp= spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,10000,50):
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
