from abc import get_cache_token
import pygame
import spotipy
from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from pprint import pprint
import sys

# Client id, and secret client id from the Spotify Developer Dashboard
cid = '2979387358d646089e17a9f58f435b71'
secret = '38abc9ffc9a84a21b38c3928646685a3'

# Client and Secret Client id being validaded
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# 20 tracks from an artist being printet to the terminal
results = sp.search(q='aj tracy', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])


# Various types of infomation about a given artist
if len(sys.argv) > 1:
    kunstner = sys.argv[1]
else:
    kunstner = 'spotify:artist:1d5Y2zrhRQ6R0plv652L67'

artist = sp.artist(kunstner)
pprint(artist)

