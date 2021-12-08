from pico2d import *
import game_world
import game_framework
import collision
import server

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

RUN_SPEED_KMPH2 = 20.0
RUN_SPEED_MPM2 = (RUN_SPEED_KMPH2 * 1000 / 60.0)
RUN_SPEED_MPS2 = (RUN_SPEED_MPM2 / 60.0)
RUN_SPEED_PPS2 = (RUN_SPEED_MPS2 * PIXEL_PER_METER)


JUMP_SPEED_PPS = RUN_SPEED_PPS * 0.5

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

BOTTOM = 225

class Fire:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        self.frame = 0
        if Fire.image == None:
            Fire.image = load_image('boss.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 16, self.y - 12, self.x + 26, self.y + 5


    def draw(self):
        draw_rectangle(*self.get_bb())
        if self.velocity > 0:
            #self.image.clip_draw(90 + int(self.frame) * 90, 0, 90, 40, self.x, self.y)
            self.image.clip_draw(70 + int(self.frame) * 90, 110, 80, 40, self.x, self.y)
        else:
            #self.image.clip_draw(90 + int(self.frame) * 90, 100, 90, 40, self.x, self.y)
            self.image.clip_draw(90 + int(self.frame) * 90, 0, 90, 40, self.x, self.y)

    def update(self):
        self.x += RUN_SPEED_PPS * game_framework.frame_time * self.velocity
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 1

        if self.x < 25 or self.x > 1920 - 25:
            game_world.remove_object(self)

        if collision.collide(self, server.mario):
            game_world.remove_object(self)
            server.state -= 1
            if server.state < 1:
                server.state = 1
                server.life -= 1
                server.mario.x = 200
                server.mario.y = 225

class Fire_ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):
        self.frame = 0
        self.v = 10.0
        if Fire_ball.image == None:
            Fire_ball.image = load_image('fire.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 15, self.y - 12, self.x + 8, self.y + 13

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 17, 80, 15, 15, self.x, self.y, 25, 25)

    def update(self):
        self.x += RUN_SPEED_PPS2 * game_framework.frame_time * self.velocity
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        if self.v > 0:
            self.y += JUMP_SPEED_PPS * game_framework.frame_time
        elif self.v < 0:
            self.y -= JUMP_SPEED_PPS * game_framework.frame_time

        self.v -= 0.1

        if collision.collide(self, server.mario):
            game_world.remove_object(self)
            server.state -= 1
            if server.state < 1:
                server.state = 1
                server.life -= 1
                server.mario.x = 200
                server.mario.y = 225

        if self.y <= BOTTOM:
            self.v = 9.0
            self.y = BOTTOM

        if self.x < 25 or self.x > 1920 - 25:
            game_world.remove_object(self)
