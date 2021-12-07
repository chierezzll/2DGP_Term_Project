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

import server

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            game_framework.change_state(main_stage2_2)
        else:
            server.mario.handle_event(event)

def enter():
    server.background2 = Background(960, 540)
    server.mario = Mario(170, 340)
    server.coins = [Coins(850 + 30 * i, 600) for i in range(3)]
    server.coins2 = [Coins(1025 + 30 * i, 350) for i in range(5)]
    server.gumba = Monster_Gumba(860, 580, 50, 2)
    server.gumba2 = Monster_Gumba(720, 230, 50, 2)
    server.item_block1 = Item_Block(11750, 850, 1, 1)

    server.air_tile = Air_tile(350, 300, 10)
    server.air_tile2 = Air_tile(1000, 300, 10)
    server.air_tile3 = Air_tile(600, 430, 7)
    server.air_tile4 = Air_tile(800, 550, 10)
    server.air_tile5 = Air_tile(1150, 550, 7)
    server.air_tile6 = Air_tile(660, 200, 10)

    server.air_tile7 = Air_tile(150, 300, 5)
    server.air_tile8 = Air_tile(1400, 650, 7)
    server.air_tile9 = Air_tile(1650, 750, 15)

    game_world.add_object(server.background2, 0)
    game_world.add_object(server.mario, 1)
    game_world.add_objects(server.coins, 1)
    game_world.add_objects(server.coins2, 1)
    game_world.add_object(server.item_block1, 1)
    game_world.add_object(server.air_tile, 1)
    game_world.add_object(server.air_tile2, 1)
    game_world.add_object(server.air_tile3, 1)
    game_world.add_object(server.air_tile4, 1)
    game_world.add_object(server.air_tile5, 1)
    game_world.add_object(server.air_tile6, 1)
    game_world.add_object(server.air_tile7, 1)
    game_world.add_object(server.air_tile8, 1)
    game_world.add_object(server.air_tile9, 1)
    game_world.add_object(server.gumba, 1)
    game_world.add_object(server.gumba2, 1)

    server.mario.velocity += RUN_SPEED_PPS

    server.block1 = Block(18210, 450, 8)
    server.block2 = Block(18210, 450, 8)
    server.block3 = Block(11050, 450, 4)
    server.block4 = Block(11131, 310, 1)
    server.block5 = Block(11300, 310, 1)
    server.item_block2 = Item_Block(11460, 310, 1, 1)
    server.item_block3 = Item_Block(11460, 310, 1, 1)
    server.item_block4 = Item_Block(31180, 430, 1, 1)
    server.item_block5 = Item_Block(111200, 420, 2, 1)
    server.pipe = Pipe(111000, 225, 0)
    server.pipe2 = Pipe(111350, 285, 1)
    server.pipe3 = Pipe(111700, 330, 2)


def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def update():
    if server.mario.x > 1920:
        game_framework.change_state(main_stage2_2)

    for game_object in game_world.all_objects():
        game_object.update()

def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()


