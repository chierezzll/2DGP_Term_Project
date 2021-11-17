from pico2d import *
import game_framework
import random
import game_framework
import title_state
import main_stage1_3
import main_stage2_2

import game_world

from mario import Mario
from item_block import Item_Block
from background2 import Background
from tiles import Tiles
from tiles_bottom import Tiles_bottom
from block import Block
from pipe import Pipe
from monster_gumba import Monster_Gumba
from coins import Coins
from air_tile import Air_tile

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

BOTTOM = 225

name = "main_stage2_1"

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
    global background2, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block1, gumba, gumba2
    global air_tile, air_tile2, air_tile3, air_tile4, air_tile5, air_tile6, air_tile7, air_tile8, air_tile9
    background2 = Background(960, 540)
    mario = Mario(170, 340)
    coins = Coins(850, 600, 3)
    coins2 = Coins(1025, 350, 5)
    gumba = Monster_Gumba(860, 580, 50, 2)
    gumba2 = Monster_Gumba(720, 230, 50, 2)
    item_block1 = Item_Block(1750, 850, 1)

    air_tile = Air_tile(350, 300, 10)
    air_tile2 = Air_tile(1000, 300, 10)
    air_tile3 = Air_tile(600, 430, 7)
    air_tile4 = Air_tile(800, 550, 10)
    air_tile5 = Air_tile(1200, 550, 7)
    air_tile6 = Air_tile(660, 200, 10)

    air_tile7 = Air_tile(150, 300, 5)
    air_tile8 = Air_tile(1400, 650, 7)
    air_tile9 = Air_tile(1650, 750, 15)

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
    coins.update()
    coins2.update()

    if mario.x > 1920:
        game_framework.change_state(main_stage2_2)

    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    background2.draw()
    mario.draw()
    gumba.draw()
    gumba2.draw()
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
    air_tile8.draw()
    air_tile9.draw()

    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()


