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

with open("permits_hydepark.csv") as f:
	contents = f.readlines(28)
for line in contents:
	for c in line.split():
		self.type = int(c)

def zip_code_barchart():
	fig = plt.figure()
	axes=fig.add_subplot(111)
	axes.bar([0.5,1.5,2.5],[4,6,2000])
	axes.set_title("Hyde Park Zip Code Bar Chart")
	myrange = range(1,4)
	axes.set_xticks(myrange)
	axes.set_xticklabels(['Zip Codes'])
	axes.set_yticklabels("frequency")
	plt.draw()
	plt.savefig('bar.jpg')
	subprocess.call('open bar.jpg', shell=True)


for arg in sys.argv:
	if arg == "latlong":
		print get_avg_latlng("permits_hydepark.csv")
	elif arg == "hist":
		print zip_code_barchart("permits_hydepark.csv")