from pico2d import *

class Item_Block():
    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    def draw(self):
        k = 0
        for i in range(self.l):
            self.image.clip_draw(64, 110, 20, 31, self.x + k, self.y)
            k += 17

    def update(self):
        pass