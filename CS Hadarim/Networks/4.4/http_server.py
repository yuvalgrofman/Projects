# Ex 4.4 - HTTP Server Shell# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import os
import socket
import glob
from glob import glob

DEFAULT_URL = r'/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/index.html'
ROOT_URL = r'/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot'
IMG_PATH = r'/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/'

IP = "0.0.0.0"
PORT = 80
SOCKET_TIMEOUT = 100

FILE_DICTIONARY = {
    1 : r"/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/uploads/",
}

FORRBIDEN_DICTIONARY = { 
    # r"/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/imgs/abstract.jpg" : ""
    r"/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/forbiddenpage" : r"",
}

REDIRECTION_DICTIONARY = {
    r"/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/js/submit.js" : r"submitcopy.js",
    r"/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/js/box.js" : r"boxcopy.js",
    r"/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/index1" : r"redirectindex.html",
}

def recvall(sock):

    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

def get_file_data(filename):
    """ Get data from file """

    with open(filename, 'rb') as f:
        data = f.read()

    return data

def handle_client_request(resource, method, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""

    if resource == '/':
        url = DEFAULT_URL

    else:

        url = resource
        url.replace("/","\\")
        url = ROOT_URL + url


    if resource.split("?")[0] == "/image":
        name = url.split("=")[-1]
        filePath = "/Users/yuvalgrofman/Documents/Projects/CS Hadarim/Networks/4.4/webroot/uploads/" + name

        dataToSend = get_file_data(filePath) 

        client_socket.send("POST".encode())  

        http_header = "HTTP/1.1"  
        http_msg = " 200 OK\r\n"
        http_contentType = "image"

        http_header = "HTTP/1.1200 OK\r\nContent-Length: " + str(len(dataToSend)) + "\r\nContent-Type: image\r\n\r\n"  
        client_socket.send(http_header.encode() + dataToSend)

    elif method == 'POST': 
        fileData = recvall(client_socket) 
        file = open(FILE_DICTIONARY[1] + "imageOne.jpg", "wb")
        file.write(fileData)

        http_response = "HTTP/1.1 200 OK"
        client_socket.send(http_response.encode())


    elif resource.split("?")[0] == "/calculate-area":
        
        numbers = resource.split("?")[-1].split("&")

        height = int((numbers[0].split("="))[-1])
        length = int((numbers[1].split("="))[-1])

        http_header = "HTTP/1.1 200 OK Content type: text/plain\r\n\r\n" + str((height * length) / 2) 
        client_socket.send(http_header.encode())

    elif resource.split("?")[0] == "/calculate-next":

        num = int(resource.split("=")[-1]) + 1
        http_header = "HTTP/1.1 200 OK Content type: text/plain\r\n\r\n" + str(num) 
        client_socket.send(http_header.encode())

    elif (url in FORRBIDEN_DICTIONARY.keys()):
        http_response = "HTTP/1.1 403 Forbidden\r\n"
        client_socket.send(http_response.encode())

    elif url in REDIRECTION_DICTIONARY:
        http_response = "HTTP/1.1 302 Found\r\nLocation: " + REDIRECTION_DICTIONARY[url] 
        client_socket.send(http_response.encode())

    elif (not os.path.isfile(url)):
        http_response = "HTTP/1.1 404 Not Found\r\n"
        client_socket.send(http_response.encode())

    else: 

        filetype = url.split(".")[-1]
        http_header = "HTTP/1.1"  
        http_msg = "200 OK\r\n"

        if filetype == 'html':
            http_contentType = "CONTENT-TYPE: text\html; charset=utf-8"

        elif filetype == 'jpg':
            http_contentType = "Content-Type: image/jpeg"

        elif filetype == 'js':
            http_contentType = "Content-Type: text/css"
        
        elif filetype == 'css':
            http_contentType = "Content-Type: text/css"

        elif filetype == 'ico':
            http_contentType = "image/x-icon"

        elif filetype == 'gif':
            http_contentType = "image/gif"

        else: 
            http_response = "HTTP/1.1 500 Internal Server Error\r\n"
            client_socket.send(http_response.encode())
            client_socket.close()


        data = get_file_data(url)
        http_response = http_header + http_msg + "Content-Length: " + str(len(data)) + http_contentType + "\r\n\r\n" 
        client_socket.send(http_response.encode() + data)


def validate_http_request(request):
    """ Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL """

    data = request.split()

    if (data[0] == b'GET'  and data[2] == b'HTTP/1.1'): 
        return True, 'GET', data[1].decode()

    if (data[0] == b'POST' and  data[2] == b'HTTP/1.1'):
        return True, 'POST', data[1].decode()
    
    return False, None, None 

def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')

    while True:

        client_request = client_socket.recv(1024)
        valid_http, method, resource = validate_http_request(client_request)

        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, method, client_socket)
            break

        else:
            print('Error: Not a valid HTTP request')
            break

    print('Closing connection')
    client_socket.close()


def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print("Listening for connections on port {}".format(PORT))

    while True:
        client_socket, client_address = server_socket.accept()
        print('New connection received')
        client_socket.settimeout(SOCKET_TIMEOUT)

        try: 
            handle_client(client_socket)

        except TimeoutError: 
            print("TimeOut error")


if __name__ == "__main__":
    # Call the main handler function
    main()