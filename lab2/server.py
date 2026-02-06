import socket
import Model









class Server:
    SERVERIP = 'localhost'
    SERVERPORT = 20500
    ENCODER = 'utf-8'
    BUFFER = 1024
    model = None

    def __init__(self):
        self.model = Model.Model()
        self.bind_socket()
        self.start_server()

    def is_valid_username(self, username:str):
        print(username)
        return str(username in self.model.valid_usernames)

    def bind_socket(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.bind((self.SERVERIP, self.SERVERPORT))
            self.sock.listen()
            print("Server is waiting for connection...")
        except OSError:
            print("OSError in bind_socket() on server.py")

    def is_id_num_valid_number(self, id_num:str):
        print("is_id_num_valid_number")
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

    def start_server(self):
        while True:
            connection_socket, client_address = self.sock.accept()
            print(f"Connected with {client_address}")

            response = self.process_message((connection_socket.recv(self.BUFFER).decode(self.ENCODER)))
            #response = self.process_message(function, int(data))
            connection_socket.send(str(response).encode(self.ENCODER))
            connection_socket.close()

    def parse_line(self, line: str):
        # returns a list of the data elements for a single row in the database
        tmp = line.strip()
        data_list = tmp.split(":")
        #print("Parsed line data: ", data_list)
        return data_list

    def get_employee_data_by_id(self, id_num):
        """return employee data for a row specified by employee id"""
        if not self.is_id_num_valid_number(id_num):
            print("ID number is not valid")
            return
        id_str = str(id_num)
        print("Searching for employee ID:", id_str)
        try:
            with open(self.model.database_file_name, "r") as f:
                for line in f:
                    data = self.parse_line(line)
                    if data[0] == id_str:
                        print(f"Employee {id_str} found")
                        return str(data[0]) + " "+ data[1] + " "+data[2] +" "+data[3]
                print(f"Employee {id_str} not found")
                return None
        except FileNotFoundError:
            self.handle_file_not_found()
            return None

    def is_department_valid(self, department:str):
        return department in self.model.valid_departments

    def get_valid_departments(self):
        return self.model.valid_departments


    def add_record_to_db(self, new_record):
        try:
            db = self.model.database_file_name
            import os
            # open in binary append+ so we can inspect/modify the last byte reliably
            with open(db, "ab+") as f:
                f.seek(0, os.SEEK_END)
                if f.tell() != 0:
                    f.seek(-1, os.SEEK_END)
                    if f.read(1) != b'\n':
                        f.write(b'\n')
                f.write((new_record + '\n').encode(self.ENCODER))
        except FileNotFoundError:
            self.handle_file_not_found()

    def is_db_empty(self):
        with open(self.Model.database_file_name, "r") as f: 
            if not f.read(1):
                print("Database is currently empty!")
                return True
            return False

    def delete_record(self, id_num):
        if not self.is_id_num_valid_number(id_num):
            print("ID number is not valid")
        try:
            employee_records = []
            id_str = str(id_num)
            with open(self.model.database_file_name, "r") as f:
                for line in f:
                    line_data = self.parse_line(line)
                    if line_data[0] == id_str:
                        continue
                    else:
                        employee_records.append(line_data)
                    print(employee_records)
                        # clear the existing file content and add records
            with open(self.model.database_file_name, "w") as f:
                for record in employee_records:
                    new_line = record[0] + ":" + record[1] + ":" + record[2] + ":" + record [3]
                    f.write(new_line + "\n")
        except FileNotFoundError:
            return "FileNotFoundError"
        
    def get_records(self):
        try:
            records = []
            with open(self.model.database_file_name, "r") as f:
                for line in f:
                   records.append(line.strip())
                return "\n".join(records)

        except FileNotFoundError:
            self.handle_file_not_found()
            return "ERROR: Database file not found"

    def process_message(self, message):
        print("process msg, ", message )
        # message expected like: get_employee_data_by_id(1234)
        funcs = {
            "get_employee_data_by_id": self.get_employee_data_by_id,
            "is_department_valid": self.is_department_valid,
            "get_valid_departments": self.get_valid_departments,
            "add_record_to_db": self.add_record_to_db,
            "is_db_empty": self.is_db_empty,
            "delete_record": self.delete_record,
            "get_records": self.get_records,
            "is_valid_username": self.is_valid_username
        }
    
        try:
            # Restrict builtins and allow only the mapped functions
            result = eval(message, {"__builtins__": {}}, funcs)
        except Exception as e:
            result = f"ERROR: {e}"
        return result


if __name__ == "__main__":
    serv = Server()
