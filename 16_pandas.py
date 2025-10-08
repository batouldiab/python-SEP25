import pandas as pd

dataset = {
    'brand': ['Toyota', 'Ford', 'Kia'],
    'year': [2020, 2022, 2018]
}

dataframe = pd.DataFrame(dataset) # creates pandas dataframe from dictionary
dataframe2 = pd.DataFrame(dataset, index=['car1','car2','car3']) # creates pandas dataframe from dictionary with custom row indices

row = {
    'name': 'batoul',
    'age': 28
}
df = pd.DataFrame([row]) # must add bracket if we only have one row


# getting row by index:
print(dataframe.loc[1]) #refer to the row index 1 (using loc)
list_row_indices = [0,1]
print(dataframe.loc[list_row_indices]) #refer to the row index 0 & 1

print(dataframe2.loc['car2']) #refer to the row index car1
list_row_indices = ['car2','car3']
print(dataframe2.loc[list_row_indices]) #refer to the row index car2 & car3

print(dataframe2.iloc[0]) #refer to the row numeric index 0 (using iloc)
list_row_indices = [0,1]
print(dataframe2.iloc[list_row_indices]) #refer to the row numeric index 0 & 1
print(dataframe2.iloc[0:2]) #refer to the row numeric index 0 to 1 (2 not included)

print(dataframe2['year']) # get certain column

print(dataframe2.loc['car1', ['year']]) # get specific value using row index and column name
print(dataframe2.loc['car1':'car2', ['brand', 'year']]) # select multiple values using specific row range and columns names





# Reading from CSV
df = pd.read_csv('students_grades.csv')
print(df) # only print 1st 5 rows
print(df.to_string()) # prints all dataframe

try:
    df = pd.read_csv('students_grades.csv')
    print (df)
except FileNotFoundError:
    print("No data available")





# saving df to CSV
dataset = {
    'brand': ['Toyota', 'Ford', 'Kia'],
    'year': [2020, 2022, 2018]
}

df = pd.DataFrame(dataset)
df.to_csv('filepath.csv', index = False)






# append row to df
dataset = {
    'brand': ['Toyota', 'Ford', 'Kia'],
    'year': [2020, 2022, 2018]
}

df = pd.DataFrame(dataset)

row = {
    'brand': 'Nissan',
    'year': 2023
}
df = df._append(row, ignore_index = True)
print(df)






# append row to df in file:
row_df = {
    'brand': ['Nissan'],
    'year': [2023]
}
df = pd.DataFrame(row_df)

import os
filePath = 'filepath.csv'
fileExists = os.path.isfile(filePath) #True/False
if not fileExists: # same as: if fileExist == False
    df.to_csv(filePath, index = False)
else: # fileExist == True
    df.to_csv(filePath, mode = 'a', index = False, header= False) # appends to existing file (mode = 'a')

print('Data appended Successfully!')




# modify the dataframe
dataset = {
    'brand': ['Toyota', 'Ford', 'Kia'],
    'year': [2020, 2022, 2018]
}

df = pd.DataFrame(dataset)

new_year = 2024
name_to_modify = 'Kia'
df.loc[df['brand']==name_to_modify, 'year'] = new_year # selects rows of brand column with the corresponding condition
print(df)


# modify the dataframe in CSV
import os
filePath = 'filepath.csv'
fileExists = os.path.isfile(filePath)

if not fileExists: # same as: if fileExist == False
    print("No available data to modify!")
else:
    df = pd.read_csv(filePath)
    new_year = 2024
    name_to_modify = 'Kia'
    df.loc[df['brand']==name_to_modify, 'year'] = new_year # selects rows of brand column with the corresponding condition
    df.to_csv(filePath, index = False) # overwrites the existing file (mode = 'w' by default)
    print('Modified Successfuly!')
