from pico2d import *

class Castle:
    def __init__(self, x, y):
        self.image = load_image('Castle.png')
        self.x = x
        self.y = y

    def get_bb(self):
        return self.x - 5, self.y - 80, self.x + 8, self.y - 3

    def draw(self):
        #draw_rectangle(*self.get_bb())
        self.image.draw(self.x, self.y, 150, 150)

    def update(self):
        pass