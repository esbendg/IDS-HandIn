# IDS-HandIn 28/11/2021

This is a magic mirror interface, with different visual and interactive possibilities.

List of requirements to run this program:

SpotifyCurrentSong.py needs an acces token, which you can get from this link https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= once you have clicked the link scroll down to "OAuth Token" then press get token and then under " Required scopes for this endpoint:" tick off "user-read-currently-playing", if you are not logged in, it will ask you to login into a Spotify account, then copy and paste into the "SPOTIFY_ACCESS_TOKEN" variable. 


Pickle file named mood.pkl on path

We have experienced some issues with the newsapi, if you experience issues with the program not recognizing certain newsapi commands, try to first pip uninstall both "newsapi-python" and "newsapi" and then reinstall "newsapi-python", that has fixed the issues on our end. It appears if both "newsapi-python" and "newsapi" are both installed it causes an issue. 

Required pip installs:

tkinter
tkcalendar
newsapi-python
mediapipe
opencv-python
pickle
json
requests
datetime
spotipy
spotipy.client
spotipy.oauth2
pprint
sys
abc

