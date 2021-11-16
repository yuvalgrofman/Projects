# Ex 4.4 - HTTP Server Shell# Author: Barak Gonen
# Purpose: Provide a basis for Ex. 4.4
# Note: The code is written in a simple way, without classes, log files or other utilities, for educational purpose
# Usage: Fill the missing functions and constants

# TO DO: import modules
import os
import socket

DEFAULT_URL = "webroot/index.html" 
IP = "0.0.0.0"
PORT = 80
SOCKET_TIMEOUT = 10^10


def get_file_data(filename):
    """ Get data from file """

    with open(filename, 'r') as f:
        data = f.read()

    return data

def handle_client_request(resource, client_socket):
    """ Check the required resource, generate proper HTTP response and send to client"""
    # TO DO : add code that given a resource (URL and parameters) generates the proper response

    if resource == '':
        url = DEFAULT_URL

    else:
        url = resource

    if (not os.path.isfile(url)):
        http_response = "HTTP/1.1 404 Not Found\r\n"
        client_socket.send(http_response.encode())
        
        client_socket.close()

    # TO DO: check if URL had been redirected, not available or other error code. For example:
    # if url in REDIRECTION_DICTIONARY:
        # TO DO: send 302 redirection response

    # TO DO: extract requested file tupe from URL (html, jpg etc)
    filetype = url.spilt(".")[-1]

    if filetype == 'html':
        http_header = "HTTP/1.1 200 OK\r\nCONTENT-TYPE: text\html; charset=utf-8\r\n"  

    elif filetype == 'jpg':
        http_header = "HTTP/1.1 200 OK\r\nCONTENT-TYPE: image\jpeg;\r\n"  

    elif filetype == 'js':
        http_header = "HTTP/1.1 200 OK\r\nContent-Type: text/javascript; charset=UTF-8\r\n"  
    
    elif filetype == 'css':
        http_header = "HTTP/1.1 200 OK\r\nContent-Type: text/css"  
        

    # TO DO: read the data from the file
    data = get_file_data(url)
    http_response = http_header + "Content-Length:" + len(data) + "\r\n" + data
    client_socket.send(http_response.encode())



def validate_http_request(request):
    """ Check if request is a valid HTTP request and returns TRUE / FALSE and the requested URL """

    data = request.split()

    if (data[0] == 'GET'  and 
        data[1][0] == '\\'   and 
        data[2][0:4] == 'HTTP' and 
        data[2][-4:] == '\\r\\n'):

        return True, data[1]
    
    return False, 
    
        

def handle_client(client_socket):
    """ Handles client requests: verifies client's requests are legal HTTP, calls function to handle the requests """
    print('Client connected')

    while True:

        client_request = client_socket.recv(1024)
        valid_http, resource = validate_http_request(client_request)

        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break

        else:
            print('Error: Not a valid HTTP request')
            break

    print('Closing connection')
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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