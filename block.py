from pico2d import *
import collision
import server
import mario
import game_world

class Block:
    BOY_X0, BOY_Y0 = -50, 60

    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    def get_bb(self):
        return self.x - 11, self.y - 15, self.x + 10, self.y + 15

    def get_bb_head(self):
        return self.x - 11, self.y + 5, self.x + 10 + 20 * (self.l - 1), self.y + 13

    def get_bb_foot(self):
        return self.x - 11, self.y - 13, self.x + 10 + 20 * (self.l - 1), self.y - 11

    def update(self):
        pass


    def draw(self):
        k = 0
        # draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_head())
        draw_rectangle(*self.get_bb_foot())
        for i in range(self.l):
            self.image.clip_draw(46, 110, 20, 31, self.x + k, self.y)
            k += 20
