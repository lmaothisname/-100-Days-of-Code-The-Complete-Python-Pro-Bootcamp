import requests
import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
ID="ur_id"
SECRET="ur_secret"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp =spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=ID,client_secret=SECRET,redirect_uri="https://example.com/callback",scope="playlist-modify-private",show_dialog=True,cache_path=r"D:\python\Day 46\.cache",username="ur_username))   
user_id=sp.current_user()["id"]
song_uris=[]

year=date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    try:
        uri=result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. skipped.")
playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)

