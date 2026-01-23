# Employee Database Management System \
A simple command-line employee database management system built with Python using the Model-View-Controller (MVC) design pattern.\

## Overview
This application allows users to manage employee records through a text-based interface. Employee data is stored in a flat-file database with colon-separated values.
Features

Add New Employee - Create new employee records with validation\
Search Employee - Look up employees by their ID number\
Remove Employee - Delete employee records with confirmation\
Display All Employees - View all employees in the database\
Input Validation - Ensures data integrity with checks for:\
- Unique employee IDs
- Valid department assignments
- Proper name formatting



## Data Structure
Employee records are stored in the following format:
ID:FirstName:LastName:Department\
Example:\
101:John:Doe:Engineering\
102:Jane:Smith:Marketing\
## Architecture
The application follows the MVC (Model-View-Controller) pattern:

Model - Manages data and business logic (database file, valid departments)
View - Handles user interface and display
Controller - Processes user input and coordinates between Model and View

## Usage
### Main Menu Options

Add a new employee
Search for an employee
Remove an employee
Display all employees
Exit program

### Adding an Employee

Enter a unique employee ID (numeric, positive, and 4 digits long)
Enter first name (alphabetic characters only)
Enter last name (alphabetic characters only)
Select a valid department from the available list

### Searching for an Employee

Enter the employee ID
View the employee's information
Option to search again or return to main menu

### Removing an Employee

Enter the employee ID to remove
Confirm deletion
Record is permanently removed from the database

## Requirements

Python 3.10+ (uses match statement)
No external dependencies required

## File Structure
project/\
├── Controller.py    # Handles user input and application logic\
├── Model.py         # Defines data structure and validation\
├── View.py          # Manages user interface\
├── main.py          # Application entry point\
└── data.txt         # Employee database file


## Error Handling
The application includes error handling for:

File not found errors
    If a file named "data.txt" is not found in the directory. The user will be prompted to create a new database. If the user creates a new databse
    a file named "data.txt" will be created in the directory to act as the new database file. If the user refuses, then the program simply terminates.
Invalid input types
Duplicate employee IDs
Non-existent departments
    The user has a selection of valid departments to choose from. They will be prompted to use a valid department from the list.
Invalid employee lookups

Notes
Employee IDs must be unique positive numeric values that are 4 digits long
Names must contain only alphabetic characters
Departments must match predefined valid departments in the Model
All changes are immediately persisted to the database file