import requests
import time
from pprint import pprint


SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = 'BQC1KsW_NwysvwyUWBpd4D56vsNucUZPmSscPosU4I3AqwCGpKjVIFv3e8hyRxQQQnKMziZGu6ztnnBGUn8qyr-H1RHVdJmTIhdq3ScSjjYJItXFYQwSemSEhyQPfyBSEDuTmjVZ42PAGLQALLgqu4o'


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


