from pico2d import *
import game_framework
import random

import game_framework
import title_state
import main_stage1_2
import main_stage2_1
import collision
import game_world
from mario import Mario
from item_block import Item_Block
from background import Background
from tiles import Tiles
from tiles_bottom import Tiles_bottom
from block import Block
from pipe import Pipe
from monster_gumba import Monster_Gumba
from coins import Coins

from castle import Castle
import server
# Game object class here

BOTTOM = 225

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

name = "main_stage1_3"


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            game_framework.change_state(main_stage2_1)
        else:
            server.mario.handle_event(event)

def enter():
    server.background = Background(960, 540)
    server.tiles = Tiles()
    server.tiles_bottom = Tiles_bottom()
    server.mario = Mario(200, 225)
    server.coins = [Coins(950 + 30 * i, 360) for i in range(5)]
    server.coins2 = [Coins(1190 + 30 * i, 270) for i in range(3)]
    server.item_block1 = Item_Block(300, 310, 1, 1)
    server.item_block2 = Item_Block(380, 310, 1, 1)
    server.item_block3 = Item_Block(460, 310, 1, 1)
    server.item_block4 = Item_Block(380, 430, 1, 4)
    server.item_block5 = Item_Block(1200, 420, 1, 1)
    server.block1 = Block(900, 310, 1)
    server.block2 = Block(950, 420, 4)
    server.block3 = Block(1200, 310, 2)
    server.block4 = Block(1180, 420, 1)
    server.block5 = Block(1232, 420, 1)
    server.gumba = Monster_Gumba(1000, 215, 100, 1)
    server.gumba2 = Monster_Gumba(380, 215, 50, 1)
    server.castle = Castle(1750, 275)

    game_world.add_object(server.background, 0)
    game_world.add_object(server.mario, 1)
    game_world.add_object(server.tiles, 1)
    game_world.add_object(server.tiles_bottom, 1)
    game_world.add_objects(server.coins, 1)
    game_world.add_objects(server.coins2, 1)
    game_world.add_object(server.item_block1, 1)
    game_world.add_object(server.item_block2, 1)
    game_world.add_object(server.item_block3, 1)
    game_world.add_object(server.item_block4, 1)
    game_world.add_object(server.item_block5, 1)
    game_world.add_object(server.block1, 1)
    game_world.add_object(server.block2, 1)
    game_world.add_object(server.block3, 1)
    game_world.add_object(server.block4, 1)
    game_world.add_object(server.block5, 1)
    game_world.add_object(server.gumba, 1)
    game_world.add_object(server.gumba2, 1)
    game_world.add_object(server.castle, 0)

    server.pipe = Pipe(111000, 225, 0)
    server.pipe2 = Pipe(111350, 285, 1)
    server.pipe3 = Pipe(111700, 330, 2)



    server.mario.velocity += RUN_SPEED_PPS

def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def update():

    if collision.collide(server.mario, server.castle):
        game_framework.change_state(main_stage2_1)

    # if server.mario.x > 1920:
    #     game_framework.change_state(main_stage2_1)

    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


