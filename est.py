#Import pandas, note that the as operator allows us to assign the name of pandas to anym name we can use throughout the program
import pandas as pd

#This is how you check your pandas version
#print(pd.__version__) #Uncomment

#This is how you create a data set

dataset = {"Colors": ["blue", "green", "yellow", "purple"],
           "models": ["Honda", "Bmw", "Ford", "suzuki"],
            "Seat Allocation": ["5", "5", "5", "7"]}

#The result ==

#    Colors  models Seat Allocation
# 0    blue   Honda               5
# 1   green     Bmw               5
# 2  yellow    Ford               5
# 3  purple  suzuki               7

#This is how you assign a dataset to a dataframe

df = pd.DataFrame(dataset)

#How to access the values
#first option is using the [iloc] method ie.
'''
df.iloc[0,0] #Uncomment
'''
#in this case the result would be "blue"

#What is a pandas series???
#you can directly print a dataset like this
'''
print(pd.Series(dataset)) #uncomment,    use only for analysing if your data s entered, though not accurate for checking positions
'''

#!!!!Notice that the keys of the dictionary become the labels
#I prefer using DataFrames

#Locate row
'''
print(df.loc[0]) #First Row (not column)
''' # Uncomment

#The Result ==
# Colors              blue
# models             Honda
# Seat Allocation        5
# Name: 0, dtype: object

#open a csv file, I got the sample csv from the internet
csv_path = "/home/wtc/Documents/side pojs/Pandas Configuration/Pandas-Tutorial/customers-100.csv"
ndf = pd.read_csv(csv_path)

#Print the rown default
#print(ndf) #But as you can see it prints the rows but only 10, which is the first 5 and last five 

#To fix this
#Increase the number of printable rows
pd.options.display.max_rows = 100 # It will now print the specified number of rows

'''
print(ndf)
''' #Uncomment

#Print the number of rows
''' 
print(pd.options.display.max_rows)  
''' #uncomment ___________________ #check out other data you can return after pressing the [.] after typing display

'''
Let's talk JSON!!!!
'''

#I downloaded a JSON file for referential purposes. I currently don't know what it contains, let's Find out :)

#read JSON file
json_path = "/home/wtc/Documents/side pojs/Pandas Configuration/Pandas-Tutorial/sample.json"
jdf = pd.read_json(json_path)

#Print the Contents of your JSON file

# print(jdf.to_string)

#print all the column heads
# print(jdf.head(0)) #Uncomment

#print the last five elements of the DataFrame
# print(jdf.tail()) #Uncomment '''you can customise how many'''

print(jdf.tail())

#___________________________________________CLEANING DATA___________________________________________________#

#we will now use the data.csv file
new_csv_path = "/home/wtc/Documents/side pojs/Pandas Configuration/Pandas-Tutorial/data.csv"
exmp = pd.read_csv(new_csv_path)

#we are looking for
#    - Empty Cells
#    - Data in wrong format
#    - wrong data
#    - Duplicates

#let's start with empty cells
'''
no_empty_cells = exmp.dropna()
''' #uncomment

#If you want to change the existing dataframe => df.dropna(inplace = True)

#Replace null cells
'''
replaced_exmp = exmp.fillna("Enter value in space for null", inplace=True)
''' #uncomment

#replace on specified columns
'''
spec_replaced = exmp["pulse"].fillna("enter the replacing value", inplace=True)
''' #uncomment

#replace with the mean, median, or mode

#_____MEAN_____

'''
#start by calculating the mean
mean = exmp["Duration"].mean()

#then replace with it

exmp["Duration"].fillna(mean, inplace=True)
''' #Uncomment

#median


'''
#same way :)
median = exmp["Duration"].median()

exmp["Duration"].fillna(median, inplace=True)
''' #uncomment

#Mode
'''
#same way
mode = exmp["Duration"].mode()
print

exmp["Duration"].fillna(mode, inplace=True)
''' #uncomment



