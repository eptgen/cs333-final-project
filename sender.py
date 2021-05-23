import socket
from shared_lib import ec_driver, PORT1

message = ""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while message != "quit":
	message = input()
	the_message = bytes(message, "utf-8")
	fragments = ec_driver.encode(the_message)
	
	# Send each fragment one by one
	for fragment in fragments:
		sock.sendto(fragment, ("localhost", PORT1))
