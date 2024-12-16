import csv
import re
import statistics
import matplotlib.pyplot as plt

# Open the File to get data
file = open("Highest Holywood Grossing Movies.csv","r")
csvReader = csv.reader(file)

movieTitle = []
worldSales = []

#loop through file and add data to lists.
next(csvReader) #skips header row

for row in csvReader:
    movieTitle.append(row[1])
    v = row[9] #removes $ and appends to list
    v = v[1:]
    worldSales.append(v)
    
file.close()

#Parse the elements to string and Integer respectivly
movieTitle = [str(i) for i in movieTitle]
worldSales = [int(i) for i in worldSales]

#Find specific values max, min and mean
meanvalue = sum(worldSales)/len(worldSales)
print("The mean value of money earned is $",meanvalue)
maxSales = max(worldSales)
minSales = min(worldSales)
print("The Maximum amount of money made is $",maxSales)
print("The Minimum amount of money made is $",minSales)

#plot the graph
plt.bar(movieTitle, worldSales, color='blue')
plt.title("Top selling Movies worldwide")
plt.ylabel("Amount in $")
plt.xticks(rotation = 60)
plt.xlabel("Movie title")
plt.show()