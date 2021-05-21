import socket

message = ""

while message != "quit":
	message = input()
	the_message = bytes(message, "utf-8")

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(the_message, ("localhost", 5005))