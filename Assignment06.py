# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions and classes & organized by
#       Separation of Concerns patterns
# Change Log: (Who, When, What)
#   BChristopherson, 5/26/2025,Created Script
#   BChristopherson, 5/26/2025,Updated Script and added additional comments
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = ''  # Hold the choice made by the user.
students: list = []  # a table of student data

### Separation of Concern Pattern ###
# PROCESSING --------------------------------------

# Define the Classes
#-------------------
# A single class is being used for data processing
class FileProcessor:
    """
    A collection of functions related to data processing

    ChangeLog: (Who, When, What)
    BChristopherson, 5-26-2025, Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads student data from the Enrollments.json file
        Change Log: (Who, When, What)
        BChristopherson, 5-26-25, Created function
        :param file_name:
        :param student_data:
        :return: student_data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running"
                                     " this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file and not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes student data to the Enrollments.json file
        Change Log: (Who, When, What)
        BChristopherson, 5-26-25, Created function
        :param file_name of file to be written to
        :param student_data, table containing student enrollments
        :return: student_data, updated with the data that was written
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check if the file is a"
                                     " valid JSON format file", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.closed
        return student_data

### Separation of Concern Pattern ###
# PRESENTATION  -----------------------------

# Define the Classes
#-------------------
# A single class is being used for presenting and handling data
class IO:
    """
    A collection of functions related to user inputs, and outputs to user

    ChangeLog: (Who, When, What)
    BChristopherson, 5-26-2025, Created Class
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user
        Change Log: (Who, When, What)
        BChristopherson, 5-26-25, Created function

        :param message:
        :param error: Exception error
        :return: No return data
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --", error)
            print(error, error.__doc__, type(error), sep="\n")


    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu to the user
        Change Log: (Who, When, What)
        BChristopherson, 5-26-25, Created function
        
        :return: None 
        """
        print()
        print(menu)


    @staticmethod
    def input_menu_choice():
        """ This function accepts the user's menu choice as an input
        Change Log: (Who, When, What)
        BChristopherson, 5-26-25, Created function
        :return: returns the user's choice, as a string  
        """
        choice = "0"
        try:
            choice = input("Enter the number for your choice: 1, 2, 3, or 4: \n")
            if choice not in ("1","2","3","4"):
                raise Exception("Please choose 1, 2, 3 or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice


    @staticmethod
    def output_student_courses(student_data: list):
        """ This function outputs the student enrollment information
            Change Log: (Who, When, What)
            BChristopherson, 5-26-25, Created function
            
            :param: student_data, table of student enrollments
            ### NEED TO FILL THIS IN ###
            :return: 
            """
        print("\nThe current registrations are (in comma-separated format): ")
        print("-" *50)
        for student in students:  ###?? - should this be for student in student_data???
            print(f"{student['FirstName']},{student['LastName']},{student['CourseName']}")
            #string_row = f"["FirstName"],student[0],student[1],student[2]))
            #print(student["FirstName"],student["LastName"],student["CourseName"])
        print("-" *50)


    @staticmethod
    def input_student_data(student_data: list):
        """ This function accepts the new student enrollment information, as input
            Change Log: (Who, When, What)
            BChristopherson, 5-26-25, Created function

            ### NEED TO FILL THIS IN ###
            :return: student_data
            """
        try: # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("What is the course name? ")
            if not course_name:
                raise ValueError('Response cannot be empty')
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            # Add new student to the students table
            students.append(student_data)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e: ### compare line below with Starter file
            IO.output_error_messages("Error: There was a problem with your entered data.")

# When the program starts, read the file data into a list of lists (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
  
    menu_choice = IO.input_menu_choice()

    # Input new student
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        # Process the data to create and display a custom message
        print()
        print("-" *50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in:{student["CourseName"]}')
        print("-" * 50)
        continue

    # Display current data
    elif menu_choice == "2": # This will not work if it is an integer!
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":  # This will not work if it is an integer!
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        print("\nThe data was written to the file!")
        IO.output_student_courses(student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":  # This will not work if it is an integer!
        break  # out of the loop
    else:
        print("Thank you!")
        # input_menu_choice function already gives message to user \
        # if user enters values other than 1,2,3 or 4

print("Program Ended")
