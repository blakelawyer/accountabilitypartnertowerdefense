import socket
import threading

HEADER = 64
PORT = 8009
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.3.147"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    thread = threading.Thread(target=recv)
    thread.start()

def recv():
    while True:
        print(client.recv(2048).decode(FORMAT))

while True:
    send(input())
