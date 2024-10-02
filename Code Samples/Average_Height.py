'''
Title: Average Height Calculator
Created by: J Finn
Date: 24-Sept-2024
'''

# Ask User for 5 differet Heights in cm
height1 = int(input("What id the First Height in cm"))
height2 = int(input("What is the second height in cm"))
height3 = int(input("What is the third height in cm"))
height4 = int(input("What is the fourth height in cm"))
height5 = int(input("What is the fifth height in cm"))

# Find the Average of the 5 Heights\
averageHeight = (height1+height2+height3+height4+height5)/5

# Display the answer
print("The average height is ", averageHeight,"cm")