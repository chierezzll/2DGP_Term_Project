from pico2d import *
import server

class Background:
    global mario

    def __init__(self, x, y): # 생성자
        self.image = load_image('background.png')
        self.x = x
        self.y = y


    def draw(self):
        self.image.clip_draw(0, 0, 1920, 1080, self.x, self.y)
        self.image.clip_draw(0, 0, 1920, 1080, self.x + 1920, self.y)

    def update(self):
        pass