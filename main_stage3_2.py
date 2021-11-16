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
from tiles1_2 import Tiles
from tiles_bottom1_2 import Tiles_bottom
from block import Block
from pipe import Pipe
from monster_gumba import Monster_Gumba
from coins import Coins
from air_tile import Air_tile
from castle import Castle

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
    global background, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block, gumba, gumba2, gumba3, gumba4
    global air_tile, castle
    background = Background(960, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario(25, 590)

    air_tile = Air_tile(10, 550, 10)

    block = Block(620, 320, 5)
    item_block1 = Item_Block(670, 420, 1)



    gumba = Monster_Gumba(600, 215, 50, 1)
    gumba2 = Monster_Gumba(1500, 215, 70, 2)
    gumba3 = Monster_Gumba(800, 215, 90, 2)
    gumba4 = Monster_Gumba(1300, 215, 50, 1)

    castle = Castle(1770, 275)

    mario.velocity += RUN_SPEED_PPS

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def update():
    mario.update()
    gumba.update()
    gumba2.update()
    gumba3.update()
    gumba4.update()
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
    gumba3.draw()
    gumba4.draw()
    air_tile.draw()
    tiles.draw()
    tiles_bottom.draw()
    block.draw()
    item_block1.draw()
    castle.draw()

    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()
    delay(0.06)


