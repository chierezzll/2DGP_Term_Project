from pico2d import *
import collision
import server

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Air_tile:
    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.x = x
        self.y = y
        self.l = l

    # def get_bb_2(self):
    #     return self.x - 2200, self.y - 10000, self.x + 10000, self.y - 547

    def get_bb_2(self, x = 0, y = 223):
        return x - 500,  y - 300, x + 5200, y - 25

    def get_bb_head(self):
        return self.x - 11, self.y + 5, self.x + 10 + 20 * (self.l - 1), self.y + 13

    def get_bb_foot(self):
        return self.x - 11, self.y - 13, self.x + 10 + 20 * (self.l - 1), self.y - 11


    def draw(self):
        k = 0
        draw_rectangle(*self.get_bb_2())
        draw_rectangle(*self.get_bb_head())
        draw_rectangle(*self.get_bb_foot())
        for i in range(self.l):
            self.image.clip_draw(29, 110, 20, 31, self.x + k, self.y)
            k += 20

    def update(self):
        if collision.collide_2(self, server.mario):
            server.mario.y -= RUN_SPEED_PPS / 200

            if server.mario.y < 10:
                server.mario.x = 50
                server.mario.y = 790