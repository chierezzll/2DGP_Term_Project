from pico2d import *
import game_framework
import random

import game_framework
import title_state
import main_stage1_1
import main_stage1_3
import json
import os

import game_world

from mario import Mario
from item_block import Item_Block
from background import Background
from tiles1_2 import Tiles
from tiles_bottom1_2 import Tiles_bottom
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

BOTTOM = 225

name = "main_stage1_2"

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
    global background, tiles, tiles_bottom, mario, coins, item_block2, item_block1, item_block3, block1, block2, block3, block4, block5, gumba
    global gumba2, fire
    background = Background(960, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario()
    coins = Coins(850, 500, 4)
    item_block1 = Item_Block(225, 310, 1)
    item_block2 = Item_Block(1131, 450, 1)
    item_block3 = Item_Block(1320, 310, 1)
    block1 = Block(700, 310, 4)
    block2 = Block(820, 450, 8)
    block3 = Block(1050, 450, 4)
    block4 = Block(1131, 310, 1)
    block5 = Block(1300, 310, 1)
    gumba = Monster_Gumba(700, 215, 100, 1)
    gumba2 = Monster_Gumba(900, 480, 50, 1)

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
    gumba.update()
    gumba2.update()

    if mario.x > 1920:
        game_framework.change_state(main_stage1_3)

def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    gumba.draw()
    gumba2.draw()
    block1.draw()
    block2.draw()
    block3.draw()
    block4.draw()
    block5.draw()
    item_block1.draw()
    item_block2.draw()
    item_block3.draw()
    tiles.draw()
    tiles_bottom.draw()
    coins.draw()
    update_canvas()
    delay(0.06)


