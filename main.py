import pygame as pg
import sys
from os import path

import calories
from settings import *
from sprites import *
from calorieMenu import *
from defenseManager import *


class Game:
    # Initializes the game, screen size, title, clock object, and prepares to load map data.
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        icon = pg.image.load("tower.png")
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    # Opens the map file and appends all the data to a list for easy access.
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map1.txt'), 'rt') as f1:
            for line in f1:
                self.map_data.append(line)
        self.log_data = []
        with open(path.join(game_folder, 'log1.txt'), 'rt') as f2:
            for line in f2:
                self.log_data.append(line)

    def new(self):

        # Creates a sprite group for easy management of all enemies, towers, etc. Easy to iterate through.
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.towers = pg.sprite.Group()
        self.bases = pg.sprite.Group()
        self.paths = pg.sprite.Group()
        self.portals = pg.sprite.Group()

        # Iterates through the map data and creates the corresponding objects.
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'E':
                    Enemy(self, col, row)
                if tile == 'P':
                    Path(self, col, row)
                if tile == 'X':
                    Portal(self, col, row)
                if tile == 'B':
                    Base(self, col, row)
                if tile == 'T':
                    Tower(self, col, row)

    def run(self):
        # The game loop - when self.playing = false, the game ends.
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()  # Handles events.
            self.update()  # Updates the game state based on events + time that's passed.
            self.draw()  # Each tick, we're re-drawing everything on the screen so that it's updated.

    # Quits the game.
    def quit(self):
        pg.quit()
        sys.exit()

    # Updates all sprites in the designated group.
    def update(self):
        self.all_sprites.update()
        for tower in self.towers:
            tower.update_tower()
        for enemy in self.enemies:
            enemy.update_enemy()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)  # Fills the screen with the background color.
        self.draw_grid()  # Draws a grid for easy visualization, may be removed later.
        self.all_sprites.draw(self.screen)  # Draws all sprites by bliting them on screen.
        pg.display.flip()

    def events(self):
        # Handles all events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_e:
                    calorieMenuScreen(self)
                if event.key == pg.K_q:
                    defenseManagerScreen(g)


g = Game()  # Creates Game object.

# Executes until escape it hit or the game is quit otherwise.
# Functionally executes once; run() is the loop that does the legwork.
while True:
    g.new()  # Initializes all the sprite groups and loads the tile map from map.txt.
    g.run()  # This is where the magic happens..
