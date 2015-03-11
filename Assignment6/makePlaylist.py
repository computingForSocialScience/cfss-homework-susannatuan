#number of artist names --> writes csv
import sys
import requests
#import random
#from ..assignment5.fetchArtist import *
from artistNetworks import *
from analyzeNetworks import *
import numpy as np


# now get all of the information from assignment 5 functions
def fetchArtistId(name):
    base = "https://api.spotify.com/v1/search?q=" #get Spotify info about artists that match keyword string
    query = name + "&type=artist"
    url = base+query
    print url
    req = requests.get(url)
    data = req.json()
    artist = data['artists']['items'][0]['id']
    return artist
#getting LIST of artists' ids

#inputting artist id
def fetchAlbumIds(artist_id):
    url_base = "https://api.spotify.com/v1/artists/" + artist_id
    url_album = "/albums?album_type=album"
    url_market = "&market=US"
    url = url_base + url_album + url_market
    req = requests.get(url)
    data = req.json()
    album = data['items'][0]['id']
    return album
#getting LIST of album ids

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

#inputting album id
def fetchAlbumInfo(album_id):

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
#getting DICTIONARY of album info

def fetchTrackNames(album_id):
    url = 'https://api.spotify.com' + '/v1/albums/' + album_id + '/tracks'
    req = requests.get(url)
    data = req.json()
    trackNames = []
    print trackNames
    for track in data['items']:
        trackNames.append(track['name'])
    return trackNames
    #return track_list #generates random sample from a given 1-D array
# #getting LIST of tracks given album id (which is given by artist's id)

#print fetchTrackNames('5rlB2HPoNHg2m1wmmh0TRv')

# if __name__ == "__main__": #only run if this is the main program "python makePlaylist"
#     artist_names = sys.argv[1:] #listing strings representing arguments on command-line
#     artist_ids = [fetchArtistId(name) for name in artist_names]
#     for variable in artist_names:
#         edgeList = combineEdgeLists(edgeList, getEdgeList(variable,2))

#     g = pandasToNetworkX(edgeList)

#     artists_playlist = []
#     for i in range(30):
#         artists_playlist.append(randomcentralNode(g))
#         # #sampling 30 artists from network using randomCentralNode

#     for artist in artists_playlist:
#         artist_name = fetchArtistInfo(artist)['name']
#         album_id = random.choice(fetchAlbumIds(artist))
#         album_name = fetchAlbumInfo(album_id)['name']
#         track_name = random.choice(fetchTrackNames(album_id))
#         playlist.append((artist_name, album_name, track_name))
#     pd.DataFrame(playlist, columns=['artist_name', 'album_name', 'track_name']).to_csv('playlist.csv', index=False, encoding='utf-8')


