from flask import Flask, render_template, request, redirect, url_for
import pymysql
from io import open
import pandas as pd
import networkx as nx
import json
from create_tables import *
import matplotlib.pyplot as plt

dbname="facebook"
host="127.0.0.1"
user="root"
passwd="newpwd"
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

cur = db.cursor()

app=Flask(__name__)

@app.route('/') #base web address
def make_index_resp():
    # this function just renders index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/profile/<uid>') #static route
def make_profiles_resp():
	# goes to database, finds facebook
	cur.execute('''SELECT * FROM facebook''')
	facebook = cur.fetchall()
	return render_template('facebook.html',uid=uid)

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

if __name__ == '__main__':
	app.run()