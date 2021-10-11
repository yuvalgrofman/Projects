#   Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020

import socket
import protocol
import glob
import os 
import shutil
import subprocess


IP = ????
PHOTO_PATH = ???? # The path + filename where the screenshot at the server should be saved


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

        cmd, data = protocol.parse(cmd)  

        return True, cmd, data

    except: 

        return False, None, None 


def handle_client_request(command, params):
    """Create the response to the client, given the command is legal and params are OK

    For example, return the list of filenames in a directory
    Note: in case of SEND_PHOTO, only the length of the file will be sent

    Returns:
        response: the requested data

    """

    response = 'OK'
    return response


def dir(path : str):

    try: 
        files_list = glob.glob(path + "/*.*")
        return files_list

    except: 
        return False

def delete(path : str):
    try: 

        os.remove(path)
        return True

    except FileNotFoundError: 
        print("File not found")
        
        return False

def copy(file : str , dest : str):
    try: 

        shutil.copy(file, dest)
        return True

    except: 
        return False

def execute(path : str):
    try: 

        subprocess.Popen(['open'], path)
        return True

    except: 
        return False

def take_screenshot():
    pyautogui



def main():
    # open socket with client

    # (1)

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

                # add length field using "create_msg"

                # send to client

                if command == 'SEND_FILE':
                    # Send the data itself to the client

                    # (9)
                
                if command == 'EXIT':
                    break
            else:
                # prepare proper error to client
                response = 'Bad command or parameters'
                # send to client

        else:
            # prepare proper error to client
            response = 'Packet not according to protocol'
            #send to client

            # Attempt to clean garbage from socket
            client_socket.recv(1024)

    # close sockets
    print("Closing connection")


if __name__ == '__main__':
    main()
