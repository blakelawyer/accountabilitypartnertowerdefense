import pygame as pg
import sys
from pygame.locals import *

import calories
from calories import *

pg.init()
font = pg.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def calorieMenuScreen(self):
    burnedEntered = False
    consumedEntered = False
    doneEntering = False

    caloriesBurned = 0
    caloriesConsumed = 0
    pressedNumbers = ""

    loggingCalories = True
    while loggingCalories:

        self.screen.fill((0, 0, 0))
        draw_text("calorieMenu", font, (255, 255, 255), self.screen, 20, 20)
        draw_text("Calories Burned: " + str(caloriesBurned), font, (255, 255, 255), self.screen, 320, 20)
        draw_text("Calories Consumed: " + str(caloriesConsumed), font, (255, 255, 255), self.screen, 520, 20)
        draw_text(pressedNumbers, font, (255, 255, 255), self.screen, 20, 80)

        if burnedEntered == False and not doneEntering:
            draw_text("How many calories did you burn today?", font, (255, 255, 255), self.screen, 20, 60)
        elif burnedEntered == True and consumedEntered == False and doneEntering == False:
            draw_text("How many calories did you consume today?", font, (255, 255, 255), self.screen, 20, 60)
        elif doneEntering:
            calories.netCalories = (2000 - caloriesConsumed) + caloriesBurned
            draw_text("Net Calories: " + str(calories.netCalories), font, (255, 255, 255), self.screen, 20,
                      60)
        draw_text("Total Calorie Points: " + str(2000 - caloriesConsumed + caloriesBurned), font, (255, 255, 255), self.screen, 720, 20)

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
                if event.key == pg.K_BACKSPACE:
                    if (pressedNumbers != ""):
                        pressedNumbers = pressedNumbers[:len(pressedNumbers) - 1]
                        print("Backspace:", pressedNumbers)

                if event.key == pg.K_RETURN:
                    if (pressedNumbers != ""):
                        enteredCalories = int(pressedNumbers)
                        if (burnedEntered == False):
                            caloriesBurned += enteredCalories
                            burnedEntered = True
                        elif (burnedEntered == True and consumedEntered == False):
                            caloriesConsumed += enteredCalories
                            consumedEntered = True
                            doneEntering = True
                        pressedNumbers = ""

        pg.display.update()
