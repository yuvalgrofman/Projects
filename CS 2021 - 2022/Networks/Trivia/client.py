import socket
import chatlib  # To use chatlib functions or consts, use chatlib.**

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

	conn.send(msg.encode())
	print("Sent server: " + msg)
	



	


def recv_message_and_parse(conn):
	"""
	Recieves a new message from given socket,
	then parses the message using chatlib.
	Paramaters: conn (socket object)
	Returns: cmd (str) and data (str) of the received message. 
	If error occured, will return None, None
	"""
	full_msg =  conn.recv(1024).decode()
		
	cmd, data = chatlib.parse_message(full_msg)
	return cmd, data
	
	

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((SERVER_IP, SERVER_PORT))
	return s


def error_and_exit(error_msg):
	print(error_msg)
	exit()


def login(conn):
	
	while (True):
		username = input("Please enter username: \n")
		password = input("Please enter password: \n")

		build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["login_msg"], username+"#"+password)
		cmd, data = recv_message_and_parse(conn) 

		if (cmd == "LOGIN_OK"):
			return
		
		print("Login failed please try again.")

	

def logout(conn):
	build_and_send_message(conn, chatlib.PROTOCOL_CLIENT["logout_msg"], "")

def  build_send_recv_parse(conn, cmd, data):

	build_and_send_message(conn, cmd, data)
	cmd , data = recv_message_and_parse(conn)

	return cmd, data

def get_score(conn):
	cmd, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["MY_SCORE"], "")

	if (not cmd == "YOUR_SCORE"):
		error_and_exit("Received wrong error from Server")

	return data

def get_highscore(conn):
	cmd , data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["HIGHSCORE"], "")
	print(data)

def play_question(conn): 
	cmd, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["GET_QUESTION"],"")

	dataList = chatlib.split_data(data)
	print(dataList[1])
	answer = input("write your answer to the quesion? ")

	build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["SEND_ANSWER"], dataList[0] + '#' + answer)


def main():

	conn = connect()
	login(conn)

	while (True):

		cmd = input("Write a command \n")

		if (cmd == "s"):
			print("Your score is: " + get_score(conn))

		elif (cmd == "h"):
			get_highscore(conn)

		elif (cmd == 'q'):
			break

	logout(conn)
	conn.close()

if __name__ == '_main_':
    main()