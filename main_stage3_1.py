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

import game_world
from mario import Mario
from item_block import Item_Block
from background3 import Background
from tiles import Tiles
from tiles_bottom import Tiles_bottom
from block import Block
from pipe import Pipe
from monster_gumba import Monster_Gumba
from monster_turtle import Monster_Turtle
from coins import Coins
from air_tile import Air_tile

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
    global background, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block, gumba, gumba2, turtle, turtle2, turtle3
    global air_tile, air_tile2, air_tile3, air_tile4, air_tile5, air_tile6, air_tile7, air_tile8, air_tile9
    background = Background(960, 540)
    tiles_bottom = Tiles_bottom()
    mario = Mario(25, 590)

    air_tile = Air_tile(10, 550, 10)
    air_tile2 = Air_tile(430, 550, 2)
    air_tile3 = Air_tile(680, 550, 10)

    turtle = Monster_Turtle(550, 550, 150, 1)
    turtle2 = Monster_Turtle(320, 520, 120, 1)
    turtle3 = Monster_Turtle(1530, 550, 140, 1)


    coins = Coins(430, 620, 2)
    coins2 = Coins(955, 420, 4)

    item_block1 = Item_Block(1430, 650, 1)

    air_tile4 = Air_tile(900, 370, 10)
    block = Block(980, 470, 3)
    gumba = Monster_Gumba(960, 400, 40, 2)

    air_tile5 = Air_tile(1100, 550, 7)
    air_tile6 = Air_tile(1420, 550, 2)

    air_tile7 = Air_tile(1600, 550, 18)


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
    turtle.update()
    turtle2.update()
    turtle3.update()

    coins.update()
    coins2.update()
    if mario.x > 1920:
        game_framework.change_state(main_stage3_2)

    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    gumba.draw()
    turtle.draw()
    turtle2.draw()
    turtle3.draw()


    coins.draw()
    coins2.draw()

    item_block1.draw()


    air_tile.draw()
    air_tile2.draw()
    air_tile3.draw()
    air_tile4.draw()
    air_tile5.draw()
    air_tile6.draw()
    air_tile7.draw()
    block.draw()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


