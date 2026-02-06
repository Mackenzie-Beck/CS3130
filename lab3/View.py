"""his class handles the different views, basically only a main menu for a simple project like this.
"""

class View:
    controller = None

    def select_db(self):
        print("Select a database file: ")
        file_name = input()
        self.controller.select_db()


    def main_menu(self):
        """Main entry point of the program."""


        print("--\n\n")
        print("----- Main Menu -----\n")

        print("Select one of the following:\n")
        print("    1. Add a new employee\n")
        print("    2. Search for an employee\n")
        print("    3. Remove an employee\n")
        print("    4. Display Employees\n")
        print("    5. Exit\n\n")

        print("Enter your option: ")
        selection = input()
        print("\n\n--")

        self.controller.handle_input(selection)


    def username(self):
        print("Enter user name")
        user_name = input()

        self.controller.is_valid_username(user_name)