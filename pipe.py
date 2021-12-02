from pico2d import *
import server
import collision

class Pipe:
    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    def get_bb(self):
        return self.x - 11, self.y - 200, self.x + 23, self.y + 10

    def get_bb_head(self):
        return self.x - 11, self.y + 15, self.x + 23, self.y + 25

    def draw(self):
        k = 0
        #draw_rectangle(*self.get_bb_head())
        draw_rectangle(*self.get_bb())
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
        if collision.collide(self, server.mario):
            if server.mario.x < self.x:
                server.mario.x = self.x - 30
            else:
                server.mario.x = self.x + 40