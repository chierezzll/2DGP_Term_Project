from pico2d import *
from mario import Mario

class Fire:
    global mario

    def __init__(self):
        self.image = load_image('fire.png')
        self.frame = 0
        self.x = 0
        self.isSkill = 0
        self.firebeg = 0
        self.firebegy= 0

    def update(self):
        self.frame = (self.frame + 1) % 3
        if self.isSkill > 0:
            self.x += 45
            if self.x > 300:
                self.x = 0
                self.isSkill = 0

        elif self.isSkill < 0:
            self.x -= 45
            if self.x < -300:
                self.x = 0
                self.isSkill = 0

        elif self.isSkill == 0:
            self.firebeg = mario.x
            self.firebegy = mario.y



    def skill(self, j):
        self.isSkill = j

    def draw(self):
        if self.isSkill > 0:
            self.image.clip_draw(0 + self.frame * 17, 80, 15, 15, self.firebeg + self.x, self.firebegy, 25, 25)
        elif self.isSkill < 0:
            self.image.clip_draw(0 + self.frame * 17, 80, 15, 15, self.firebeg + self.x, self.firebegy, 25, 25)