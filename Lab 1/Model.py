"""
Model to represent the data

Probably not necessary since the actual db is stored as the text file. And the controller just manipulates data.txt directly. But for now
Im storing the valid departments here

If I get around to it, putting a reference to the file here and moving all of the actual opening and closing of the file to this class would probably 
be more consistent with a MVC architecture. But it works as is.
"""


class Model:

    valid_departments = ["Science", "Art", "Math", "English"]

    database_file_name = "data.txt"


    def set_database_file_name(self, new_name:str):

        # make sure db name is a valid string

        if not new_name.isalpha():
            print("Invalid file name")
        else:
            self.database_file_name = new_name