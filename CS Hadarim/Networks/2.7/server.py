#   Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020

import socket
import protocol
import glob
import os 
import shutil
import subprocess
from sys import platform
import pyautogui
from PIL import Image
import base64



IP = '127.0.0.1'
PHOTO_PATH = '/Users/yuvalgrofman/Downloads/icons8-chrome-144.png' # The path + filename where the screenshot at the server should be saved




def dir(path : str):

    try: 
        if not os.path.isdir(path):
            return 'False [Errno 2] No such file or directory: ' + path

        files_list = glob.glob(path + "/*.*")
        return files_list

    except Exception as e: 
        return str(False) + " " + str(e)

def delete(path : str):
    try: 
        os.remove(path)
        return True

    except Exception as e: 
        return str(False) + " " + str(e)

def copy(file : str , dest : str):
    try: 

        shutil.copy(file, dest)
        return True

    except Exception as e: 
        return str(False) + " " + str(e)

def execute(path : str):
    try: 
        if not os.path.isdir(path):
            return 'False [Errno 2] No such file or directory: ' + path

        if platform == "darwin":

            subprocess.Popen(['open', path])
            return True

        elif platform == "cygwin":
            subprocess.call(path)
            return True

        else: 
            return False

    except Exception as e: 
        return str(False) + " " + str(e)

def take_screenshot():
    try: 

        image = pyautogui.screenshot() 
        image.save(PHOTO_PATH)

        return True

    except Exception as e:
        return str(False) + " " + str(e)


def send_photo(conn):

    image = open(PHOTO_PATH, "rb")

    imageToRead = image.read()

    lenData = str(len(str(imageToRead)))
    lenlenData = str(len(lenData))

    lenlenData = "0" * (2 - len(lenlenData)) + lenlenData

    conn.send(lenlenData.encode())
    conn.send(lenData.encode())

    data = imageToRead[:1024]
    imageToRead = imageToRead[1024:]
    while data:
        conn.send(data)
        data = imageToRead[:1024]
        imageToRead = imageToRead[1024:]




def check_client_request(cmd):
    """
    Break cmd to command and parameters
    Check if the command and params are good.

    For example, the filename to be copied actually exists

    Returns:
        valid: True/False
        command: The requested cmd (ex. "DIR")
        params: List of the cmd params (ex. ["c:\\cyber"])
    """

    if (not protocol.check_cmd(cmd)):
        print("Illegal input from server")
        
    try: 

        cmd, data = protocol.parse_cmd(cmd)  

        return True, cmd, data

    except: 

        return False, None, None 


def handle_client_request(conn, command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_PHOTO, only the length of the file will be sent

    Returns:
        response: the requested data

    """
    response = "unknown command"

    if (command == "DIR"):
        response = dir(params[0])

    elif (command == "COPY"):
        response = copy(params[0], params[1])

    elif (command == "EXECUTE"):
        response = execute(params[0])

    elif (command == "DELETE"):
        response = delete(params[0])

    elif (command == "TAKE_SCREENSHOT"):
        response = take_screenshot()

    elif (command == "SEND_PHOTO"):
        send_photo(conn) 

    return response

def main():

    # open socket with client
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 8820 ))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    # handle requests until user asks to exit
    while True:
        # Check if protocol is OK, e.g. length field OK
        valid_protocol, cmd = protocol.get_msg(client_socket)
        if valid_protocol:
            # Check if params are good, e.g. correct number of params, file name exists
            valid_cmd, command, params = check_client_request(cmd)
            if valid_cmd:

                # (6)

                # prepare a response using "handle_client_request"
                response = handle_client_request(client_socket, command, params)

                # add length field using "create_msg"
                msg = protocol.create_msg(str(response))

                if not command == 'SEND_FILE':
                    client_socket.send(msg)
                
                if command == 'EXIT':
                    break
            else:
                # prepare proper error to client
                response = 'Bad command or parameters'

                msg = protocol.create_msg(response)
                # send to client
                client_socket.send(msg)

        else:
            # prepare proper error to client
            response = 'Packet not according to protocol'
            #send to client
            msg = protocol.create_msg(response)
            # send to client
            client_socket.send(msg)
            # Attempt to clean garbage from socket
            client_socket.recv(1024)

    # close sockets
    print("Closing connection")


if __name__ == '__main__':
    main()
