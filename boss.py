from pico2d import *
import game_framework
import game_world
from boss_fire import Fire, Fire_ball
import random
import time

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 0.03
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Boss:
    def __init__(self, x, y, d, num):
        self.image = load_image('boss.png')
        self.x = x
        self.y = y
        self.tx = x
        self.d = d  # 이동범위
        self.dir = 1
        self.num = num # 갯수
        self.frame = 0

        self.time = 300         # 직선 불

        self.time2 = 1500        # 곡선 불

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += RUN_SPEED_PPS * self.dir
        if self.x >= self.tx + self.d:
            self.dir = -1
        elif self.x <= self.tx - self.d:
            self.dir = 1

        self.time -= 1
        self.time2 -= 1
        if self.time == 0:
            self.skill()
            self.time = random.randint(100, 1000)

        if self.time2 == 0:
            self.skill_ball()
            self.time2 = random.randint(1000, 2000)



    def skill(self):
        fire = Fire(self.x, self.y, self.dir)
        game_world.add_object(fire, 1)

    def skill_ball(self):
        fire = Fire_ball(self.x, self.y, self.dir)
        game_world.add_object(fire, 1)

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(0 + int(self.frame) * 80, 30, 80, 80, self.x, self.y, 110, 110)
        else:
            self.image.clip_draw(0 + int(self.frame) * 80, 140, 80, 80, self.x, self.y, 110, 110)
