# import random
#
# import pygame as pg
# import sys
#
# import sprites
# from pygame.locals import *
#
# class Wave:
#
#     # map1x, map1y = [31, 9]
#     # map2x, map2y = [31, 8]
#
#     def __init__(self):
#         waves = [
#             [10, 0, 0],
#             [20, 0, 0],
#             [10, 10, 0],
#             [20, 10, 0],
#             [10, 0, 10],
#             [0, 10, 10],
#             [10, 10, 10],
#             [0, 20, 10],
#             [20, 10, 20],
#             [20, 0, 20],
#             [0, 30, 0],
#             [20, 10, 20],
#             [10, 20, 20],
#             [20, 20, 20]
#         ]
#         self.startwave(self, waves[0][0])
#
#     def startwave(self, num):
#         if random.randrange(2) == 0:
#             for i in num:
#                 sprites.Enemy(self, 31, 9)
#
#     def movewave(self, ):
