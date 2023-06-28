import socket
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.nicknames = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()

        print("Server started. Listening on", (self.host, self.port))

        while True:
            client_socket, client_address = self.server_socket.accept()
            print("New client connected:", client_address)

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        client_socket.send("DUY".encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')

        self.nicknames.append(nickname)
        self.clients.append(client_socket)

        self.broadcast(f'{nickname} joined the chat!'.encode('utf-8'))

        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                self.broadcast(message.encode('utf-8'))
            except:
                index = self.clients.index(client_socket)
                self.clients.remove(client_socket)
                client_socket.close()
                nickname = self.nicknames[index]
                self.nicknames.remove(nickname)
                self.broadcast(f'{nickname} left the chat!'.encode('utf-8'))
                break

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

server = Server('localhost', 12345)
server.start()
