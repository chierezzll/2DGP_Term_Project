from pico2d import *

class Tiles:
    def __init__(self):
        self.image = load_image('tiles_001.png')
        self.y = 200

    def draw(self):
        k = 0
        for i in range(23):
            self.image.clip_draw(0, 10, 95, 100, 0 + k, self.y - 50)
            k += 90

    def update(self):
        pass