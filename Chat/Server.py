import socket
import threading

class Server:
    MAX_CONNECTIONS = 5
    connections = []
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        self.mySocket.bind(('0.0.0.0', 10000))
        self.mySocket.listen(1)

    def handler(self, client, clientAddress):
        while True:
            data = client.recv(1024)
            for client in self.connections:
                client.send(data)
            if not data:
                print(str(clientAddress[0]) + ':' + str(clientAddress[1]), "disconnected")
                self.connections.remove(client)
                client.close()
                break

    def isMaxConnectionsEstablished(self):
        return len(self.connections) >= self.MAX_CONNECTIONS

    def run(self):
        print("Server is up and running")
        while True:
            client, clientAddress = self.mySocket.accept()
            if not self.isMaxConnectionsEstablished():
                connectionThread = threading.Thread(target = self.handler, args = (client, clientAddress))
                connectionThread.daemon = True
                connectionThread.start()
                self.connections.append(client)
                print(str(clientAddress[0]) + ':' + str(clientAddress[1]), "connected")
            else:
                print("Maximum connections established")
                client.send(b"Chosen chatroom is full")
                client.close

server = Server()
server.run()  
