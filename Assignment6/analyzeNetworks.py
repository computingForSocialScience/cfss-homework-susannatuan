import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def readEdgeList(filename):
	edgeList = pd.read_csv(filename)
	#pd.read_csv takes a string (URL) and returns a DataFrame
	dataFrame = pd.DataFrame(edgeList)
	print dataFrame
	if len(dataFrame.columns) > 2:
		print "Error"
	else:
		dataFrame=dataFrame[dataFrame.columns[0:2]]
	return dataFrame

#filename = 'edgeList.csv'
#readEdgeList(filename)
#turning the csv file into a DataFrame

def degree(edgeList, in_or_out):
	#series.value_counts()  takes a parameter and returns object of counts of values
	# DataFrame + string --> in degree or out degree for all nodes on list
	dataFrame = readEdgeList(edgeList)
	if in_or_out == "in":
		degree = dataFrame['artistID'].value_counts()
	if in_or_out == "out":
		degree = dataFrame['next_artistID'].value_counts()
	return degree

#print degree('edgeList.csv', 'in')

def combineEdgelists(edgeList1, edgeList2):
	#combining dataframes
	#dataframe1 = edgeList1
	#dataframe2 = edgeList2
	concatenated = pd.concat([edgeList1], [edgeList2])
	return concatenated.drop_duplicates()
#edgeList1 = readEdgeList('edgeList.csv')
#edgeList2 = readEdgeList('edgeList.csv')
#print combineEdgelists(edgeList1, edgeList2)

def pandasToNetworkX(edgeList):
	g = nx.DiGraph()
	for sender, receiver in edgeList.to_records(index = False):
		g.add_edge(sender, receiver)
	return(g)
	nx.draw(g, with_labels=False)
	plt.show()


#edgeList = readEdgeList('edgeList.csv')
#pandasToNetworkX(edgeList)

#not showing a graph?!?!

def randomCentralNode(inputDiGraph):
	#takes graph --> single node from that network
	nodes_dict = nx.eigenvector_centrality(pandasToNetworkX(edgeList))
	#nx.eigenvector_centrality() takes graph as parameter and returns nodes in a dict.
	#print nx.eigenvector_centrality(pandasToNetworkX(edgeList))
	normal_dict = sum(nodes_dict.values())
	#probabilities do not sum to 1?!?
	random_node = np.random.choice(nodes_dict.keys(), p = nodes_dict.values())
	return random_node

edgeList = readEdgeList('edgeList.csv')
print randomCentralNode(pandasToNetworkX(edgeList))






