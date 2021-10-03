import pygame as pg

import calories
from settings import *
import math


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.level = 1

        self.health = 100
        self.speed = 1

    def update_enemy(self):
        toRemove = -1
        for enemy in calories.enemy_list:
            if enemy.health <= 0:
                enemy.kill()
                toRemove = enemy
        if toRemove != -1:
            calories.enemy_list.remove(toRemove)

        toRemove = -1
        for enemy in calories.enemy_list:
            if enemy.level == 1:
                if enemy.rect.x > 26 * TILESIZE:
                    enemy.rect.x -= 1
                elif enemy.rect.x == 26 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 2:
                if enemy.rect.y < 11 * TILESIZE:
                    enemy.rect.y += 1
                elif enemy.rect.y == 11 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 3:
                if enemy.rect.x > 17 * TILESIZE:
                    enemy.rect.x -= 1
                elif enemy.rect.x == 17 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 4:
                if enemy.rect.y > 3 * TILESIZE:
                    enemy.rect.y -= 1
                elif enemy.rect.y == 3 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 5:
                if enemy.rect.x > 11 * TILESIZE:
                    enemy.rect.x -= 1
                elif enemy.rect.x == 11 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 6:
                if enemy.rect.y < 11 * TILESIZE:
                    enemy.rect.y += 1
                elif enemy.rect.y == 11 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 7:
                if enemy.rect.x > 5 * TILESIZE:
                    enemy.rect.x -= 1
                elif enemy.rect.x == 5 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 8:
                if enemy.rect.y < 15 * TILESIZE:
                    enemy.rect.y += 1
                elif enemy.rect.y == 15 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 9:
                if enemy.rect.x < 11 * TILESIZE:
                    enemy.rect.x += 1
                elif enemy.rect.x == 11 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 10:
                if enemy.rect.y < 20 * TILESIZE:
                    enemy.rect.y += 1
                elif enemy.rect.y == 20 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 11:
                if enemy.rect.x > 4 * TILESIZE:
                    enemy.rect.x -= 1
                elif enemy.rect.x == 4 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 12:
                if enemy.rect.y > 18 * TILESIZE:
                    enemy.rect.y -= 1
                elif enemy.rect.y == 18 * TILESIZE:
                    enemy.level += 1
            if enemy.level == 13:
                if enemy.rect.x > 0:
                    enemy.rect.x -= 1
                elif enemy.rect.x == 0:
                    enemy.level += 1
            if enemy.level == 14:
                calories.baseHealth -= 1
                enemy.kill()
                toRemove = enemy

        if toRemove != -1:
            calories.enemy_list.remove(toRemove)



class Tower(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.towers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("catapult-2.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.time = 0
        self.damage = 25
        self.range = 10
        self.shotSpeed = 1

    def shoot(self, enemy):
        enemy.health -= 25

    def update_tower(self):

        min_distance = 999999
        target = -1

        for enemy in calories.enemy_list:
            a = [self.x, self.y]
            b = [enemy.x, enemy.y]
            print(math.dist(a, b))
            if math.dist(a, b) <= 5:
                print("in rangasd")
                if math.dist(a, b) < min_distance:
                    min_distance = math.dist(a, b)
                    print("Min distance", min_distance)
                    target = enemy

        if target != -1:
            if self.time == 0:
                self.time = pg.time.get_ticks()
                self.shoot(target)
            else:
                current_time = pg.time.get_ticks()
                if current_time - self.time >= 1000:
                    self.shoot(target)
                    self.time = current_time




class Base(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bases
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.health = 10

class Portal(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.portals
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.health = 10

class Path(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.paths
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
