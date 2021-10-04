import socket
import chatlib  # To use chatlib functions or consts, use chatlib.****

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5678

# HELPER SOCKET METHODS

def build_and_send_message(conn, code, data):
	"""
	Builds a new message using chatlib, wanted code and message. 
	Prints debug info, then sends it to the given socket.
	Paramaters: conn (socket object), code (str), data (str)
	Returns: Nothing
	"""

	msg = chatlib.build_message(code, data)
	print("Sent server: \'" + msg + "\'")
	conn.send(msg.encode())
	

def recv_message_and_parse(conn):
	"""
	Recieves a new message from given socket,
	then parses the message using chatlib.
	Paramaters: conn (socket object)
	Returns: cmd (str) and data (str) of the received message. 
	If error occured, will return None, None
	"""

	try:

		full_msg = conn.recv(1024).decode()
		cmd, data = chatlib.parse_message(full_msg)

		return cmd, data

	except:
		return None, None
	
	

def connect():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((SERVER_IP,SERVER_PORT))
	return s


def error_and_exit(error_msg):

	print(error_msg)
	exit()



def login(conn):
    username = input("Please enter username: \n")
    password = input("Please enter password: \n")

    while True:

        build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], username + "#" + password)

        (cmd,data) = recv_message_and_parse(conn)

        if  cmd == "LOGIN_OK":
            print("Login Successful")
            return 

        elif cmd == "ERROR":

            print("Error! Error! Username does not exist")
            username = input("Please enter another username: \n")

            if input("Would you like to change password?(Y)") == "Y":
                password = input("Please enter another password: \n")



		
        print("Login Unsuccessful. Trying again...")
	


def logout(conn):
	build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], "")
	print("Logout successful")

def main():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("127.0.0.1", 5678))

	login(s)	
	logout(s)

if __name__ == '__main__':
    main()
