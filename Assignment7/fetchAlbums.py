import requests
from datetime import datetime

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
    #pass"""

artist_id ="26dSoYclwsYLMAKD3tpOr4"
album_id="5rlB2HPoNHg2m1wmmh0TRv"
print fetchAlbumIds(artist_id)
print fetchAlbumInfo(album_id)
