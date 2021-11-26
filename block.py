from pico2d import *

class Block:
    BOY_X0, BOY_Y0 = -50, 60

    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    def get_bb(self):
        return self.x - 12, self.y - 15, self.x + 10, self.y + 15


    def draw(self):
        k = 0
        draw_rectangle(*self.get_bb())
        for i in range(self.l):
            self.image.clip_draw(46, 110, 20, 31, self.x + k, self.y)
            k += 20