import csv
import matplotlib.pyplot as plt

file = open("unemploymentData.csv","r")

csvReader = csv.reader(file)

#setup lists
lr2019 = []
lr2018 = []
months = ["Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]

#loop through file and add data to lists.
next(csvReader) #skips header row
for row in csvReader:
    lr2018.append(row[1])  #add the figure for 2018 to the correct list
        
    lr2019.append(row[2])  #add the figure for 2019 to the correct list
    
file.close()

#save the elements in boths lists as ints
lr2018 = [int(i) for i in lr2018]
lr2019 = [int(i) for i in lr2019]

#Find the mean of each year
print("The mean for 2018 is",sum(lr2018)/len(lr2018))
print("The mean for 2019 is",sum(lr2019)/len(lr2019))

#plot the graph
plt.plot(months,lr2018)
plt.plot(lr2019)
plt.legend(["2018","2019"])
plt.title("Live Register for Dublin County")
plt.ylabel("Number of people")
plt.show()