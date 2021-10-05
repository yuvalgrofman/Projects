# Protocol Constants

CMD_FIELD_LENGTH = 16	# Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4   # Exact length of length field (in bytes)
MAX_DATA_LENGTH = 10**LENGTH_FIELD_LENGTH-1  # Max size of data field according to protocol
MSG_HEADER_LENGTH = CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages 
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
"login_msg" : "LOGIN",
"logout_msg" : "LOGOUT",
"HIGHSCORE" : "HIGHSCORE",
"MY_SCORE" : "MY_SCORE",
"GET_QUESTION" : "GET_QUESTION",
"SEND_ANSWER" : "SEND_ANSWER" 
}

PROTOCOL_SERVER = {
"login_ok_msg" : "LOGIN_OK",
"login_failed_msg" : "ERROR"
}

# Other constants
ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
	"""
	Gets command name (str) and data field (str) and creates a valid protocol message
	Returns: str, or None if error occured
	"""

	try:

		command = cmd

		if (len(command) > CMD_FIELD_LENGTH or len(data) > MAX_DATA_LENGTH):
			return None

		command = command + (" " * (16 - len(command))) 


		parameters = data 
		paramLength = str(len(parameters)) 
		paramLength = "0" * (4 - len(paramLength)) + paramLength

		full_msg = command + "|" + paramLength + "|" + parameters
		return full_msg
	
	except:
		return None


def parse_message(data):
	"""
	Parses protocol message and returns command name and data field
	Returns: cmd (str), data (str). If some error occured, returns None, None
	"""

	try:

		if (data[16] != "|" or data[21] != "|"):
			return None,None
		
		for i in range(len(data)):
			if data[i] == '|' and (i != 16 and i != 21):
				return None, None

		cmd = data[0:16].replace(" ","")

		msg = data[22:]
		msgLength = data[17:21]

		if (int(msgLength) != len(msg)):
			return None,None

		# The function should return 2 values
		return cmd, msg

	except:
		return None, None

	
def split_data(msg, expected_fields):
	"""
	Helper method. gets a string and number of expected fields in it. Splits the string 
	using protocol's data field delimiter (|#) and validates that there are correct number of fields.
	Returns: list of fields if all ok. If some error occured, returns None
	"""

	try:

		if msg.count("#") != expected_fields - 1:
			return None
		
		return msg.split("#")

	except:
		return None
		

	



def join_data(msg_fields):
	"""
	Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter. 
	Returns: string that looks like cell1#cell2#cell3
	"""

	try: 
		msg = ""
		for field in msg_fields:
			msg += '#' + str(field) 

		return msg

	except:
		return None

