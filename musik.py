from abc import get_cache_token
import pygame
import requests
import spotipy
import json
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from pprint import pprint
import sys

cid = '2979387358d646089e17a9f58f435b71'
secret = '38abc9ffc9a84a21b38c3928646685a3'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp= spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Nedenstående viser forskellige sange fra en kunstner.
results = sp.search(q='aj tracy', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])


# Forskellige informationer om en kunstner
if len(sys.argv) > 1:
    urn = sys.argv[1]
else:
    urn = 'spotify:artist:1d5Y2zrhRQ6R0plv652L67'

artist = sp.artist(urn)
pprint(artist)

