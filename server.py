import socket
import threading

HEADER = 64
PORT = 8008
SERVER = socket.gethostbyname("localhost")
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    while True:
        msg = conn.recv(2048).decode(FORMAT)
        print(f"[{addr}] {msg}")

def start():
    print("[STARTING] server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

    while True:
        message = input().encode(FORMAT)
        conn.send(message)


