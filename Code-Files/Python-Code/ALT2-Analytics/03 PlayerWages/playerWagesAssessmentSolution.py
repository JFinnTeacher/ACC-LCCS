import csv
import re
import statistics
import matplotlib.pyplot as plt

#open the file to read
file = open("playerWages.csv","r")

csvReader = csv.reader(file)

#setup lists
age = []
club = []
value = []
wage = []

#loop through file and add data to lists.
next(csvReader) #skips header row

for row in csvReader:
    
    age.append(row[1])   #add the second age to the age list
    club.append(row[3])  #add the club to the club list
    
    v = row[4]   #select the value
    v = v[1:-1]  #take only the second character to the second last character of the value
    value.append(v) #store it in the value list
    
    w = row[5]   #select the wage
    w = re.sub("€","",w)   #remove the euro sign from the wage 
    w = re.sub("K","",w)   #remove the K from the wage
    wage.append(w)         #store it in the wage list
        
file.close()

#print the lists
print(age)
print(club)
print(value)
print(wage)

#save the elements in lists as int or float
age = [int(i) for i in age]
value= [float(i) for i in value]
wage = [float(i) for i in wage]

#calculate mean
meanAge = sum(age)/len(age)
print("The mean age of the players is", meanAge)

print("The median age of the players is", statistics.median(age))
print("The mode of the clubs is",statistics.mode(club))

#plot the graph
plt.plot(value)
plt.plot(wage)
plt.legend(["Value (M)","Wages (K)"])
plt.title("Player Value and Wages")
plt.ylabel("Amount")
plt.show()
