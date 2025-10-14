import streamlit as st
import pandas as pd
import os

# --- Helper Functions ---
def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def assign_letter_grade(average):
    letter = 'F'
    if average >= 60:
        letter = 'D'
    if average >= 70:
        letter = 'C'
    if average >= 80:
        letter = 'B'
    if average >= 90:
        letter = 'A'
    return letter

def save_student_data(student_data, file_path):
    df = pd.DataFrame(student_data)
    file_exists = os.path.isfile(file_path)
    try:
        if not file_exists:
            df.to_csv(file_path, index=False)
        else:
            df.to_csv(file_path, mode='a', index=False, header=False)

        return True
    except:
        return False
    
def modify_student_data(student_name, new_grades, file_path):
    pass

def list_students(file_path):
    if os.path.isfile(file_path):
        df = pd.read_csv(file_path)
        st.subheader("Student Information:")
        st.dataframe(df)
    else:
        st.warning("No data available. The student database is empty.")
    
# --- Streamlit App ---
st.title("🎓 Student Grade Manager")
file_path = "students_grades.csv"

# Sidebar for navigation
option = st.sidebar.radio("Choose an action:", (
    "Add a new student", 
    "Modify a student's grades", 
    "List all students")
)

# Initialize session state for subject count
if 'num_subjects' not in st.session_state:
    st.session_state.num_subjects = 1

# Handle number of subjects outside form
if option == "Add a new student" or option == "Modify a student's grades":
    num_subjects = st.number_input(
        "Enter the number of subjects:", 
        min_value=1, 
        step=1,
        value=st.session_state.num_subjects,
        key="num_subjects_outside_form"
    )
    
    # Update the session state 
    if num_subjects != st.session_state.num_subjects:
        st.session_state.num_subjects = num_subjects
        # Force rerun to update the UI with new number of grade fields
        st.rerun()

# Option 1: Add new student
if option == "Add a new student":
    with st.form("add_student_form"):
        student_name = st.text_input("Enter the student's name:")
        
        # Display the currently selected number of subjects (readonly)
        st.write(f"Number of subjects: {st.session_state.num_subjects}")
        
        # Dynamically create grade inputs based on session state
        grades = []
        for i in range(st.session_state.num_subjects):
            grade = st.number_input(
                f"Enter grade for subject {i+1}:", 
                min_value=0.0, 
                step=1.0,
                key=f"add_grade_{i}"
            )
            grades.append(grade)
        
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not student_name:
            st.error("Please enter a student name.")
        elif len(grades) != st.session_state.num_subjects:
            st.error(f"Please ensure you've entered all {st.session_state.num_subjects} grades.")
        else:
            avg = calculate_average(grades)
            letter = assign_letter_grade(avg)
            student = {
                'Name': [student_name],
                'Grades': [str(grades)],
                'Average': [avg],
                'Letter Grade': [letter]
            }
            success = save_student_data(student, file_path)
            if success:
                st.success(f"Student {student_name} added successfully!")
            else:
                st.error("An error occured")

elif option == "Modify a student's grades":
    # implement the code here instead of pass
    pass


# Option 3: List students
elif option == "List all students":
    list_students(file_path)