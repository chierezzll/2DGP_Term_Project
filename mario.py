from pico2d import *
import game_framework

BOTTOM = 225

class Mario:
    global item_block1
    def __init__(self):
        self.image = load_image('mario_sheet.png')
        self.x = 200
        self.y = 225
        self.dir = 0
        self.frame = 0
        self.posx = 350
        self.posy = 90
        self.isJump = 0
        self.v = 7
        self.m = 2
        self.f = 0

    def update(self):
        self.frame = (self.frame + 1 ) % 4
        self.x += 10 * self.dir     #마리오 이동속도
        if self.isJump > 0:
            if self.v > 0:
                # 속도가 0보다 클때는 위로 올라감
                self.f = (0.5 * self.m * (self.v * self.v))
            else:
                # 속도가 0보다 작을때는 아래로 내려감
                self.f = -(0.5 * self.m * (self.v * self.v))

            self.y += self.f
            self.v -= 1
            if self.y == BOTTOM:
                self.isJump = 0
                self.v = 7

    def draw(self):
        if self.dir != 0:
            self.image.clip_draw(self.posx + self.frame * 45 , self.posy, 40, 90, self.x, self.y, 50, 50)          # 350, 400, 450, 500
        else:
            self.image.clip_draw(self.posx , self.posy, 40, 90, self.x, self.y, 50, 50)


    def jump(self, j):
        self.isJump = j

