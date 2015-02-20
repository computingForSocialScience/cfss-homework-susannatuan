import sys
import csv
import requests
import pandas as pd

def getRelatedArtists(artistID):
	url = "https://api.spotify.com/v1/artists/" + artistID + "/related-artists" #list of dictionaries
	req = requests.get(url)
	data = req.json() #turning it into ordered list of values
	related_artists = []
	for i in data['artists']: #for one variable in data artists return the id
		related_artists.append(i['id']) #then append the id of the next variable
	return related_artists #return this LIST of IDs
		

#artistID = '43ZHCT0cAZBISjO8DG9PnE'
#print getRelatedArtists(artistID)

#[u'0JDkhL4rjiPNEp92jAgJnS', u'2zyz0VJqrDXeFDIyrfVXSo', u'293zczrfYafIItmnmM3coR', u'1T0wRBO0CK0vK8ouUMqEl5', u'6kACVPfCOnqzgfEF5ryl0x', u'2nvKpWcP8etYTq4JrRiUiy', u'3oDbviiivRWhXwIE8hxkVV', u'03hfAxVdAWj7kxDnSG0fLD', u'1FqqOl9itIUpXr4jZPIVoT', u'5N6GwJzOcOY5kv8p0NjhYL', u'15FyiY3ChN0QRspHIQYq0W', u'4b0WsB47XCa9F83BmwQ7WX', u'7dNsHhGeGU5MV01r06O8gK', u'1eYhYunlNJlDoQhtYBvPsi', u'2GaayiIs1kcyNqRXQuzp35', u'59hLmB5DrdihCYtNeFeW1U', u'2y8Jo9CKhJvtfeKOsYzRdT', u'0wi4yTYlGtEnbGo4ltZTib', u'3IZrrNonYELubLPJmqOci2', u'3TiISqKS6ESlMQ4WFfZJw2']

def getDepthEdges(artistID, depth):
	network_list = [] #larger list of related artists
	for A in getRelatedArtists(artistID):
		add_tuple = artistID, A
		network_list.append(add_tuple)
	for variable in getRelatedArtists(artistID):
		for x in getRelatedArtists(variable):
			add_new_tuple = variable, x
			if add_new_tuple in network_list:
				pass
			else:
				network_list.append(add_new_tuple)
	return network_list

#print getDepthEdges('43ZHCT0cAZBISjO8DG9PnE', 2)

def getEdgeList(artistID, depth):
	edge_list = pd.DataFrame(getDepthEdges(artistID, depth))
	edge_list.columns = ["artistID", "next_artistID"]
	return edge_list

#print getEdgeList('43ZHCT0cAZBISjO8DG9PnE', 2)

#artistID           next_artistID
#0  43ZHCT0cAZBISjO8DG9PnE  0JDkhL4rjiPNEp92jAgJnS
#1  0JDkhL4rjiPNEp92jAgJnS  43ZHCT0cAZBISjO8DG9PnE 
#etc.

def writeEdgeList(artistID, depth, filename):
	#write DataFrame to a comma-separated values (csv) file
	#parameters are buckets for arguments

	dataframe = getEdgeList(artistID, depth)
	csv_file = dataframe.to_csv(filename, index = False)

writeEdgeList('2mAFHYBasVVtMekMUkRO9g', 1, 'edgelist.csv')