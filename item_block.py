from pico2d import *

class Item_Block():
    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    def get_bb(self):
        return self.x - 11, self.y - 15, self.x + 6, self.y + 15

    def get_bb_head(self):
        return self.x - 11, self.y + 5, self.x + 6, self.y + 13

    def get_bb_foot(self):
        return self.x - 11, self.y - 13, self.x + 6, self.y - 11

    def draw(self):
        draw_rectangle(*self.get_bb_head())
        draw_rectangle(*self.get_bb_foot())
        k = 0
        for i in range(self.l):
            self.image.clip_draw(64, 110, 20, 31, self.x + k, self.y)
            k += 17

    def update(self):
        pass