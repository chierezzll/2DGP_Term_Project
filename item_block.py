from pico2d import *
import server
import collision
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 0.15
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Item_Block():
    def __init__(self, x, y, l):
        self.image = load_image('OverWorld.png')
        self.image_coin = load_image('items.png')
        self.x = x
        self.y = y
        self.l = l
        self.collision = 0
        self.frame = 0

        self.dir = 1
        self.coin_y = self.y

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
        if self.collision == 0:
            for i in range(self.l):
                self.image.clip_draw(64, 110, 20, 31, self.x + k, self.y)
                k += 17

        if self.collision == 1:     # 동전 출현
            self.image.clip_draw(31, 110, 17, 31, self.x + k - 2, self.y)
            if self.coin_y < self.y + 70:
                self.image_coin.clip_draw(0 + int(self.frame) * 15, 16, 15, 16, self.x + k - 3, self.coin_y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if collision.collide_foot_head(self, server.mario):
            self.collision = 1

        if self.collision == 1:
            self.coin_y += RUN_SPEED_PPS * self.dir