import sys
import requests
import csv
import pandas as pandas
import networkx as networkx
import numpy
from io import open
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *

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
#getting list of artists' ids

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
#getting diictionary of artists' info

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url_base = "https://api.spotify.com/v1/artists/" + artist_id
    url_album = "/albums?album_type=album"
    url_market = "&market=US"
    url = url_base + url_album + url_market
    req = requests.get(url)
    data = req.json()
    album = data['items'][0]['id']
    return album
#getting list of album ids given the artist's id

def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    url_base = "https://api.spotify.com/v1/albums/" + album_id
    url = url_base
    req = requests.get(url)
    data = req.json()
    info={}
    info["artist_id"]=data["artists"][0]["id"]
    info["album_id"]=album_id #string
    info["name"]=data["name"] #string
    info["release_date"]=data["release_date"] [:4]
    info["popularity"]=data["popularity"] #int
    return info
#getting dictionary of album info
#need track

def fetchTrack(album_id):
	req = requests.get("https://api.spotify.com/v1/albums" + album_id + "/tracks")
	data = req.json()
	track_list = data['items'][0]['name']
	return track_list

if __name__ == "__main__":
	artist_names = sys.argv[1:] #listing strings representing arguments on command-line
	def pandasToNetworkX(edgeList):
		g = nx.DiGraph()
		for sender, receiver in edgeList.to_records(index = False):
			g.add_edge(sender, receiver)
		return(g)

open('edgeList.csv')
write.open('edgeList.csv')















