import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    print "input artists are ", artist_names
    # YOUR CODE HERE
    artist_list=[]
    album_list=[]
    for row in artist_names:
    	artist_id=fetchArtistId(row)
    	artist_info=fetchArtistInfo(artist_id)
    	artist_list.append(artist_info)
    	album_name=fetchAlbumIds(artist_id)
    	for new_row in album_name:
    		album_name=fetchAlbumInfo(new_row)
    		album_list.append(album_name)

    writeArtistsTable(artist_list)
    writeAlbumsTable(album_list)
    plotBarChart()
    

