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

JUMP_SPEED_PPS = RUN_SPEED_PPS * 2

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

BOTTOM = 225

class Fire:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        self.frame = 0
        self.v = 2
        self.count = 0
        self.dir = 1
        if Fire.image == None:
            Fire.image = load_image('fire.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 15, self.y - 22, self.x + 8, self.y - 3

    def draw(self):
        draw_rectangle(*self.get_bb())
        self.image.clip_draw(int(self.frame) * 17, 80, 15, 15, self.x, self.y - 15, 25, 25)

    def update(self):
        self.x += RUN_SPEED_PPS * game_framework.frame_time * self.velocity * 0.7
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3

        if self.v > 0:
            self.y += JUMP_SPEED_PPS * game_framework.frame_time * 0.4
        elif self.v < 0:
            self.y -= JUMP_SPEED_PPS * game_framework.frame_time * 0.4

        self.v -= 0.1

        if self.y <= BOTTOM:
            self.v = 2.0
            self.y = BOTTOM

        if self.x < 25 or self.x > 1920 - 25:
            game_world.remove_object(self)

        if collision.collide(self, server.pipe):
            game_world.remove_object(self)
        if collision.collide(self, server.pipe2):
            game_world.remove_object(self)
        if collision.collide(self, server.pipe3):
            game_world.remove_object(self)

        if collision.collide(self, server.gumba):
            game_world.remove_object(self)
            game_world.remove_object(server.gumba)
        if collision.collide(self, server.gumba2):
            game_world.remove_object(self)
            game_world.remove_object(server.gumba2)
        if collision.collide(self, server.gumba3):
            game_world.remove_object(self)
            game_world.remove_object(server.gumba3)
        if collision.collide(self, server.gumba4):
            game_world.remove_object(self)
            game_world.remove_object(server.gumba4)

        if collision.collide(self, server.turtle):
            game_world.remove_object(self)
            game_world.remove_object(server.turtle)
        if collision.collide(self, server.turtle2):
            game_world.remove_object(self)
            game_world.remove_object(server.turtle2)
        if collision.collide(self, server.turtle3):
            game_world.remove_object(self)
            game_world.remove_object(server.turtle3)