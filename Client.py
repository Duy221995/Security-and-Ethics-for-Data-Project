import socket
import threading

class Client:
    def __init__(self, host, port):
        self.nickname = input("Enter your nickname: ")
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def receive(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message == 'DUY':
                    self.client_socket.send(self.nickname.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occurred. Disconnected from the server.")
                self.client_socket.close()
                break

    def write(self):
        while True:
            message = f'{self.nickname}: {input("")}'
            self.client_socket.send(message.encode('utf-8'))

client = Client('localhost', 12345)

receive_thread = threading.Thread(target=client.receive)
receive_thread.start()

write_thread = threading.Thread(target=client.write)
write_thread.start()
