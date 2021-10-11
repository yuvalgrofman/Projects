import socket
import chatlib  # To use chatlib functions or consts, use chatlib.**
import re

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
	# print("Sent server: " + msg)
	



	


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

	print("Your score is " + data)

def get_highscore(conn):
	cmd , data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["HIGHSCORE"], "")
	print(data)

def play_question(conn): 
	cmd, data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["GET_QUESTION"],"")

	dataList = chatlib.split_data(data, 6)

	print(dataList[1])
	print("The options are: \n 1: " + dataList[2] + "\n 2: " + dataList[3] + "\n 3: " + dataList[4] + "\n 4: " + dataList[5])
	answer = input("write your answer to the quesion. \n")

	newCmd, newData = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["SEND_ANSWER"], dataList[0] + '#' + answer)

	if (newCmd == "WRONG_ANSWER"):
		print("wrong answer. The correct answer is #" + newData)
	
	elif (newCmd == "CORRECT_ANSWER"):
		print("correct answer.")
	
def get_logged_users(conn):
	cmd , data = build_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["LOGGED"], "")

	print("Logged Users: " + data)
		



def main():

	conn = connect()
	login(conn)

	while (True):

		print("""p        Play a trivia question
s        Get my score
h        Get high score
l        Get logged users
q        Quit""")
		cmd = input("Write a command \n")

		if (cmd == "s"):
			get_score(conn)

		elif (cmd == "h"):
			get_highscore(conn)
		
		elif (cmd == 'p'):
			play_question(conn)
		
		elif(cmd == "l"):
			get_logged_users(conn)

		elif (cmd == 'q'):
			break

	logout(conn)
	conn.close()

if __name__ == '__main__':
    main()