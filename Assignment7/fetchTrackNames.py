import sys
import requests
import csv
from bs4 import BeautifulSoup
from fetchArtist import *
from fetchAlbums import *

def fetchTrackNames(album_id):
    url = 'https://api.spotify.com' + '/v1/albums/' + album_id + '/tracks'
    req = requests.get(url)
    data = req.json()
    trackNames = []
    print trackNames
    for track in data['items']:
        trackNames.append(track['name'])
    return trackNames

#print fetchTrackNames('5rlB2HPoNHg2m1wmmh0TRv')