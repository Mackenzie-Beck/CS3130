"""
Model to represent the data


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