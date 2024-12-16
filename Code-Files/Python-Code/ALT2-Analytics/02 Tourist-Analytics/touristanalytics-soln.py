import csv
import matplotlib.pyplot as plt
import statistics # install statistics using pip install statistics to calculate median

file = open("TouristArrivalsBasic.csv","r")

csvReader = csv.reader(file)

#setup lists
country = []
v2017 = []
v2018 = []

#loop through file and add data to lists.
next(csvReader) #skips header row
for row in csvReader:
    country.append(row[1]) #Add the country names
    v2017.append(row[2])#add the figure for 2017 to the correct list
    v2018.append(row[3])#add the figure for 2018 to the correct list
    
file.close()

#save the elements in 3 lists Country name as string all others as int
country = [str(i) for i in country]
v2017 = [int(i) for i in v2017]
v2018 = [int(i) for i in v2018]

#Find the mean of each year
print("The mean for 2017 is",sum(v2017)/len(v2017))
print("The mean for 2018 is",sum(v2018)/len(v2018))
#Find the median of each year using statistics
print("The median for 2017 is", statistics.median(v2017))
print("The median for 2018 is", statistics.median(v2018))

#plot the graph
plt.plot(country,v2017)
plt.plot(country,v2018)
plt.legend(["2017","2018"])
plt.title("Number of Visitors per Country")
plt.ylabel("Number of people")
plt.xticks(rotation = 60) # rotates the text on the x label to make it legible
plt.xlabel("Countries")
plt.show()
