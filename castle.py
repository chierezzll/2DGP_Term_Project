from pico2d import *

class Castle:
    def __init__(self, x, y):
        self.image = load_image('Castle.png')
        self.x = x
        self.y = y

    def draw(self):
        self.image.draw(self.x, self.y, 150, 150)