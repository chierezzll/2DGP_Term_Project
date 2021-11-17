from pico2d import *
import game_framework
import random
import game_framework
import title_state
import main_stage3_2
import json
import os

# Game object class here

BOTTOM = 225

name = "main_stage3_3"


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
from boss import Boss

# Game object class here

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
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
    global background, tiles, tiles_bottom, mario, boss
    background = Background(960, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario(200, 225)
    boss = Boss(1100, 240, random.randint(100, 200), 1)

    mario.velocity += RUN_SPEED_PPS

def exit():
    game_world.clear()


def pause():
    pass

def resume():
    pass

def update():
    mario.update()
    boss.update()
    # if mario.x > 1920:
    #     game_framework.change_state(main_stage1_2)

    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    tiles.draw()
    tiles_bottom.draw()

    boss.draw()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


