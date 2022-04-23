# pands-project
Data File description

the iris.data file is a comma seperated value (csv) file containing a range of information pertaining to various plants. Attributes pertaining to each plant within the file include sepal lenght (cm), sepal width (cm), petal length (cm), petal width (cm), and class.
There are three seperate plant classes included within the file (setosa, versicolour and Virginica)
There are a total of 150 instances of each variable included within the file.


My understanding of the project

The objective of the project is to develop a program that can read in the data from the Iris.data file, analyse it, generate a summary (average, standard deviation, max, min etc.), generate a histogram of each of the attributes, generate a scater plot of each of the attributes and save the summary to the folder.

My Objectives

I would like my script to be versitile in its application, as such I would like it to have the following features:
1. Be able to specify the file that the being analysed in order to allow me to repurpose the script for alternative data sets
2. 

Notes/Comments/Observations

The following section details the thought process/approach to developing the analysis.py file:

Initially, I need to import the numpy and matplotlib. This will import the functionlity required to generate the histogram and scatter plot, making the functionality available alter in the script.

I then need to access the file that contains the data we wish to analyse, I can open this file as read only as I do not wish to edit or write to the data file. I also want the user to be able to specify the filename to be imported, allowing the script to be used for other data sources in the future. 
The first problem I can see is how do I identify what the data relates to when used for other applications, it is quite simple to assign a title to each attribute in the context of the project but using it on various other files/datasets with different attributes is a challenge. My initial solution to this problem is to ensure that the attribute description is passed in by the user when runnning the script. In order to run the file, in the terminal the user will need to:
1. run the script
2. Specify the file name
