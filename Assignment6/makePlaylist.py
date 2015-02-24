#number of artist names --> writes csv
import sys
import requests
import random
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *
import numpy as np

if __name__ == "__main__":
    artist_names = sys.argv[1:] #listing strings representing arguments on command-line
    print ('artists are', artist_names)

#now get all of the information from assignment 5 functions
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
    return np.random.choice.(artist)
#getting LIST of random artists' ids

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
	#return info
#getting DICTIONARY of artists' info

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
    return np.random.choice(album)
#getting LIST of random album ids given the artist's id

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
    #return info
#getting DICTIONARY of album info
#now, need tracks

def fetchTrack(album_id):
	req = requests.get("https://api.spotify.com/v1/albums" + album_id + "/tracks")
	data = req.json()
	track_list = data['items'][0]['name']
	return np.random.choice(track_list) #generates random sample from a given 1-D array
#getting LIST of random tracks given album id (which is given by artist's id)

for variable in artist_names:
    artist.append(album, track_list)
    return artist
#getting new LIST of all random artists, albums and tracks

edgeList = getEdgeList(artist_id)

#getting full network list using pandas
def pandasToNetworkX(edgeList):
    g = nx.DiGraph()
    for sender, receiver in edgeList.to_records(index = False):
        g.add_edge(sender, receiver)
    return(g)

artists_playlist = []

for artist in artists_playlist:
    artist_playlists.append(randomCentralNode(g))
#sampling 30 artists from network using randomCentralNode

f.write(artists_playlist)



