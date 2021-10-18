#   Ex. 2.7 template - client side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020

import chatlib
import socket
import protocol
import glob
from PIL import Image
import io
import base64


IP = '127.0.0.1'
PORT = 8820 
SAVED_PHOTO_LOCATION = '/Users/yuvalgrofman/Downloads/download.png' # The path + filename where the copy of the screenshot at the client should be saved

def handle_server_response(my_socket, cmd):
    """
    Receive the response from the server and handle it, according to the request
    For example, DIR should result in printing the contents to the screen,
    Note- special attention should be given to SEND_PHOTO as it requires and extra receive
    """
    # (8) treat all responses except SEND_PHOTO

    isValid, data = protocol.get_msg(my_socket)

    dataList = data.split(" ")

    cmdWorked = dataList[0]
    errorMsg = " ".join(dataList[1:])
    
    if (not isValid):
        print("Error occurred.")

    cmd = cmd.split(" ")[0]

    if (cmd == 'DIR'):
        print(data)

    elif (cmd == 'DELETE'):

        if (cmdWorked == 'False'):
            print("Delete failed")
            print(errorMsg)
        else: 
            print("Delete worked")

    elif (cmd == "COPY"):

        if (cmdWorked == 'False'):
            print("Copy failed")
            print(errorMsg)
        else: 
            print("Copy worked")

    elif (cmd == "EXECUTE"):

        if (cmdWorked == 'False'):
            print("Execute failed")
            print(errorMsg)
        else: 
            print("Execute worked")

    elif (cmd == "TAKE_SCREENSHOT"):

        if (cmdWorked == 'False'):
            print("Take screenshot failed")
            print(errorMsg)
        else: 
            print("Take screenshot worked")

    elif (cmd == "SEND_PHOTO"):
        print(data)
        # pilimage = Image.open(image)
        # pilimage.save(SAVED_PHOTO_LOCATION)

    else:
        print("Unknown command")







# def build_and_send_message(conn, code, data):
# 	"""
# 	Builds a new message using chatlib, wanted code and message. 
# 	Prints debug info, then sends it to the given socket.
# 	Paramaters: conn (socket object), code (str), data (str)
# 	Returns: Nothing
# 	"""

# 	msg = chatlib.build_message(code, data)

# 	conn.send(msg.encode())
# 	# print("Sent server: " + msg)

# def recv_message_and_parse(conn):
# 	"""
# 	Recieves a new message from given socket,
# 	then parses the message using chatlib.
# 	Paramaters: conn (socket object)
# 	Returns: cmd (str) and data (str) of the received message. 
# 	If error occured, will return None, None
# 	"""
# 	full_msg =  conn.recv(1024).decode()
		
# 	cmd, data = chatlib.parse_message(full_msg)
# 	return cmd, data


# def build_send_recv_parse(conn, cmd, data):

#     build_and_send_message(conn, cmd, data)
#     cmd , data = recv_message_and_parse(conn)

#     return cmd, data 

def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket .connect((IP, PORT))

    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_PHOTO\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')

    # loop until user requested to exit
    while True:
        cmd = input("Please enter command:\n")
        if protocol.check_cmd(cmd):
            packet = protocol.create_msg(cmd)
            my_socket.send(packet)

            if cmd == "SEND_PHOTO":
                isPhotoDownloaded = protocol.getImage(my_socket, SAVED_PHOTO_LOCATION)

                if (isPhotoDownloaded):
                    print("Send photo complete.")
                
                else: 
                    print("Send photo failed")


            else:
                handle_server_response(my_socket, cmd)

            if cmd == 'EXIT':
                break
        else:
            print("Not a valid command, or missing parameters\n")

    my_socket.close()

if __name__ == '__main__':
    main()