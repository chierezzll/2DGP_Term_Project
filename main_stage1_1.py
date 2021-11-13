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
from coins import Coins
# from fire import Fire
# Game object class here

BOTTOM = 225

name = "main_stage1_1"


# def handle_events():
#     global running
#     global mario
#     global fire
#
#     events = get_events()
#     for event in events:
#         if event.type == SDL_QUIT:
#             game_framework.quit()
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             game_framework.change_state(title_state)
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_INSERT:
#             game_framework.change_state(main_stage1_2)
#         elif event.type == SDL_KEYDOWN:     # 이동
#             if event.key == SDLK_RIGHT:
#                 mario.dir += 1
#                 mario.posx = 350
#                 mario.posy = 90
#             elif event.key == SDLK_LEFT:
#                 mario.dir -= 1
#                 mario.posx = 620
#                 mario.posy = 0
#             elif event.key == SDLK_SPACE:
#                 mario.isJump = 1
#             elif event.key == SDLK_a:
#                 if mario.dir != -1:
#                     fire.isSkill = 1
#                 else:
#                     fire.isSkill = -1
#             elif event.key == SDLK_DOWN:
#                 mario.posx = 620
#
#
#
#         elif event.type == SDL_KEYUP:
#             if event.key == SDLK_RIGHT:
#                 mario.dir -= 1
#                 mario.frame = 0
#                 mario.posx = 350
#             elif event.key == SDLK_LEFT:
#                 mario.dir += 1
#                 mario.frame = 0
#                 mario.posy = 0
#                 mario.posx = 750
#             elif event.key == SDLK_DOWN:
#                 mario.posx = 350

mario = None

def enter():
    global background, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block1, gumba, gumba2, pipe, pipe2, pipe3
    global fire
    background = Background(960, 540)
    tiles = Tiles()
    tiles_bottom = Tiles_bottom()
    mario = Mario()
    coins = Coins(580, 360, 3)
    coins2 = Coins(1450, 235, 7)
    item_block1 = Item_Block(450, 310, 1)
    item_block2 = Item_Block(620, 430, 1)
    block1 = Block(550, 310, 1)
    gumba = Monster_Gumba(600, 215, 100, 1)
    gumba2 = Monster_Gumba(1500, 215, 100, 1)
    # fire = Fire()
    pipe = Pipe(1000, 225, 0)
    pipe2 = Pipe(1350, 285, 1)
    pipe3 = Pipe(1700, 330, 2)

def exit():
    global background, tiles, tiles_bottom, mario, coins, coins2, item_block2, item_block1, block1, gumba, gumba2, pipe, pipe2, pipe3
    global fire
    del(background)
    del(tiles)
    del(tiles_bottom)
    del(mario)
    del(coins)
    del(coins2)
    del(item_block1)
    del(item_block2)
    del(block1)
    del(gumba)
    del(gumba2)
    # del(fire)
    del(pipe)
    del(pipe2)
    del(pipe3)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            mario.handle_event(event)







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
    # fire.update()
    if mario.x > 1920:
        game_framework.change_state(main_stage1_2)



def draw():
    clear_canvas()
    background.draw()
    mario.draw()
    gumba.draw()
    gumba2.draw()
    block1.draw()
    item_block1.draw()
    item_block2.draw()
    tiles.draw()
    tiles_bottom.draw()
    coins.draw()
    coins2.draw()
    pipe.draw()
    pipe2.draw()
    pipe3.draw()

    # fire.draw()

    update_canvas()
    delay(0.06)


