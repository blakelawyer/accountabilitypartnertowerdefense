import socket

HEADER = 64
PORT = 8007
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.16.0.80"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)


send(input())
msg = client.recv(2048).decode(FORMAT)
print(f"[{SERVER}] {msg}")
import main
g = main.Game()  # Creates Game object.

# Executes until escape it hit or the game is quit otherwise.
# Functionally executes once; run() is the loop that does the legwork.
while True:
    g.new()  # Initializes all the sprite groups and loads the tile map from map.txt.
    g.run()  # This is where the magic happens..

