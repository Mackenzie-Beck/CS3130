import socket
import View
import Controller










class Client:
    SERVERIP = 'localhost'
    SERVERPORT = 20500
    ENCODER = 'utf-8'
    BUFFER = 1024
    sock = None
    view = None
    controller = None


    def __init__(self):
        # Do not open a persistent connection here.
        # Controller.send_request() will open a new socket per request.
        try:
            self.view = View.View()
            self.controller = Controller.Controller()

            self.controller.SERVERIP = self.SERVERIP
            self.controller.SERVERPORT = self.SERVERPORT
            self.controller.ENCODER = self.ENCODER
            self.controller.BUFFER = self.BUFFER

            self.view.controller = self.controller
            self.controller.view = self.view

            self.start_client()
        except OSError:
            print("OSError in bind_socket() on client.py")

    def start_client(self):
        self.controller.connect_to_server()
        self.view.username()



    

if __name__ == "__main__":
    client = Client()