from pico2d import *

class Pipe:
    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    def draw(self):
        k = 0
        if self.l == 0: # pipe의 y가 225
            self.image.clip_draw(84, 97, 52, 50, self.x, self.y)
        elif self.l == 1:       # pipe의 y가 285
            self.image.clip_draw(84, 97, 52, 50, self.x, self.y)
            for i in range(4):
                self.image.clip_draw(84, 97, 52, 15, self.x, self.y - 33 - k)
                k += 15
        elif self.l == 2:       ## pipe의 y가 330
            self.image.clip_draw(84, 97, 52, 50, self.x, self.y)
            for i in range(7):
                self.image.clip_draw(84, 97, 52, 15, self.x, self.y - 33 - k)
                k += 15

    def update(self):
        pass