"""
Controller to handle all user inputs.
Interacts with the Model.
Alters the view .
"""

class Controller:

    view = None
    sock = None
    # put all of these on the controller for now, just assign them to the same as client in client.bind_cosket()
    # not the best but works for now
    SERVERIP = None
    SERVERPORT = None
    ENCODER = None
    BUFFER = None



    def create_new_db(self):
        self.Model.create_new_db()

    def is_db_empty(self):
        msg = "is_db_empty"
        return self.send_request(msg)

    def handle_file_not_found(self):
        print("Database not found, would you like to create one? (Y/N)")
        sel = input()
        if sel.lower() == "y":
            self.create_new_db()
            self.view.main_menu()
        if sel.lower() == "n":
            print("No database provided, exiting program")



    def print_employee(self, data):
        print("Employee ID: ", data[0])
        print("\nEmployee name:", data[1], data[2])
        print("\nDepartment:", data[3])

    def get_employee_data_by_id(self, id_num: int):
        msg = f"get_employee_data_by_id({int(id_num)})"
        return self.send_request(msg)



    def is_id_num_valid_number(self, id_num:str):
                # check if employee id is a valid int
        #print("is_id_num_valid")
        try:
            int(id_num)
        except ValueError:
            print("Employee ID must be a number, please re-enter: ")
            return False
        if int(id_num) < 0:
            print("Employee Id must be a positive integer, please re-enter: ")
            return False
        if len(id_num) != 4:
            print("Employee ID must be 4 digits long, please re-enter: ")
            return False
        return True

    def is_id_num_valid(self, id_num :str):
        # check if employee id is a valid int
        #print("is_id_num_valid")
        if not self.is_id_num_valid_number(id_num):
            return False

        # check if employee already exists

        data = self.get_employee_data_by_id(id_num)
        if data != "None":
            print("Employee already exists! Please enter a different employee ID: ")
            return False
        
        return True


    def get_valid_departments(self):
        msg = "get_valid_departments()"
        return self.send_request(msg)

    def is_department_valid(self, department: str):
        msg = f'is_department_valid("{department}")'
        return self.send_request(msg)


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
        if self.is_department_valid(department) == "False":
            print("Department: ", department, " does not exist. Use one of the following: ")
            print(self.get_valid_departments())
            self.add_new_employee()
        else:
            print("Adding new record to database:\n")
            new_record = id_num + ":" + fname + ":" + lname + ":" + department
            
            # quote the record and use send_request (opens a new socket per request)
            msg = f'add_record_to_db("{new_record}")'
            self.send_request(msg)

        print("\nWould you like to add another record? (Y/N): ")
        inp = input()
        tmp_inp = inp.lower()

        if tmp_inp == "y":
            self.add_new_employee()
        elif tmp_inp == "n":
            self.view.main_menu()
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
        while not self.is_id_num_valid_number(id_num):
            id_num = input()

        data = self.get_employee_data_by_id(id_num)
        data = data.split()

        
        if self.is_db_empty() == "True":
            self.view.main_menu()
        if data[0] == None:
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
                self.view.main_menu()
            else:
                print("/Now thats not a number like I said but I'll just take you back to the main menu.\n")
                self.view.main_menu()
        else:
            print("Employee not found. Please try again.")
            self.search_employee()
            


    def remove_employee(self):
        print("Enter ID of employee you wish to remove: ")
        id_num = input()
        


        while not self.is_id_num_valid_number(id_num):
            id_num = input()


        if self.is_db_empty() == "True":
            self.view.main_menu()




        if self.get_employee_data_by_id(id_num) == "None":
            print("Employee", id_num, "not found")
            self.remove_employee()


        else:
            print("Are you sure you want to delete employee:", id_num, "(Y/N)")
            response = input()
            if response.lower() == 'y':
                print("Deleting employee record from database")
                msg = f"delete_record({int(id_num)})"
                return self.send_request(msg)
        self.view.main_menu()





            

    def display_employees(self):
        print("Display employees:\n")
        try:
            with open(self.Model.database_file_name, "r") as f:
                self.is_db_empty()
                for line in f:
                    self.print_employee(self.parse_line(line))
                    print("\n-----")

                self.view.main_menu()
        except FileNotFoundError:
            self.handle_file_not_found()

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
                self.display_employees() # todo
            case "5":
                self.exit_program()

    def send_request(self, msg: str) -> str:
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.SERVERIP, self.SERVERPORT))
            s.send(msg.encode(self.ENCODER))
            return s.recv(self.BUFFER).decode(self.ENCODER)