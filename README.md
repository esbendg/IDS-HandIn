# IDS-HandIn 26/11/2021 - Made by Lukas S. Harder, Esben D. Galsgaard, Karsten Heiseldal, Áron Kuna & Jonatan Meyer

This is a magic mirror interface, with different visual and interactive possibilities.

List of requirements to run this program:

In order to run this program you should have installed the modules under required pip modules & imports. Then you need to get a Spotify Access Token, which you can get if you follow the steps below. Then you should open the main.py file and run the program from there. 

Regarding the Spotify Access Token: 
SpotifyCurrentSong.py needs an acces token, which you can get from this link https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types= once you have clicked the link scroll down to "OAuth Token" then press get token and then under " Required scopes for this endpoint:" tick off "user-read-currently-playing", if you are not logged in, it will ask you to login into a Spotify account, then copy and paste into the "SPOTIFY_ACCESS_TOKEN" variable on line 9, in the SpotifyCurrentSong.py file.


Pickle file named mood.pkl on path
 - to create this. Use the function "create_pkl_file()"

Regarding newsapi:
We have experienced some issues with the newsapi, if you experience issues with the program not recognizing certain newsapi commands, try to first pip uninstall both "newsapi-python" and "newsapi" and then reinstall "newsapi-python", that has fixed the issues on our end. It appears if both "newsapi-python" and "newsapi" are both installed it causes an issue. 
If the newsapi is telling it is being overloaded, try to replace it with this key: '859e740202ab4f9a8a8a187ea16101a3', i should be pasted into line 9 under 'apikey'


Required pip modules and other imports:

- tkinter
- tkcalendar
- newsapi-python
- mediapipe
- opencv-python
- pickle
- json
- requests
- datetime
- spotipy
- spotipy.client
- spotipy.oauth2
- pprint
- sys
- abc

