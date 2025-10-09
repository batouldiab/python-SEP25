import pandas as pd
import os

# Function 1:
# Function to get grades from the user
def get_grades():
    """
    write the code to return the list of grades.
    terminal must look like:
    Enter the number of subjects: 3
    Enter the grade for subject 1: 70
    Enter the grade for subject 2: 80
    Enter the grade for subject 3: 90
    """
    pass


# Function 2:
# Function to calculate the average grade
def calculate_average(grades):
    """
    write the code to return the average
    """
    pass



# Function 3:
# Function to assign a letter grade based on average score
def assign_letter_grade(average):
    """
    write the code to return the corresponding letter.
    avg more than or equal to 90 must return 'A'. 
    avg more than or equal to 80 must return 'B'. 
    avg more than or equal to 70 must return 'C'. 
    avg more than or equal to 60 must return 'D'. 
    else must return 'F'. 
    """
    pass

# list_of_grades = get_grades()
# avg = calculate_average(list_of_grades)
# letter = assign_letter_grade(avg)
# print(letter)

# Function 4:
# Function to list all students
def list_students(file_path):
    """
    write the code to print the corresponding students information from the csv file.
    if the data file exists,  it prints:
    Student Information:
    Name           Grades  Average Letter Grade
    0   s1  [4.0, 6.0, 8.0]        6            F

    if file doesn't exist, it prints:
    No data available. The student database is empty.
    """
    pass


# Function 5:
# Function to save student data to a CSV file
def save_student_data(student_data, file_path):
    """
    write the code that gets the student data dictionary as the row to append to file.
    don't forget to handle the case if file_path doesn't exist.
    """
    pass



# Function 6: 
# Function to modify a student's grade
def modify_student_data(student_name, new_grades, file_path):
    """
    write the code to get the dataframe from the file.
    if the student's data are in the file, modify the grades with the new grades. 
    """
    pass


# Function main:
# Function to start program:
def main():
    """
    write the code that will keep asking the user for entering values 
    to do work based on the entered value.
    the terminal must start typing:
            1. Add a new student
            2. Modify a student's grades
            3. List all students
            4. Exit
            Choose an option:

    If user enters 1, the terminal will print "Enter the student's name: ",
    then after the name is entered, it will ask for the grades 
    (number of grades then gets each grade). Then it adds it to the csv file.
    then it will print:
    "Student {student_name} added successfully!"
    If user enters 2, the terminal will print "Enter the student's name to modify: ",
    then after the name is entered, it will ask for number of grades and then gets each grade,
    then it modifies it in the csv. then it will then print:
    "Student {student_name}'s grades have been updated."
    If user enters 3, it will call the function that prints the list of students from csv.
    If user enters 4, it will print "Exiting..." and stops the prgram.
    any other choice will cause printing "Invalid option, please try again."
    """
    pass