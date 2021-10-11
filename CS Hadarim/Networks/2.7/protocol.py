#   Ex. 2.7 template - protocol

Client_Commands = {"DIR" : 1,"DELETE" : 1,"COPY" : 2,"EXECUTE" : 1,"TAKE_SCREENSHOT" : 0, "SEND_PHOTO" : 0} 
Server = {}




LENGTH_FIELD_SIZE = 4
PORT = 8820


def check_cmd(data):
    """
    Check if the command is defined in the protocol, including all parameters
    For example, DELETE c:\work\file.txt is good, but DELETE alone is not
    """

    data = data.split(" ")

    if (len(data) == 0):
        return False

    cmd = data[0]
    param =  " ".join(data[1:])

    if (cmd in Client_Commands.keys() and Client_Commands[cmd] == len(param)):
        return True

    return False

def parse_cmd(data):
    data = data.split(" ")

    cmd = data[0]
    param =  data[1:]

    return cmd, data


    

def create_msg(data):
    """
    Create a valid protocol message, with length field
    """

    lenData = str(len(data))
    lenlenData = len(lenData)

    if (lenlenData > 2):
        raise ValueError("Illegal argument. Too much data.")
        
    msg = lenlenData + lenData + data
    return msg.encode()


def get_msg(conn):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """

    try: 
        lenlenData = int(conn.recv(2).decode())
        lenData = int(conn.recv(lenlenData).decode())

        remainingData = lenData 
        data = ""

        while (remainingData > 1024):
            data += conn.recv(1024).decode()
            remainingData -= 1024

        data += conn.recv(remainingData).decode()

        return True, data 

    except:
        return False, "Error"


