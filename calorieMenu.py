import pygame as pg
import sys
from pygame.locals import *

pg.init()
font = pg.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def calorieMenuScreen(self):

    pressedNumbers = ""

    loggingCalories = True
    while loggingCalories:

        self.screen.fill((0, 0, 0))
        draw_text("calorieMenu", font, (255, 255, 255), self.screen, 20, 20)
        draw_text("How many calories did you burn?", font, (255, 255, 255), self.screen, 20, 60)
        draw_text("ex. 300cal", font, (255, 255, 255), self.screen, 20, 80)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_e:
                    loggingCalories = False
                if event.key == pg.K_0:
                    pressedNumbers += "0"
                    print(pressedNumbers)
                if event.key == pg.K_1:
                    pressedNumbers += "1"
                    print(pressedNumbers)
                if event.key == pg.K_2:
                    pressedNumbers += "2"
                    print(pressedNumbers)
                if event.key == pg.K_3:
                    pressedNumbers += "3"
                    print(pressedNumbers)
                if event.key == pg.K_4:
                    pressedNumbers += "4"
                    print(pressedNumbers)
                if event.key == pg.K_5:
                    pressedNumbers += "5"
                    print(pressedNumbers)
                if event.key == pg.K_6:
                    pressedNumbers += "6"
                    print(pressedNumbers)
                if event.key == pg.K_7:
                    pressedNumbers += "7"
                    print(pressedNumbers)
                if event.key == pg.K_8:
                    pressedNumbers += "8"
                    print(pressedNumbers)
                if event.key == pg.K_9:
                    pressedNumbers += "9"
                    print(pressedNumbers)
                if event.key == pg.K_RETURN:
                    print("User hit enter!")
                    enteredCalories = int(pressedNumbers)

        pg.display.update()