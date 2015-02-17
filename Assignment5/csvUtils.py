from io import open #opens a file
from fetchArtist import fetchArtistInfo, fetchArtistId
from fetchAlbums import fetchAlbumInfo, fetchAlbumIds

def writeArtistsTable(artist_info_list):
    f = open('artists.csv', 'r+') #f is a file
    f.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY')
    for artist in artist_info_list:
        ARTIST_ID = artist['id']
        ARTIST_NAME = artist['name']
        ARTIST_FOLLOWERS = artist['followers']
        ARTIST_POPULARITY = artist['popularity']
        f.write('%s, "%s", %s, %s\n' % (ARTIST_ID, ARTIST_NAME, ARTIST_FOLLOWERS, ARTIST_POPULARITY))
        #writing to a file its parameter

artist_info_list = [{'id': '26dSoYclwsYLMAKD3tpOr4', 'name': 'Britney Spears', 'followers': 941683, 'popularity': 83}]
artist_info_list = (fetchArtistInfo(fetchArtistId("Britney Spears")))
writeArtistsTable(artist_info_list)

def writeAlbumsTable(album_info_list):
    s = open('albums.csv', 'r+')
    s.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY')
    for album in album_info_list:
        ARTIST_ID = album['artist_id']
        ALBUM_ID = album['album_id']
        ALBUM_NAME = album['name']
        ALBUM_YEAR = album['year']
        ALBUM_POPULARITY = album['popularity']
        s.write('%s, "%s", %s, %s\n' % (ARTIST_ID, ALBUM_ID, ALBUM_NAME, ALBUM_YEAR, ALBUM_POPULARITY))

album_info_list = [{'artist_id': '26dSoYclwsYLMAKD3tpOr4', 'album_id': '5rlB2HPoNHg2m1wmmh0TRv', 'name': 'Britney Jean (Deluxe Version)', 'year': '2013', 'popularity': 67}]
album_info_list = (fetchAlbumInfo(fetchAlbumId('Britney Spears')))
writeAlbumsTable(album_info_list)

#only exeute this code below this
    #writeArtistsTable("empty string") #executing the above code
    #print fetchArtistInfo(fetchArtistId("Beck"))