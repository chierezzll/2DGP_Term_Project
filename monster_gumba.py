from pico2d import *
import game_framework
import server
import collision
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 0.03
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

TOP = 900

class Monster_Gumba:
    def __init__(self, x, y, d, num):
        self.image = load_image('Enemies.png')
        self.x = x
        self.y = y
        self.tx = x
        self.d = d  # 굼바 이동범위
        self.dir = 1
        self.num = num # 굼바 갯수
        self.frame = 0

        self.collision = 0
        self.y2 = self.y

        self.parent = None

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 20, self.y + 15

    def get_bb_head(self):
        return self.x - 15, self.y + 10, self.x + 20, self.y + 15

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x += RUN_SPEED_PPS * self.dir

        if self.collision == 0:
            if self.x >= self.tx + self.d:
                self.dir = -1
            elif self.x <= self.tx - self.d:
                self.dir = 1


        if collision.collide_head_foot(self, server.mario):
            self.collision = 1

        if self.collision == 1:
            self.y2 -= RUN_SPEED_PPS
            if self.y2 < self.y - 50:
                game_world.remove_object(self)

        if collision.collide(self, server.mario):
            self.set_parent(server.mario)
            if self.x > server.mario.x + 20 or self.x < server.mario.x - 20:
                self.parent = None
            if self.parent == server.mario:
                server.state -= 0.005
            if server.state < 1:
                server.state = 1
                server.life -= 1
                server.mario.x = 50
                server.mario.y = TOP
        if 50 < server.mario.x < 60:
            server.mario.y -= RUN_SPEED_PPS * 3


    def draw(self):
        k = 0
        #draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_head())
        if self.collision == 0:
            for i in range(self.num):
                self.image.clip_draw(0 + int(self.frame) * 30, 0, 30, 30, self.x + k, self.y + 10, 50, 50)
                k += 30
        elif self.collision == 1:
            self.image.clip_draw(60, 0, 30, 30, self.x, self.y2 + 10 , 50, 50)

    def set_parent(self, mario):
        self.parent = mario

