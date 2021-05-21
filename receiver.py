import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("localhost", 5005))

while True:
    data, addr = sock.recvfrom(1024)
    print("received message: %s" % data)