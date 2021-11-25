import requests
import time
from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
# In line 9 below is where you put your Spotify Access Token, so that it works with your personal Spotify account. 
# Instruction regarding where and how to get the Spotify Access Token can be found in README.md
SPOTIFY_ACCESS_TOKEN = 'BQA5HsMGA3tShn5w7h7yGRAi6B01B0PALwEwWKQ0iIUbSFYc4dMxjWtCcl5uvSgJAFkgPXGtfzFl6GjPriaMpQBirv42EHf59SHFzpx_uYOTPMpcbFzTs5LxhKr_vkwFHo5KkxpmZzEVTjHQCzkbOMo'


# In the function below we define how we through the Spotify Access Token access the current playing track on a Spotify account.
def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()
    try:
        track_id = json_resp['item']['id']
    except KeyError:
        return "Need a valid Spotify key"
        
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


get_current_track(SPOTIFY_ACCESS_TOKEN)