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
from air_tile import Air_tile
from monster_gumba import Monster_Gumba
from monster_turtle import Monster_Turtle
from coins import Coins
from boss import Boss

import server
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
            server.mario.handle_event(event)

def enter():
    server.background3 = Background(960, 540)
    server.tiles = Tiles()
    server.tiles_bottom = Tiles_bottom()
    server.mario = Mario(200, 225)
    server.boss = Boss(1100, 240, random.randint(100, 200), 1)

    game_world.add_object(server.background3, 0)
    game_world.add_object(server.mario, 1)
    game_world.add_object(server.tiles, 1)
    game_world.add_object(server.tiles_bottom, 1)
    game_world.add_object(server.boss, 1)

    server.mario.velocity += RUN_SPEED_PPS

    server.block1 = Block(18210, 450, 8)
    server.block2 = Block(18210, 450, 8)
    server.block3 = Block(11050, 450, 4)
    server.block4 = Block(11131, 310, 1)
    server.block5 = Block(11300, 310, 1)
    server.item_block1 = Item_Block(11460, 310, 1, 1)
    server.item_block2 = Item_Block(11460, 310, 1, 1)
    server.item_block3 = Item_Block(11460, 310, 1, 1)
    server.item_block4 = Item_Block(31180, 430, 1, 1)
    server.item_block5 = Item_Block(111200, 420, 2, 1)
    server.pipe = Pipe(111000, 225, 0)
    server.pipe2 = Pipe(111350, 285, 1)
    server.pipe3 = Pipe(111700, 330, 2)
    server.air_tile2 = Air_tile(41100, 300, 7)
    server.air_tile3 = Air_tile(41150, 420, 2)
    server.air_tile4 = Air_tile(61110, 530, 10)
    server.air_tile5 = Air_tile(91110, 420, 2)
    server.air_tile6 = Air_tile(11100, 500, 6)
    server.air_tile7 = Air_tile(11370, 200, 5)
    server.air_tile8 = Air_tile(16100, 550, 18)
    server.air_tile9 = Air_tile(16100, 550, 18)
    server.turtle = Monster_Turtle(31160, 620, 100, 1)
    server.turtle2 = Monster_Turtle(91190, 220, 120, 1)
    server.gumba = Monster_Gumba(60110, 215, 50, 1)
    server.gumba2 = Monster_Gumba(151100, 215, 70, 1)
    server.gumba3 = Monster_Gumba(80110, 215, 90, 1)
    server.gumba4 = Monster_Gumba(131100, 215, 50, 1)

def exit():
    game_world.clear()


def pause():
    pass

def resume():
    pass

def update():

    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


