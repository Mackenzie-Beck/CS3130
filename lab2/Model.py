"""
Model to represent the data


"""


class Model:

    valid_departments = ["Science", "Art", "Math", "English"]

    valid_usernames = ["mack"]

    database_file_name = "data.txt"


    def create_new_db(self):
        with open(self.database_file_name, "w"):
            pass

    def set_database_file_name(self, new_name:str):

        # make sure db name is a valid string

        if not new_name.isalpha():
            print("Invalid file name")
        else:
            self.database_file_name = new_name

    def get_database_file_name(self)-> str:
        return self.database_file_name

    def add_valid_department(self, department_name:str):

        # make sure department name is a valid string
        if not department_name.isalpha():
            print("Invalid department name")
        else:
            self.valid_departments.append(department_name)
            print(f"Department {department_name} added successfully.")


    def remove_valid_department(self, department_name:str):

        if department_name in self.valid_departments:
            self.valid_departments.remove(department_name)
            print(f"Department {department_name} removed successfully.")
        else:
            print(f"Department {department_name} not found in valid departments.")