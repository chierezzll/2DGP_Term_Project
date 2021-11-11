from pico2d import *

class Coins:
    def __init__(self, x, y, l):
        self.image = load_image('items.png')
        self.frame = 0
        self.x = x
        self.y = y
        self.l = l

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        k = 0
        for i in range(self.l):
            self.image.clip_draw(0 + self.frame * 15, 16, 15, 16, self.x + k, self.y)
            k += 30