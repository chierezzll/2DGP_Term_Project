from pico2d import *

class Air_tile:
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


    def draw(self):
        k = 0
        draw_rectangle(*self.get_bb_head())
        draw_rectangle(*self.get_bb_foot())
        for i in range(self.l):
            self.image.clip_draw(29, 110, 20, 31, self.x + k, self.y)
            k += 20

    def update(self):
        pass