import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 5000))

while True:
    msg = s.recv(24)
    print(msg.decode("utf-8"))



