import requests
import time
from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
# In line 9 below is where you put your Spotify Access Token, so that it works with your personal Spotify account. 
# Instruction regarding where and how to get the Spotify Access Token can be found in README.md
SPOTIFY_ACCESS_TOKEN = 'BQCyyQavROTZzOftTbTFEyfBN0JJrHbHr_9f26v4gieOYg96f6u57yM9VpBnn6isKcasWGj1-Jap_OZON5xH8HxTFM_DLXaqlVwN0qKN4TmMv-qd-dOkl_I6vy6YobnZntPD87Hc5gin5FUl1E_zyHs'


# In the function below we define how we through the Spotify Access Token access the current playing track on a Spotify account.
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
    # This is the what gets showed on the 'mirror'
    stringsong = current_track_info["track_name"] + " - " + current_track_info["artists"]

    return stringsong


