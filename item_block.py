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
    def __init__(self, x, y, l, type):
        self.image = load_image('OverWorld.png')
        self.image_item = load_image('items.png')
        self.x = x
        self.y = y
        self.l = l
        self.type = type        # 1: 코인 2: 초록 버섯 3: 빨간 버섯 4: 꽃
        self.collision = 0
        self.item = True
        self.frame = 0

        self.coin_sound = load_wav('coin_sound.wav')
        self.coin_sound.set_volume(10)

        self.dir = 1
        self.coin_y = self.y

        self.item_y = self.y

    def get_bb(self):
        return self.x - 11, self.y - 15, self.x + 6, self.y + 15

    def get_bb_head(self):
        return self.x - 11, self.y + 5, self.x + 6, self.y + 13

    def get_bb_foot(self):
        return self.x - 11, self.y - 13, self.x + 6, self.y - 11

    def get_bb_item(self):
        return self.x - 11, self.y + 12, self.x + 6, self.y + 32

    def draw(self):
        # draw_rectangle(*self.get_bb_head())
        # draw_rectangle(*self.get_bb_foot())
        draw_rectangle(*self.get_bb_item())
        k = 0
        if self.collision == 0:
            for i in range(self.l):
                self.image.clip_draw(64, 110, 20, 31, self.x + k, self.y)
                k += 17

        if self.collision == 1:
            self.image.clip_draw(31, 110, 17, 31, self.x + k - 2, self.y)

            if self.type == 1:
                if self.coin_y < self.y + 70:       # 동전 출현
                    self.image_item.clip_draw(0 + int(self.frame) * 15, 16, 15, 16, self.x + k - 3, self.coin_y)

            elif self.type == 2:        # 초록 버섯
                if self.item == True:
                    self.image_item.clip_draw(15, 30, 15, 16, self.x + k - 3, self.item_y)  # 초록 버섯 출현

            elif self.type == 3:        # 빨간 버섯
                if self.item == True:
                    self.image_item.clip_draw(0, 30, 15, 16, self.x + k - 3, self.item_y)

            elif self.type == 4:        # 꽃
                if self.item == True:
                    self.image_item.clip_draw(32, 30, 16, 18, self.x + k - 3, self.item_y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if collision.collide_foot_head(self, server.mario):
            self.collision = 1

        if self.collision == 1:
            self.coin_y += RUN_SPEED_PPS * self.dir
            if self.item_y < self.y + 22:
                self.item_y += (RUN_SPEED_PPS / 2) * self.dir

            if self.type == 1:
                if self.item == True:
                    server.mario.coin += 1
                    self.coin_sound.play()
                    self.item = False

            if self.type == 2:
                if collision.collide_item(self, server.mario):
                    if self.item == True:
                        server.mario.life += 1
                        self.item = False

            if self.type == 3:      # 빨간 버섯
                if collision.collide_item(self, server.mario):
                    if self.item == True:
                        server.mario.state = 2
                        self.item = False

            elif self.type == 4:      # 꽃
                if collision.collide_item(self, server.mario):
                    if self.item == True:
                        server.mario.state = 3
                        self.item = False