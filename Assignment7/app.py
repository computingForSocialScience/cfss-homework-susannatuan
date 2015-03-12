from flask import Flask, render_template, request, redirect, url_for
import pymysql
from io import open
from fetchArtist import *
from fetchAlbums import *
from fetchTrackNames import *
from artistNetworks import *
from analyzeNetworks import *
import random
import pandas as pd
import numpy as np
import networkx as nx

dbname="playlists"
host="localhost"
user="root"
passwd=""
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

app = Flask(__name__)

# Step 1: create two tables if they don't already exist
cur = db.cursor() #cursor objects allow to interact with database
playlist_table = """CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT, rootArtist VARCHAR(198));"""
songs_table = """CREATE TABLE IF NOT EXISTS songs (playlistId INTEGER, songOrder INTEGER, artistName VARCHAR(198), albumName VARCHAR(198), trackName VARCHAR(198));"""
cur.execute(playlist_table)
cur.execute(songs_table)
# primary key how is it stored in representation (auto increment increments by 1 everytime)

def createNewPlaylist(artist_name):
# input: artist's name (string)
# ouput: 30-song playlist (MySQL)

# --> Playlists table
# Step: Find one artist
	artist_id = fetchArtistId(artist_name)

# Step: Add to playlists table
	if artist_id == None: #artist's id is auto-incremented
		return
	else:
		fill_playlist_table = """INSERT INTO playlists (rootArtist) VALUES (%s);"""
		cur.execute(fill_playlist_table, artist_name)

# --> Songs table
# Step: Find related artists
	related_artists = getDepthEdges(artist_id, 2)
	# Returns a list

	# Step: Create playlist list to hold all information
	playlist_id = cur.lastrowid

	songOrder = 1
	playlist = []

	artist_list = []
	album_list = []
	track_list = []
	for variable in range(30):
		# Step: Pick a random related artist
		artist = random.choice(related_artists)
		artist_list.append(artist)
		album = fetchAlbumIds(artist_id)
		# Step: Fetch albums of this random artist
		random_artist_album = random.choice(album)
		album_list.append(random_artist_album)
		# Gives album id
		# Step: Fetch tracks in album
		track = fetchTrackNames(album)
		random_track = random.choice(track)
		track_list.append(random_track)
	# Now have three lists for artists, albums, tracks
	# Incrementing songOrder by 1 and appending
		songOrder += 1
		playlist.append(playlist_id, songOrder, artist, album, track)
	
	fill_songs_table = """INSERT INTO songs (playlist_id, songOrder, artist, album, track) VALUES (%s, %s, %s, %s, %s);"""
	cur.execute(fill_songs_table)
	db.commit()
	cur.close()

@app.route('/') #base web address
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/') #static route
def make_playlists_resp():
	# goes to database, finds playlists, creates object called playlists
	# name for playlist and id for playlist
	cur.execute('''SELECT * FROM playlists''')
	playlists = cur.fetchall()
	return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
	cur.execute('''SELECT * from songs WHERE playlistId=%s;''',playlistId)
	songs = cur.fetchall()
	return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        createNewPlaylist(artistName)
        artistName = request.form['artistName']
        return(redirect("/playlists/"))


createNewPlaylist('beyonce')

if __name__ == '__main__':
    app.debug=True
    app.run() #flask starts running