from pico2d import *

class Castle:
    def __init__(self):
        self.image = load_image('Castle.png')

    def draw(self):
        self.image.draw(1750, 240)