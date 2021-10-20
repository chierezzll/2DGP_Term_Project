from pico2d import *
import game_framework
import random

import game_framework
import title_state
import main_stage1_1
import json
import os

# Game object class here

BOTTOM = 240

name = "main_stage1_2"


class Background:
    global mario

    def __init__(self, x, y): # 생성자
        self.image = load_image('background.png')
        self.x = x
        self.y = y

    def update(self):
        if mario.x > 600:
            self.x = self.x - (mario.x - 600)

    def draw(self):
        self.image.clip_draw(0, 0, 1920, 1080, self.x, self.y)
        self.image.clip_draw(0, 0, 1920, 1080, self.x + 1920, self.y)

class Tiles:
    def __init__(self):
        self.image = load_image('tiles_001.png')
        self.x = 300
        self.y = 200

    def draw(self):
        k = 0
        for i in range(23):
            self.image.clip_draw(0, 10, 95, 100, 0 + k, self.y - 50 )
            k += 90

class Tiles_bottom:
    def __init__(self):
        self.image = load_image('tiles_007.png')

    def draw(self):
        k = 0

        for i in range(65):
             self.image.draw(k, 160)
             self.image.draw(k, 130)
             self.image.draw(k, 100)
             self.image.draw(k, 70)
             self.image.draw(k, 40)
             k += 30

class Block:
    def __init__(self, x, y):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y

    def draw(self):
        k = 0
        for i in range(7):
            self.image.clip_draw(46, 110, 20, 31, self.x + k, self.y)
            k += 20

class Item_Block():
    def __init__(self, x, y):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(64, 110, 20, 31, self.x, self.y)

class Monster_Gumba:
    def __init__(self):
        self.image = load_image('Enemies.png')
        self.x = 600
        self.y = 215
        self.dir = 1
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += 3 * self.dir
        if self.x >= 700:
            self.dir = -1
        elif self.x <= 600:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(0 + self.frame * 30, 0, 30, 30, self.x, self.y)

class Coins:
    def __init__(self, x, y):
        self.image = load_image('items.png')
        self.frame = 0
        self.x = x
        self.y = y

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        k = 0
        for i in range(3):
            self.image.clip_draw(0 + self.frame * 15, 16, 15, 16, self.x + k, self.y)
            k += 30

class Mario:
    global item_block1
    def __init__(self):
        self.image = load_image('mario_sheet.png')
        self.x = 100
        self.y = 240
        self.dir = 0
        self.frame = 0
        self.posx = 350
        self.posy = 90
        self.isJump = 0
        self.v = 7
        self.m = 2
        self.f = 0

    def update(self):
        self.frame = (self.frame + 1 ) % 4
        self.x += 15 * self.dir     #마리오 이동속도
        if self.isJump > 0:
            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                self.f = (0.5 * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                self.f = -(0.5 * self.m * (self.v * self.v))

            self.y += self.f
            self.v -= 1
            if self.y == BOTTOM:
                self.isJump = 0
                self.v = 7

    def draw(self):
        self.image.clip_draw(self.posx + self.frame * 45 , self.posy, 40, 90, self.x, self.y)          # 350, 400, 450, 500

    def jump(self, j):
        self.isJump = j


def handle_events():
    global running
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.dir += 1
                mario.posx = 350
                mario.posy = 90
            elif event.key ==SDLK_LEFT:
                mario.dir -= 1
                mario.posx = 620
                mario.posy = 0
            elif event.key == SDLK_SPACE:
                mario.isJump = 1


        elif event.type == SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                mario.dir -= 1
                mario.frame = 0
            elif event.key ==SDLK_LEFT:
                mario.dir += 1
                mario.frame = 0

def enter():
    global background, background2, tiles, tiles_bottom, mario, coins, item_block2, item_block1, block1, gumba
    background = Background(960, 540)
    background2 = Background(960 + 1820, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario()
    coins = Coins(580, 360)
    item_block1 = Item_Block(450, 310)
    item_block2 = Item_Block(620, 430)
    block1 = Block(700, 310)
    gumba = Monster_Gumba()
    mario.dir += 1

def exit():
    global background, background2, tiles, tiles_bottom, mario, coins, item_block2, item_block1, block1, gumba
    del(background)
    del(background2)
    del(tiles)
    del(tiles_bottom)
    del(mario)
    del(coins)
    del(item_block1)
    del(item_block2)
    del(block1)
    del(gumba)

def pause():
    pass

def resume():
    pass

def update():
    mario.update()
    coins.update()
    gumba.update()

def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    gumba.draw()
    block1.draw()
    item_block1.draw()
    item_block2.draw()
    tiles.draw()
    tiles_bottom.draw()
    coins.draw()
    update_canvas()
    delay(0.06)


