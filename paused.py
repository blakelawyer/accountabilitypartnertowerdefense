import pygame as pg
import sys
from pygame.locals import *
from sprites import *

pg.init()
font = pg.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def paused(self):

    paused = True
    while paused:

        draw_text("PAUSED", font, (255, 255, 255), self.screen, 40, 40)
        draw_text("Press Space to Continue...", font, (255, 255, 255), self.screen, 700, 40)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pg.K_SPACE:
                    paused = False
        pg.display.update()