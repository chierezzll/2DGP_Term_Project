from pico2d import *

class Tiles_bottom:
    def __init__(self):
        self.image = load_image('tiles_007.png')

    def draw(self):
        k = 0

        for i in range(65):
            self.image.draw(k, 160)
            self.image.draw(k, 130)
            self.image.draw(k, 100)
            self.image.draw(k, 70)
            self.image.draw(k, 40)
            k += 30

    def update(self):
        pass