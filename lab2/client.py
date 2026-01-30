import socket
import View
import Controller










class Client:
    SERVERIP = 'localhost'
    SERVERPORT = 20500
    ENCODER = 'utf-8'
    BUFFER = 1024
    sock = None

    def bind_socket(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self.SERVERIP,self.SERVERPORT))

        self.start_client()


    def start_client(self):
        data=input("Please enter your message: ")
        self.sock.send(data.encode(self.ENCODER))

        data=.self.sock.recv(self.BUFFER).decode(self.ENCODER)
        print(data)