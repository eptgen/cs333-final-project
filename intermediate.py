import socket
from shared_lib import ec_driver, PORT1, PORT2
from random import random

ACCEPT_RATIO = 0.8

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", PORT1))

while True:
	data, addr = sock.recvfrom(1024)
	print("Received string " + str(data) + ": ", end="")
	
	# There is a ACCEPT_RATIO chance that the message will go through. This
	# simulates an environment where it is not guaranteed that a specific
	# message will go through, making it necessary to implement error correcting
	# codes.
	if random() < ACCEPT_RATIO:
		sock.sendto(data, ("localhost", PORT2))
		print("accepting")
	else:
		print("rejecting")
