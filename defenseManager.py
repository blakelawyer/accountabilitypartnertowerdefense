import pygame as pg
import sys
from pygame.locals import *

import calories

pg.init()
font = pg.font.SysFont(None, 20)
clicked = False

class button():
    # colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    black = (255,255,255)
    text_col = black
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self, screen):
        global clicked
        action = False

        # get mouse position
        pos = pg.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1:
                clicked = True
                pg.draw.rect(screen, self.click_col, button_rect)
            elif pg.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pg.draw.rect(screen, self.hover_col, button_rect)
        else:
            pg.draw.rect(screen, self.button_col, button_rect)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def defenseManagerScreen(self):
    managing = True
    buildTowerButton = button(500, 500, 'Play Again?')
    while managing:

        buildTowerButton.draw_button(self.screen)
        draw_text("Defense Manager", font, (255, 255, 255), self.screen, 40, 40)
        draw_text("Calorie Points Available to Spend: " + str(calories.netCalories), font, (255, 255, 255), self.screen, 700, 40)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_q:
                    managing = False

        pg.display.update()