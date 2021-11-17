from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 0.03
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Monster_Turtle:
    def __init__(self, x, y, d, num):
        self.image = load_image('Enemies.png')
        self.x = x
        self.y = y
        self.ty = y
        self.d = d  # 이동범위
        self.dir = 1
        self.num = num  # 갯수
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.y += RUN_SPEED_PPS * self.dir
        if self.y >= self.ty + self.d:
            self.dir = -1
        elif self.y <= self.ty - self.d:
            self.dir = 1

    def draw(self):
        k = 0
        for i in range(self.num):
            self.image.clip_draw(480 + int(self.frame) * 30, 0, 30, 30, self.x + k, self.y)
            k += 30