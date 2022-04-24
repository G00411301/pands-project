# pands-project
Data File description

the iris.data file is a comma seperated value (csv) file containing a range of information pertaining to various plants. Attributes pertaining to each plant within the file include sepal lenght (cm), sepal width (cm), petal length (cm), petal width (cm), and class.
There are three seperate plant classes included within the file (setosa, versicolour and Virginica)
There are a total of 150 instances of each variable included within the file.


My understanding of the project

The objective of the project is to develop a program that can read in the data from the Iris.data file, analyse it, generate a summary (average, standard deviation, max, min etc.), generate a histogram of each of the attributes, generate a scater plot of each of the attributes and save the summary to the folder.

My Objectives

I would like my script to be versitile in its application, as such I would like it to be able to specify the file that the being analysed in order to allow me to repurpose the script for alternative data sets.

Notes/Comments/Observations

The following section details the thought process/approach to developing the analysis.py file, I include also commentary on the code included in the analysis.py script.

Initially I need to import the relevant modules in order to execute functions witin the script
    1. matplotlib is imported for graph generation and data visualisation,
    2. sys - taking in the file name from the teminal when calling the script,
    3. csv - imported to allow me to interrogate the csv file throughout the calculations,
    4. pandas - imported for data anlysis, used throughout the calculations

I then create a variable filename which is passed in by the user in the terminal. This approach has been taken so the user can supply the filename they wish to conduct the analysis on. I wanted to make the script resuable with a large variaty of data sources.

In order to make sure the user inputs the file name, I included a check that ensures that there are 2 arguments passed into the script.
I assume the second piece of information submitted through the terminal is the filename/path.

The user is then asked if the csv file passed to the script has headers. If not, the user must specify the number of attributes included within the csv file, the user then must enter the appropriate headings for each of the collumns in the CSV. 
The use must input the exact number of headings that they specify in the previous question (how many columns are in the file)

It took me quite some time to figure out line 58. As fileHeading was input by the user as y or n previously, the script just repeated through the steps of asking how many fields were in the dataset. I needed to reset the value from n to soemthing else, I selected "manual" but equally any value could have been used.

I then insert the captured headings into the csv file for user later in analyis.

If the user inputs y when asked if the data has headings they skip to line 68 as the above is all contained within an if function.

I then generate a  pandas dataframe from the csv file for analysis.
I then run a number of calculations on the data frame:
    1. Average,
    2. Maximum Value,
    3. Minimum Value,
    4. The Standard Deviation of the values,
    5. Correlation.

I then create a variable for both the max and the min values in the dataframe,
I open the CSV file to pull the headings from the csv file. I decided to generate a list of the headers from the CSV file as if the user input y when asked if the data had headers I would not gather them from the user.

I then use the list of the headers to control chart generation, for each item in the list I create a scatter plot for each of the attributes in the data list. This way, I can use the script for data sources that have multiple attributes as opposed to just 5 as per the iris.data file.

I repeat the above process for creating the Histogram files.

I then create a new txt file with the title Summary data file - "Original data source filename. This file is opened in write mode, this means that the data is over written each time the script is run. A benefit to the naming convention I selected is that once you change the original dataset file name, a new txt file is created.


Userguide

User steps:

    1. input analysis.py filename.csv - assuming the file is in the current directory.
    2. The script asks if the data contains headers, if "y" skip to step 5, if no;
    3. Detail the number of attributes/collumns in the csv file,
    4. Enter the name of each attribute (sepetate each header by a space)
    5. the script runs, conducts the analysis:
        Average,
        Maximum Value,
        Minimum Value,
        The Standard Deviationv of the values,
        The Correclation of the values.
    6. The script generates a number of files in the root folder including:
        a. Histogram files,
        b. Scatter plot files,
        c. Summary .txt file

References:
I used a large variety of sources for example code, instructions etc including lecture material, labs, youtube, geeksforgeeks,

- https://python-course.eu/applications-python/sys-module.php#:~:text=the%20sys%20Module-,Information%20on%20the%20Python%20Interpreter,with%20the%20import%20statement%2C%20i.e.&text=The%20sys%20module%20provides%20information,available%20constants%2C%20functions%20and%20methods.

- https://pynative.com/python-accept-list-input-from-user/

- https://stackoverflow.com/questions/29736826/insert-a-row-at-top-of-csv-file-in-python

- https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/

- https://www.adamsmith.haus/python/answers/how-to-add-a-header-to-a-csv-file-in-python#:~:text=Use%20pandas.,DataFrame.&text=read_csv(file%2C%20header%3DNone,header%20to%20the%20CSV%20file.

- https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/

- https://python-adv-web-apps.readthedocs.io/en/latest/dicts.html

- https://www.geeksforgeeks.org/reading-rows-from-a-csv-file-in-python/#:~:text=Step%201%3A%20In%20order%20to,object%20use%20open()%20method.&text=Step%202%3A%20Create%20a%20reader,object%20to%20the%20reader%20function.&text=Step%203%3A%20Use%20for%20loop,object%20to%20get%20each%20row.

- https://stackoverflow.com/questions/24962908/how-can-i-read-only-the-header-column-of-a-csv-file-using-python

- https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/loops/automate-data-tasks-with-loops/

- https://stackoverflow.com/questions/36106712/how-can-i-limit-iterations-of-a-loop-in-python

- https://www.youtube.com/watch?v=vmEHCJofslg

- https://careerkarma.com/blog/iterate-through-dictionary-python/

- https://pandas.pydata.org/docs/user_guide/basics.html

- https://www.geeksforgeeks.org/python-pandas-dataframe-max/#:~:text=max()%20function%20returns%20the,specified%20axis%20in%20the%20dataframe.

- https://www.youtube.com/watch?v=wa9-ookDLlo

- https://www.geeksforgeeks.org/iterate-over-a-list-in-python/

- https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html

- https://www.educative.io/edpresso/how-to-concatenate-strings-in-python








