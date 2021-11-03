from pico2d import *
import game_framework
import random
import game_framework
import title_state
import main_stage2_3
import main_stage3_2
import json
import os

# Game object class here

BOTTOM = 225

name = "main_stage3_1"


class Background:
    global mario

    def __init__(self, x, y): # 생성자
        #self.image = load_image('background.png')
        self.image = load_image('bg2.png')
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

class Pipe:
    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    def draw(self):
        k = 0
        if self.l == 0: # pipe의 y가 225
            self.image.clip_draw(84, 97, 52, 50, self.x, self.y)
        elif self.l == 1:       # pipe의 y가 285
            self.image.clip_draw(84, 97, 52, 50, self.x, self.y)
            for i in range(4):
                self.image.clip_draw(84, 97, 52, 15, self.x, self.y - 33 - k)
                k += 15
        elif self.l == 2:       ## pipe의 y가 330
            self.image.clip_draw(84, 97, 52, 50, self.x, self.y)
            for i in range(7):
                self.image.clip_draw(84, 97, 52, 15, self.x, self.y - 33 - k)
                k += 15

class Item_Block():
    def __init__(self, x, y):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y

    def draw(self):
        self.image.clip_draw(64, 110, 20, 31, self.x, self.y)

class Monster_Gumba:
    def __init__(self, x ,y):
        self.image = load_image('Enemies.png')
        self.x = x
        self.y = y
        self.tx = x
        self.dir = 1
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += 3 * self.dir
        if self.x >= self.tx + 100:
            self.dir = -1
        elif self.x <= self.tx - 100:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(0 + self.frame * 30, 0, 30, 30, self.x, self.y)

class Coins:
    def __init__(self, x, y, l):
        self.image = load_image('items.png')
        self.frame = 0
        self.x = x
        self.y = y
        self.l = l

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        k = 0
        for i in range(self.l):
            self.image.clip_draw(0 + self.frame * 15, 16, 15, 16, self.x + k, self.y)
            k += 30

class Mario:
    global item_block1
    def __init__(self):
        self.image = load_image('mario_sheet.png')
        self.x = 200
        self.y = 225
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
        self.x += 10 * self.dir     #마리오 이동속도
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
        if mario.dir != 0:
            self.image.clip_draw(self.posx + self.frame * 45 , self.posy, 40, 90, self.x, self.y, 50, 50)          # 350, 400, 450, 500
        else:
            self.image.clip_draw(self.posx , self.posy, 40, 90, self.x, self.y, 50, 50)


    def jump(self, j):
        self.isJump = j

class Fire:
    global mario

    def __init__(self):
        self.image = load_image('fire.png')
        self.frame = 0
        self.x = 0
        self.isSkill = 0
        self.firebeg = 0
        self.firebegy= 0

    def update(self):
        self.frame = (self.frame + 1) % 3
        if self.isSkill > 0:
            self.x += 45
            if self.x > 300:
                self.x = 0
                self.isSkill = 0

        elif self.isSkill < 0:
            self.x -= 45
            if self.x < -300:
                self.x = 0
                self.isSkill = 0

        elif self.isSkill == 0:
            self.firebeg = mario.x
            self.firebegy = mario.y



    def skill(self, j):
        self.isSkill = j

    def draw(self):
        if self.isSkill > 0:
            self.image.clip_draw(0 + self.frame * 17, 80, 15, 15, self.firebeg + self.x, self.firebegy, 25, 25)
        elif self.isSkill < 0:
            self.image.clip_draw(0 + self.frame * 17, 80, 15, 15, self.firebeg + self.x, self.firebegy, 25, 25)

def handle_events():
    global running
    global mario
    global fire

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_INSERT:
            game_framework.change_state(main_stage3_2)
        elif event.type == SDL_KEYDOWN:     # 이동
            if event.key == SDLK_RIGHT:
                mario.dir += 1
                mario.posx = 350
                mario.posy = 90
            elif event.key == SDLK_LEFT:
                mario.dir -= 1
                mario.posx = 620
                mario.posy = 0
            elif event.key == SDLK_SPACE:
                mario.isJump = 1
            elif event.key == SDLK_a:
                if mario.dir != -1:
                    fire.isSkill = 1
                else:
                    fire.isSkill = -1
            elif event.key == SDLK_DOWN:
                mario.posx = 620



        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                mario.dir -= 1
                mario.frame = 0
                mario.posx = 350
            elif event.key == SDLK_LEFT:
                mario.dir += 1
                mario.frame = 0
                mario.posy = 0
                mario.posx = 750
            elif event.key == SDLK_DOWN:
                mario.posx = 350

def enter():
    global background, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block1, gumba, gumba2, pipe, pipe2, pipe3
    global fire
    background = Background(960, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario()
    coins = Coins(580, 360, 3)
    coins2 = Coins(1450, 235, 7)
    item_block1 = Item_Block(450, 310)
    item_block2 = Item_Block(620, 430)
    block1 = Block(550, 310)
    gumba = Monster_Gumba(600, 215)
    gumba2 = Monster_Gumba(1500, 215)
    fire = Fire()
    pipe = Pipe(1000, 225, 0)
    pipe2 = Pipe(1350, 285, 1)
    pipe3 = Pipe(1700, 330, 2)
    mario.dir += 1

def exit():
    global background, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block1, gumba, gumba2, pipe, pipe2, pipe3
    global fire
    del(background)
    del(tiles)
    del(tiles_bottom)
    del(mario)
    del(coins)
    del(coins2)
    del(item_block1)
    del(item_block2)
    del(block1)
    del(gumba)
    del(gumba2)
    del(fire)
    del(pipe)
    del(pipe2)
    del(pipe3)

def pause():
    pass

def resume():
    pass

def update():
    mario.update()
    coins.update()
    coins2.update()
    gumba.update()
    gumba2.update()
    fire.update()
    if mario.x > 1920:
        game_framework.change_state(main_stage3_2)



def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    gumba.draw()
    gumba2.draw()
    block1.draw()
    item_block1.draw()
    item_block2.draw()
    tiles.draw()
    tiles_bottom.draw()
    coins.draw()
    coins2.draw()
    pipe.draw()
    pipe2.draw()
    pipe3.draw()

    fire.draw()

    update_canvas()
    delay(0.06)


