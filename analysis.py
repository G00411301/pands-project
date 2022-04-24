# analysis.py
# This program will read inputs from a specified csv file and out put a summary of the information, generate a histogram and scateer gragh and save them within the folder
# Author Michael Casey


#import numpy and matplotlip - making the resources available later in the file for chart generation.
from enum import unique
import numpy as np
import matplotlib.pyplot as plt

# Import the sys module which gives the script access to arguments passed in through the terminal. This allows users to specify the file that they wish to perform the analysis on.
import sys

# Import CSV module which provides resources for working with CSV files - source https://www.youtube.com/watch?v=q5uM4VKywbA
import csv

#import pandas module for data analysis later in the script
import pandas as pd

#Filename = None as the filename will be passed in by the user. startingpoint = 0 as I want the file to be read from the beginning. It may be useful to be able to set the startpoint as a date if using time series data and you wish to specify the start date for your analysis.
filename = None
startingpoint = 0

#checking to mkae sure an argument/filename has been included in the command line
while len(sys.argv)<2:
#if there is only one name ie. filename.py the below message pops up and closes the program"
    print ("Please include file name/path in command line")
    quit()

#I assume the second argument passed into the command line is a file/path
filename = sys.argv[1]

#Finding if the first row of the CSV files is a header/attribute name
fileHeading = input("Does your data contain headers? (y/n)? ")

#I need the user to specify a couple of things including the number of attributes I want the script to analyse and the titles/descriptions of each of those attributes.
#gatering the number of attributes to be analysed
#numAttributes = int(input ('How many attributes are in the file you want to analyse?:'))

if fileHeading == "n":
    #I need the user to specify a couple of things including the number of attributes I want the script to analyse and the titles/descriptions of each of those attributes.
    #gatering the number of attributes to be analysed
    numAttributes = int(input ('How many attributes are in the file you want to analyse?:'))

    #Gathering the names of the attributes to be analysed
    inputString = input ('Enter attribute titles within your data set (seperated by a space): ')
    #Splittingthe string the user input into a list
    inputList = inputString.split()
    #Checking the number of items in the list, if the number of attributes input is less than the number of attributes specified by the user earlier, the system requests them to reenter the number of attributes
    while len(inputList)<numAttributes:
        #if a user enters too few attribute titles, they need to reenter the titles with the correct number of titles
        print ("Not all of your attributes have titles, please assign a title to each of the attributes to be analysed")
        inputString = input ('Enter attribute titles for each attribute within your data set (seperated by a space): ')
        inputList = inputString.split()
        #quit()

    while len(inputList)>numAttributes:
        #if a user enters too many attribute titles, they need to reenter the titles with the correct number of titles
        print ("You have included too many attribute titles, please only include titles for the specified number of attributes: ")
        inputString = input ('Enter attribute titles for each attribute within your data set (seperated by a space): ')
        inputList = inputString.split()
        #quit()

    #change fileheading value to manual as maintaining it as "n" keeps putting the user through a loop
    fileHeading = "manual"

    # I need to insert the header values into the csv file, to do this I load the csv into into a pandas data fram and write a header to the csv file - source https://www.adamsmith.haus/python/answers/how-to-add-a-header-to-a-csv-file-in-python#:~:text=Use%20pandas.,DataFrame.&text=read_csv(file%2C%20header%3DNone,header%20to%20the%20CSV%20file.
    # I then insert the values input by the user earlier as the top row of the csv file.
    df = pd.read_csv(filename, header=None)
    df.to_csv(filename, header=inputList, index=False)
    

#I now need to open the csv in read in order to read the data within the csv file for use in calculations

df = pd.read_csv(filename)

#get the average of the each of the attributes included in the csv file using pandas
print ("The average/mean of the values included in", filename, "are:")
print (df.mean(axis='index', numeric_only=True))

#get the maximum value of the each of the attributes included in the csv file using pandas
print ("The maximum of the values included in", filename, "are:")
print (df.max(axis='index', numeric_only=True))

#get the minimum value of the each of the attributes included in the csv file using pandas
print ("The minimum of the values included in", filename, "are:")
print (df.min(axis='index', numeric_only=True))

#get the standard deviation of the each of the attributes included in the csv file using pandas
print ("The standard deviation of the values included in", filename, "are:")
print (df.std(axis='index', numeric_only=True))

#I want to plot each of the attributes on seperate scatter graphsto do this, I call on matplotlib 
#In order to set the limits of the chart, I find the max and min of the entire data frame

maxValue = max((df.max(axis='index', numeric_only=True)))
minValue = min((df.min(axis='index', numeric_only=True)))

#Getting field names for chart from CSV file
with open (filename, 'r') as f:
    csvReader = csv.DictReader(f)
    chartTitles = list(csvReader.fieldnames)

index = 0

for i in chartTitles:
    chartname = (chartTitles[index])
    plt.ylim(minValue *0.9 ,maxValue *1.1) #setting the limits of the chart to be the 90% of the minimum value and 110% of the maximum value
    plt.title("Scatter Plot of Attribute: " + chartTitles[index]) #importing the field names in the data set as the chart title
    plt.scatter(x=df.index, y=df[chartTitles[index]]) # plotting the scatter graphs
    plt.savefig(chartTitles[index]+" Scatter.png") #creates and saves an image of the scatter plot in the local directory
    plt.close() #need to close current function as it was compounding data on the saved graphs
    index += 1 #increase the index to generate the scatter plot for the next attribute

histIndex =0
for i in chartTitles:
    plt.title("Histogram of Attribute: " + chartTitles[histIndex]) #histogram chart titles
    plt.hist(df[chartTitles[histIndex]], bins = 5) #selectring data for the histgrams and specifying the number of bins in the histogram
    plt.savefig(chartTitles[histIndex]+" Histogram.png") #creates and saves an image of the histogram in the local directory
    plt.close() #need to close current function as it was compounding data on the saved graphs
    histIndex += 1 #increase the index to generate the histogram for the next attribute

correlation = df.corr() #find the correlation between each of the value in the dataframe
print (correlation) # print correlation


