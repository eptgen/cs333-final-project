import socket
from shared_lib import ec_driver, PORT1

message = ""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

number_of_messages = 0

while message != "quit":
	message = input()
	the_message = bytes(message, "utf-8")
	fragments = ec_driver.encode(the_message)
	
	total_length = 0
	
	# Send each fragment one by one
	for fragment in fragments:
		sock.sendto(fragment, ("localhost", PORT1))
		total_length += len(fragment)
		
	print("old/new length: " + str(len(message)) + "/" + str(total_length))
	
	# Increment counter
	number_of_messages += 1
	print("number of messages sent: " + str(number_of_messages))
