from pico2d import *
import game_framework
import game_world
import server
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Coins:
    def __init__(self, x, y):
        self.image = load_image('items.png')

        self.frame = 0
        self.x = x
        self.y = y

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        self.image.clip_draw(0 + int(self.frame) * 15, 16, 15, 16, self.x, self.y)

