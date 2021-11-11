from pico2d import *

class Monster_Gumba:
    def __init__(self, x, y, d, num):
        self.image = load_image('Enemies.png')
        self.x = x
        self.y = y
        self.tx = x
        self.d = d  # 굼바 이동범위
        self.dir = 1
        self.num = num # 굼바 갯수
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += 3 * self.dir
        if self.x >= self.tx + self.d:
            self.dir = -1
        elif self.x <= self.tx - self.d:
            self.dir = 1

    def draw(self):
        k = 0
        for i in range(self.num):
            self.image.clip_draw(0 + self.frame * 30, 0, 30, 30, self.x + k, self.y)
            k += 30