from pico2d import *
import game_framework
import random
import game_framework
import title_state
import main_stage1_2

import game_world

from mario import Mario
from item_block import Item_Block
from background import Background
from tiles import Tiles
from tiles_bottom import Tiles_bottom
from block import Block
from pipe import Pipe
from monster_gumba import Monster_Gumba
from monster_turtle import Monster_Turtle
from coins import Coins
from fire import Fire
from air_tile import Air_tile
from boss import Boss

import server
# Game object class here

BOTTOM = 225

name = "main_stage1_1"

def enter():
    server.background = Background(960, 540)
    server.tiles = Tiles()
    server.tiles_bottom = Tiles_bottom()
    server.mario = Mario(200, 225)
    server.coins = [Coins(580 + 30 * i, 360) for i in range(3)]
    server.coins2 = [Coins(1450 + 30 * i, 235) for i in range(7)]
    server.item_block1 = Item_Block(450, 310, 1, 1)
    server.item_block2 = Item_Block(620, 430, 1, 3)
    server.block1 = Block(550, 310, 1)
    server.gumba = Monster_Gumba(600, 215, 100, 1)
    server.gumba2 = Monster_Gumba(1500, 215, 100, 1)
    server.pipe = Pipe(1000, 225, 0)
    server.pipe2 = Pipe(1350, 285, 1)
    server.pipe3 = Pipe(1700, 330, 2)

    game_world.add_object(server.background, 0)
    game_world.add_object(server.mario, 1)
    game_world.add_object(server.tiles, 1)
    game_world.add_object(server.tiles_bottom, 1)
    game_world.add_object(server.item_block1, 1)
    game_world.add_object(server.item_block2, 1)
    game_world.add_object(server.gumba, 1)
    game_world.add_object(server.gumba2, 1)
    game_world.add_object(server.pipe, 1)
    game_world.add_object(server.pipe2, 1)
    game_world.add_object(server.pipe3, 1)
    game_world.add_object(server.block1, 1)

    game_world.add_objects(server.coins, 1)
    game_world.add_objects(server.coins2, 1)

    server.block2 = Block(18210, 450, 8)
    server.block3 = Block(11050, 450, 4)
    server.block4 = Block(11131, 310, 1)
    server.block5 = Block(11300, 310, 1)
    server.item_block3 = Item_Block(11460, 310, 1, 1)
    server.item_block4 = Item_Block(31180, 430, 1, 1)
    server.item_block5 = Item_Block(111200, 420, 2, 1)

    server.air_tile = Air_tile(11350, 300, 10)
    server.air_tile2 = Air_tile(101100, 300, 10)
    server.air_tile3 = Air_tile(61100, 430, 7)
    server.air_tile4 = Air_tile(81100, 550, 10)
    server.air_tile5 = Air_tile(111200, 550, 7)
    server.air_tile6 = Air_tile(61160, 200, 10)
    server.air_tile7 = Air_tile(11150, 300, 5)
    server.air_tile8 = Air_tile(111400, 650, 7)
    server.air_tile9 = Air_tile(111650, 750, 15)
    server.turtle = Monster_Turtle(31160, 620, 100, 1)
    server.turtle2 = Monster_Turtle(11990, 220, 120, 1)
    server.turtle3 = Monster_Turtle(11990, 220, 120, 1)
    server.gumba3 = Monster_Gumba(22600, 215, 100, 1)
    server.gumba4 = Monster_Gumba(122500, 215, 100, 1)

    server.boss = Boss(122500, 215, 100, 1)

def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_w:
            game_framework.change_state(main_stage1_2)
        else:
            server.mario.handle_event(event)


def pause():
    pass

def resume():
    pass

def update():
    if server.mario.x > 1920:
        game_framework.change_state(main_stage1_2)

    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()

    for game_object in game_world.all_objects():
        game_object.draw()


    update_canvas()


