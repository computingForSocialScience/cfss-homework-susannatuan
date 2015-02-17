import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    f_artists = open('artists.csv')
    #opens the csv file (which is like a table) of artist info
    f_albums = open('albums.csv')
    #opens the csv file (also like a table) of album info

    artists_rows = csv.reader(f_artists)
    #reads and gets all of the artists in each row of the csv file
    albums_rows = csv.reader(f_albums)
    #reads and gets all of the albums in each row of the csv file

    artists_header = artists_rows.next()
    #sequentially gets the header at the top of each artist row in the csv file
    albums_header = albums_rows.next()
    #sequentially gets the header at the top of each album row in the csv file

    artist_names = []
    #creating a list of artist names
    
    decades = range(1900,2020, 10)
    #makes a list of decades ranging from 1900 to 2020 with intervals at every 10 years
    decade_dict = {}
    #creating a dictionary of the decades
    for decade in decades:
        decade_dict[decade] = 0
    #this for loop addes decades from the range function to the dictionary
    
    for artist_row in artists_rows:
    #this is another for loop
        if not artist_row:
            continue
        #loop through the rows of artists and if there is information in the list of artists that is blank then keep going
        artist_id,name,followers, popularity = artist_row
        #setting the artist's id, name, followers and popularity to the information of artists in each row
        artist_names.append(name)
        #addes the artist's name

    for album_row  in albums_rows:
        if not album_row:
            continue
        #loop through the rows of albums and if there is information in the list of albums that is blank then keep going
        artist_id, album_id, album_name, year, popularity = album_row
        #setting the artist's album id, album name, album year and album popularity to the information of albums in each row
        for decade in decades:
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break
        #for the year (a variable) in the decades list, if the year is in between two intervals
        #(the intervals by 10 are defined above)
        #then add a count of 1
        #break from the loop

    x_values = decades
    #the x axis of the bar chart measures decades
    y_values = [decade_dict[d] for d in decades]
    #the y axis of the bar chart measures the number of albums in each decade
    return x_values, y_values, artist_names
    #print out the above values and artist names, whch will be used in the bar chart

def plotBarChart():
#defining the function, which will create a bar chart
    x_vals, y_vals, artist_names = getBarChartData()
    #setting the variables as inputs in the function
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10)
    #sets the width of each bar equal to 10
    ax.set_xlabel('decades')
    #assigns the x axis lable
    ax.set_ylabel('number of albums')
    #assigns the y axis lable
    ax.set_title('Totals for ' + ', '.join(artist_names))
    #assigns the bar chart's title
    plt.show()
    #shows the bar chart that we have created


    
