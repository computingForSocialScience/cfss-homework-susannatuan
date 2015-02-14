import sys
import requests
import csv
from bs4 import BeautifulSoup

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    base = "https://api.spotify.com/v1/search?q=" #get Spotify info about artists that match keyword string
    query = name + "&type=artist"
    url = base+query
    #print url
    req = requests.get(url)
    data = req.json()
    artist = data['artists']['items'][0]['id']
    return artist

artist = "Britney Spears"
print fetchArtistId(artist)

#Checkpoint 1

def fetchArtistInfo(artist_id):
	url = "https://api.spotify.com/v1/artists/" + artist_id#get Spotify info about artists that match keyword string
	req = requests.get(url)
	data = req.json()
	info = {}
	info["followers"]=data["followers"]["total"] #followers object needs total for total number of followers
	info["genres"]=data["genres"] #string
	info["id"]=data["id"] #string
	info["name"]=data["name"] #string
	info["popularity"]=data["popularity"] #int
	return info

artist_id="26dSoYclwsYLMAKD3tpOr4"
print fetchArtistInfo(artist_id)

#Checkpoint 2