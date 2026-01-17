"""
Controller to handle all user inputs.
Interacts with the Model.
Alters the view .
"""

class Controller:

    View = None
    Model = None

    
    def parse_line(self, line: str):
        # returns a list of the data elements for a single row in the database
        tmp = line.strip()
        data_list = tmp.split(":")
        #print("Parsed line data: ", data_list)
        return data_list

    def print_employee(self, data):
        print("Employee ID: ", data[0])
        print("\nEmployee name:", data[1], data[2])
        print("\nDepartment:", data[3])

    def get_employee_data_by_id(self, id_num : int):
        """return employee data for a row specified by employee id"""

        #print("Searching for employee ID:", id_num)
        try:
            with open(self.Model.database_file_name, "r") as f:
                for line in f:
                    data = self.parse_line(line)
                    #print("data[0]:", data[0])
                    #print("id_num:", id_num)
                    #print(data[0] == id_num)

                    if data[0] == id_num:
                        return data
                return None
        except FileNotFoundError:
            print("data.txt could not be found")


    def is_id_num_valid(self, id_num :str):
        # check if employee id is a valid int
        #print("is_id_num_valid")
        if not id_num.isdecimal():
            print("Employee ID must be a number, please re-enter: ")
            return False


        # check if employee already exists

        data = self.get_employee_data_by_id(id_num)

        if data:
            print("Employee already exists! Please enter a different employee ID: ")
            return False
        
        return True



    def add_new_employee(self):
        """
        get user input
        check if employee already exists
        check if department exists
        open file as append use with statement
        append line of text to file in correct format
        ask user if they want to enter another employee or go back to main
        """

        print("Enter employee ID number: ")
        id_num = input()

        while not self.is_id_num_valid(id_num):
            id_num = input()







        print("\nEnter employee first name: ")
        fname = input()

        #check if fname is a string

        if not fname.isalpha():
            print("First name must be a string.")
            self.add_new_employee()

        print("\nEnter employee last name: ")
        lname = input()

        # check if lname is a vlaid string
        if not lname.isalpha():
            print("Last name must be a string.")
            self.add_new_employee()







        print("\nEnter employee department")
        department = input()

        # Check if department exists

        if department not in self.Model.valid_departments:
            print("Department: ", department, " does not exist. Use one of the following: ")
            print(self.Model.valid_departments)
            self.add_new_employee()
        else:
            print("Adding new record to database:\n")
            new_record = id_num + ":" + fname + ":" + lname + ":" + department
            try:
                with open(self.Model.database_file_name, "a") as f:
                    f.write(new_record+ '\n')
            except FileNotFoundError:
                print("database file not found")





        print("\nWould you like to add another record? (Y/N): ")
        inp = input()
        tmp_inp = inp.lower()

        if tmp_inp == "y":
            self.add_new_employee()
        elif tmp_inp == "n":
            self.View.main_menu()
        else:
            print("\nReturning to main menu.")

    def search_employee(self):
        """
        Get employee id 
        open file as read, read through every line checking for the entered id, if not present print error and return null
        if present return the data
        """

        print("Enter employee ID number: ")
        id_num = input()


        data = self.get_employee_data_by_id(id_num)


        if data:
            print("Employee found!")
            print("--------------------\n")
            self.print_employee(data)

            print("\n\n")

            print("If you want to search for another employee, enter 1.\n")
            print("If you want to return to the main menu, enter 2.\n")
            inp = input()
            if inp == "1":
                self.search_employee()
            if inp == "2":
                self.View.main_menu()
            else:
                print("/nNow thats not a number I said but I'll just take you back to the main menu.\n")
                self.View.main_menu()
        else:
            print("Employee not found. Please try again.")
            self.search_employee()
            


    def remove_employee(self):
        print("Enter ID of employee you wish to remove: ")
        id_num = input()
        employee_records = []

        if not self.get_employee_data_by_id(id_num):
            print("Employee", id_num, "not found")
            self.remove_employee()

        else:
            print("Are you sure you want to delete employee:", id_num, "(Y/N)")
            response = input()
            if response.lower() == 'y':
                print("Deleting employee record from database")
                try:
                    with open(self.Model.database_file_name, "r") as f:
                        for line in f:
                            line_data = self.parse_line(line)
                            if line_data[0] == id_num:
                                continue
                            else:
                                employee_records.append(line_data)

                    # clear the existing file content and add records
                    with open(self.Model.database_file_name, "w") as f:
                        for record in employee_records:
                            new_line = record[0] + ":" + record[1] + ":" + record[2] + ":" + record [3]
                            f.write(new_line + "\n")
                except FileNotFoundError:
                    print("Databse file not found")




            

    def display_employees(self):
        print("Display employees:\n")
        try:
            with open(self.Model.database_file_name, "r") as f:
                for line in f:
                    self.print_employee(self.parse_line(line))
                    print("\n-----")
        except FileNotFoundError:
            print("Databse file not found")

    def exit_program(self):
        print("Exiting Program\n")
        print("-----------------")
        exit()

    def handle_input(self, selection : str):
        match selection:
            case "1":
                self.add_new_employee()
            case "2":
                self.search_employee()
            case "3":
                self.remove_employee()
            case "4":
                self.display_employees() 
            case "5":
                self.exit_program()