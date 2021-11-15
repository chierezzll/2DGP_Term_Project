from pico2d import *
import game_framework
import random
import game_framework
import title_state
import main_stage3_1
import main_stage3_3
import json
import os

# Game object class here

BOTTOM = 225

name = "main_stage3_2"


import game_world
from mario import Mario
from item_block import Item_Block
from background3 import Background
from tiles import Tiles
from tiles_bottom import Tiles_bottom
from block import Block
from pipe import Pipe
from monster_gumba import Monster_Gumba
from coins import Coins

# Game object class here

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            mario.handle_event(event)

def enter():
    global background, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block1, gumba, gumba2, pipe, pipe2, pipe3
    global fire
    background = Background(960, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario(200, 225)
    coins = Coins(580, 360, 3)
    coins2 = Coins(1450, 235, 7)
    item_block1 = Item_Block(450, 310, 3)
    item_block2 = Item_Block(620, 430, 3)
    block1 = Block(550, 310, 2)
    gumba = Monster_Gumba(600, 215, 50, 1)
    gumba2 = Monster_Gumba(1500, 215, 70, 2)
    pipe = Pipe(1000, 225, 0)
    pipe2 = Pipe(1350, 285, 1)
    pipe3 = Pipe(1700, 330, 2)

    mario.velocity += RUN_SPEED_PPS

def exit():
    game_world.clear()

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
    if mario.x > 1920:
        game_framework.change_state(main_stage3_3)

    for game_object in game_world.all_objects():
        game_object.update()


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

    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()
    delay(0.06)


