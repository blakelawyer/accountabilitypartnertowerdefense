import socket
import threading

HEADER = 64
PORT = 8009
SERVER = socket.gethostbyname("172.16.0.80")
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

clients = []

def handle_client1(conn, addr):
    msg = conn.recv(2048).decode(FORMAT)
    print(f"[{addr}] {msg}")
    clients.append(msg)

def handle_client2(conn, addr):
    msg = conn.recv(2048).decode(FORMAT)
    print(f"[{addr}] {msg}")
    clients.append(msg)


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn1, addr = server.accept()
    msg = conn1.recv(2048).decode(FORMAT)
    print(f"[{addr}] {msg}")
    clients.append(msg)
    conn2, addr = server.accept()
    msg = conn2.recv(2048).decode(FORMAT)
    print(f"[{addr}] {msg}")
    clients.append(msg)

    conn1.send(clients[1].encode(FORMAT))
    conn2.send(clients[0].encode(FORMAT))




    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()

