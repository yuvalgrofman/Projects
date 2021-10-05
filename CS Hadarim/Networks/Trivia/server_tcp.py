import socket
from time import gmtime, strftime
import random

NAME = "Yuval's Server"

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 8820 ))
server_socket.listen()
print("Server is up and running")
(client_socket, client_address) = server_socket.accept()
print("Client connected")

while True:
    data = client_socket.recv(1024).decode()
    print("Client sent: " + data)

    if data == "Bye":
        data == " "

    if (data == "Quit"):
        client_socket.send("Bye".encode())
        print("Closing Server...")
        break
    #checking if client send cmd
    if data == "NAME":
        client_socket.send(NAME.encode())
    elif data == "TIME":
        client_socket.send(strftime("%Y-%m-%d %H:%M:%S", gmtime()).encode())
    elif data == "RAND":
        client_socket.send(str(random.randint(1,10)).encode())
    else:
        client_socket.send((data.upper() + "!!!").encode())



client_socket.close()
server_socket.close()