import pygame as pg
import sys
from pygame.locals import *
from sprites import *

import calories

pg.init()
font = pg.font.SysFont(None, 20)
clicked = False
clickCounter = False

class constructButton():

    # colours for button and text
    button_col = (HIGHLIGHT)
    hover_col = (BLUE)
    click_col = (50, 150, 255)
    black = (255,255,255)
    text_col = black
    width = 32
    height = 32

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self, screen):
        global clicked
        global clickCounter
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
        global clickCounter
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
    buildingTowers = False

    buildTowerButton = button(500, 500, 'Build Tower')

    tower1 = constructButton(2*TILESIZE, 20*TILESIZE, "")
    tower2 = constructButton(8*TILESIZE, 18*TILESIZE, "")
    tower3 = constructButton(8*TILESIZE, 13*TILESIZE, "")
    tower4 = constructButton(8*TILESIZE, 7*TILESIZE, "")
    tower5 = constructButton(14*TILESIZE, 6*TILESIZE, "")
    tower6 = constructButton(20*TILESIZE, 7*TILESIZE, "")
    tower7 = constructButton(21*TILESIZE, 14*TILESIZE, "")
    tower8 = constructButton(27*TILESIZE, 7*TILESIZE, "")

    highlight = pg.Surface((TILESIZE, TILESIZE))
    highlight.fill(HIGHLIGHT)
    towerPlaceHolder = pg.Surface((TILESIZE, TILESIZE))
    towerPlaceHolder.fill(BLUE)

    while managing:

        buildTowerButton.draw_button(self.screen)
        draw_text("Defense Manager", font, (255, 255, 255), self.screen, 40, 40)
        draw_text("Calorie Points Available to Spend: " + str(calories.netCalories), font, (255, 255, 255), self.screen, 700, 40)

        if buildingTowers:

            tower1.draw_button(self.screen)
            tower2.draw_button(self.screen)
            tower3.draw_button(self.screen)
            tower4.draw_button(self.screen)
            tower5.draw_button(self.screen)
            tower6.draw_button(self.screen)
            tower7.draw_button(self.screen)
            tower8.draw_button(self.screen)

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
            if event.type == MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if (500 <= x <= 680 and 500 <= y <= 580):
                    buildingTowers = True
                    #Tower(self, 2, 2)
                    #image = pg.Surface((TILESIZE, TILESIZE))
                    #image.fill(BLUE)
                    #self.screen.blit(image, [5*TILESIZE, 5*TILESIZE])
                if (2*TILESIZE <= x <= 2*TILESIZE+32 and 20*TILESIZE <= y <= 20*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [2*TILESIZE, 20*TILESIZE])
                        Tower(self, 2, 20)
                        buildingTowers = False
                if (8*TILESIZE <= x <= 8*TILESIZE+32 and 18*TILESIZE <= y <= 18*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [8*TILESIZE, 18*TILESIZE])
                        Tower(self, 8, 18)
                        buildingTowers = False
                if (8*TILESIZE <= x <= 8*TILESIZE+32 and 13*TILESIZE <= y <= 13*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [8*TILESIZE, 13*TILESIZE])
                        Tower(self, 8, 13)
                        buildingTowers = False
                if (8*TILESIZE <= x <= 8*TILESIZE+32 and 7*TILESIZE <= y <= 7*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [8*TILESIZE, 7*TILESIZE])
                        Tower(self, 8, 7)
                        buildingTowers = False
                if (14*TILESIZE <= x <= 14*TILESIZE+32 and 6*TILESIZE <= y <= 6*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [14*TILESIZE, 6*TILESIZE])
                        Tower(self, 14, 6)
                        buildingTowers = False
                if (20*TILESIZE <= x <= 20*TILESIZE+32 and 7*TILESIZE <= y <= 7*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [20*TILESIZE, 7*TILESIZE])
                        Tower(self, 20, 7)
                        buildingTowers = False
                if (21*TILESIZE <= x <= 21*TILESIZE+32 and 14*TILESIZE <= y <= 14*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [21*TILESIZE, 14*TILESIZE])
                        Tower(self, 21, 14)
                        buildingTowers = False
                if (27*TILESIZE <= x <= 27*TILESIZE+32 and 7*TILESIZE <= y <= 7*TILESIZE+32):
                    if calories.netCalories >= 100:
                        calories.netCalories -= 100
                        self.screen.blit(towerPlaceHolder, [27*TILESIZE, 7*TILESIZE])
                        Tower(self, 27, 7)
                        buildingTowers = False

        pg.display.update()