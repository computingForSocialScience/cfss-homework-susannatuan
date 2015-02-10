import csv
import sys
import subprocess
import matplotlib.pyplot as plt

def readCSV(filename):
	with open(filename, "r") as f:
		rdr = csv.reader(f)
		lines = lines(rdr)
	return(lines)

def get_avg_latlng (data):
	for row in data:
		p=sum(LATITUDE)/float(len(LATITUDE))
		q=sum(LONGITUDE)/float(len(LONGITUDE))
	print(p,q)
	hppermits=readCSV("permits_hydepark.csv")
	get_avg_latlng(hppermits)

def zip_code_barchart():
	for row in rows:
		zip_code 

"""plt.draw()
plt.savefig('bar.jpg')
subprocess.call('open bar.jpg', shell=True)"""

fig = plt.figure()
axes=fig.add_subplot(1,1,1)
axes.bar([0.5,1.5,2.5],[4,6,2000])
myrange = range(1,4)
axes.set_xticks(myrange)
axes.set_xticklabels(['blah','blah2','blah3'])
plt.show()