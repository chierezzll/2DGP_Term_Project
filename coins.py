from pico2d import *
import game_framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Coins:
    def __init__(self, x, y, l):
        self.image = load_image('items.png')
        self.frame = 0
        self.x = x
        self.y = y
        self.l = l

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        k = 0
        for i in range(self.l):
            self.image.clip_draw(0 + int(self.frame) * 15, 16, 15, 16, self.x + k, self.y)
            k += 30