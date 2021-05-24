import socket
from time import time
from shared_lib import ec_driver, K, PORT2

TIMEOUT = 0.15 # The maximum time period between two messages of the same encoded message

# Setting up the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", PORT2))

decoded = True	# Indicates whether the current message has been decoded. Defaults
		# to True so that the program doesn't print the failed message in the beginning
fragments = []	# The current fragments received
time_of_last_message = 0

# data collection
successful = 0

while True:
	data, addr = sock.recvfrom(1024)
	
	# If there was too much of a gap since the last message, the program
	# starts to attempt to read another message
	if time() - time_of_last_message > TIMEOUT:
		# If the message was already decoded, everything is fine; otherwise, we have
		# to abort trying to read the current message
		if not decoded:
			print("failed to get message :( retrying")
		decoded = False
		fragments = []
		
	# Adds the received data to the current fragments
	fragments.append(data)
	
	# If the number of fragments is K, then we have enough to decode the message
	if len(fragments) == K:
		message = ec_driver.decode(fragments)
		print("MESSAGE RECEIVED: " + str(message))
		decoded = True
		successful += 1
		print("successes: " + str(successful))
	elif len(fragments) < K:
		print("Accumulating message (" + str(len(fragments)) + "/" + str(K) + ")")
	
	# If we have more fragments than necessary, acknowledge it and do nothing
	else:
		print("Received redundancy")
		
	# Capture the time of the last message
	time_of_last_message = time()






































