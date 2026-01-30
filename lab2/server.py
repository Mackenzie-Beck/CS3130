import socket
import Model









class Server:
    SERVERIP = 'localhost'
    SERVERPORT = 20500
    ENCODER = 'utf-8'
    BUFFER = 1024
    sock = None

    def start_server(self):
        while True:
            connection_socket, client_address= self.sock.accept()
            print(f"Connected with {client_address}")

            message=connection_socket.recv(self.BUFFER).decode(self.ENCODER)
            connection_socket.send(message.upper().encode(self.ENCODER))

    def bind_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.SERVERIP,self.SERVERPORT))
        self.sock.listen()
        print("Server is waiting for connection...")
        self.start_server(self)



