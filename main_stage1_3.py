from pico2d import *
import game_framework
import random

import game_framework
import title_state
import main_stage1_2
import main_stage2_1

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
# Game object class here

BOTTOM = 225

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50.0
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
        else:
            mario.handle_event(event)

def enter():
    global background, tiles, tiles_bottom, mario, coins, item_block2, item_block1, item_block3, block1, block2, block3, block4, block5, gumba
    global gumba2, castle, item_block4, item_block5, coins2, fire
    background = Background(960, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario()
    coins = Coins(950, 470, 3)
    coins2 = Coins(1190, 270, 2)
    item_block1 = Item_Block(300, 310, 1)
    item_block2 = Item_Block(380, 310, 1)
    item_block3 = Item_Block(460, 310, 1)
    item_block4 = Item_Block(380, 430, 1)
    item_block5 = Item_Block(1200, 420, 2)
    block1 = Block(900, 310, 1)
    block2 = Block(950, 420, 4)
    block3 = Block(1200, 310, 2)
    block4 = Block(1180, 420, 1)
    block5 = Block(1232, 420, 1)
    gumba = Monster_Gumba(1000, 215, 100, 4)
    gumba2 = Monster_Gumba(380, 215, 50, 2)
    castle = Castle()

    mario.velocity += RUN_SPEED_PPS

def exit():
    global background, tiles, tiles_bottom, mario, coins, item_block2, item_block1, item_block3, block1, block2, block3, block4, block5, gumba
    global gumba2, castle, item_block4, item_block5, coins2, fire
    del(background)
    del(tiles)
    del(tiles_bottom)
    del(mario)
    del(coins)
    del(coins2)
    del(item_block1)
    del(item_block2)
    del(item_block3)
    del(item_block4)
    del(item_block5)
    del(block1)
    del(block2)
    del(block3)
    del(block4)
    del(block5)
    del(gumba)
    del(gumba2)
    del(castle)

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
        game_framework.change_state(main_stage2_1)

def draw():
    clear_canvas()
    background.draw()
    castle.draw()
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
    item_block4.draw()
    item_block5.draw()
    tiles.draw()
    tiles_bottom.draw()
    coins.draw()
    coins2.draw()

    update_canvas()
    delay(0.06)


