# Laboratory 11

## Laboratory Objectives
1. Explore and use various tools such as: GitHub, VirtualBox, Tuffix, Linux Terminal, and Atom.
1. Write a Python program using:
     1. sqlite3
1. Run and test a Python program.

## Getting Started

1. Setting Up Python Environment

     - Verify Python Installation:
     - Open your terminal (Command Prompt for Windows, Terminal for macOS/Linux).
     - Type python --version and press Enter.
     - You should see the installed Python version displayed.

2. Configuring Visual Studio Code (VS Code)

     - Install Python Extension:
     - Open VS Code.
     - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
     - Search for “Python” in the Extensions Marketplace.
     - Click “Install” on the Python extension by Microsoft.

3. Running Python in VS Code

     - Create a New Python File:
     - In VS Code, open a folder where you want to save your Python projects.
     - Click on File > New File or press Ctrl+N to create a new file.
     - Save the file with a .py extension (e.g., hello.py).

## Program Instructions
1. Write a Python program that performs as a Tuffy Titan Contacts phone list.  You are given the main.py file and are required to create the Contacts class.
1. The following is the Entity-Relationship Diagram for the data structure:

<p align="center">
  <img src="./lab11_er_diagram.png" width="425" title="Entity-Relationship Diagram">
</p>

1. The following is some sample data to help visualize the data model:

<p align="center">
  <img src="./lab11_sample_data.png" width="300" title="Sample Data">
</p>

1. Create a `Contacts` class to meet the following requirements:
     1. Create a file named `contacts.py`.
          1. Define a method named `__init__` to meet the following requirements:  
               1. Declare a class variable to store the database file and intitialize it to an empty string.
          1. Define a method named `set_database_name` to meet the following requirements:  
               1. Take a database file name as a positional parameter and assign the value to the class variable.
               2. If the file already exists, do nothing (we want to preserve any data in the file for continued use.)
               3. If the file does not exisit, connect to the `sqlite3` file and create the `contacts` table and the `phones` table using the proper SQL `CREATE TABLE` statement.  Use the same field names as those used in the Entity-Relationship diagram above.  Use integers for all the id's and text for all the other data.
          1. Define a method named `get_database_name` to meet the following requirements:
               1. Return the value of the class variable that stores the database name.
          1. Define a method named `add_contact` to meet the following requirements:
               1. Take a first name and last name as positionals parameter.
               2. Insert the first name and last name into the contacts table using the SQL `INSERT INTO` statement.
          1. Define a method named `modify_contact` to meet the following requirements:
               1. Take a contact id, first name, and last name as positionals parameter.
               2. Update the first name and last name of the cooresponding contact id in the contacts table using the SQL `UPDATE` statement.
          1. Define a method named `add_phone` to meet the following requirements:
               1. Take a contact id, phone type, and phone number as positionals parameter.
               2. Insert the contact id, phone type, phone number into the phones table using the SQL `INSERT INTO` statement.
          1. Define a method named `modify_phone` to meet the following requirements:
               1. Take a phone id, phone type, and phone number as positionals parameter.
               1. Update the phone type and phone number of the cooresponding phone id in the phones table using the SQL `UPDATE` statement.
          1. Define a method named `get_contact_phone_list` to meet the following requirements:
               1. Return an array created from a query on the database using the SQL statement `SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones ON contacts.contact_id=phones.contact_id`.
1. Run the unit testing program to ensure that your program runs as expected.
    
- For Linux and Mac users
    ```
    ./test.sh
    ```
       
- For windows users
    ```
    ./win_test.bat
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` or `./win_test.bat` repeatedly until it passes all the test.

## Submission

Submit a zip file containing all the code files on canvas 

Naming Convention: CWID_LastName.zip  

You should have the following files:
```
main.py
contacts.py
test.txt
test.sh
win_test.sh
```
    
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|5|contacts.py file submitted contains the Contacts class and meets the program requirements|
|10|unit test passes Test01_ADD_CONTACT|
|10|unit test passes Test02_MODIFY_CONTACT|
|10|unit test passes Test03_ADD_PHONE|
|10|unit test passes Test04_MODIFY_PHONE|
|5|unit test passes Test05_GET_CONTACT_PHONE_LIST|
