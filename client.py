import socket
import threading
import pygame as pg
import sys
from os import path
import waveManager
import calories
from paused import paused
from settings import *
from sprites import *
from calorieMenu import *
from defenseManager import *
from gameOver import *
import main

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
    msg = client.recv(2048).decode(FORMAT)
    print(f"[{SERVER}] {msg}")


send(input())
g = main.Game()  # Creates Game object.

# Executes until escape it hit or the game is quit otherwise.
# Functionally executes once; run() is the loop that does the legwork.
while True:
    g.new()  # Initializes all the sprite groups and loads the tile map from map.txt.
    g.run()  # This is where the magic happens..

