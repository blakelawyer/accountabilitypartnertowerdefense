import socket
import threading

HEADER = 64
PORT = 8009
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.16.0.80"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    thread = threading.Thread(target=recv)
    thread.start()

def recv():
    while True:
        msg = client.recv(2048).decode(FORMAT)
        print(f"[{SERVER}] {msg}")


while True:
    send(input())
