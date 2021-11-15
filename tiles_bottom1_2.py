from pico2d import *

class Tiles_bottom:
    def __init__(self):
        self.image = load_image('tiles_007.png')
        self.x = 0
        self.y = 160

    def draw(self):
        k = 0

        for i in range(65):
            if k < 320 or 400 < k < 950 or k > 1040:
                 self.image.draw(k, 160)
                 self.image.draw(k, 130)
                 self.image.draw(k, 100)
                 self.image.draw(k, 70)
                 self.image.draw(k, 40)
            k += 30