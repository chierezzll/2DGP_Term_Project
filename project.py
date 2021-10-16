from pico2d import *
import random
# Game object class here

BOTTOM = 400

class Grass:
    def __init__(self): # 생성자
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(960, 540)

class Mario:

    def __init__(self):
        self.image = load_image('mario_sheet.png')
        self.x = 300
        self.y = 400
        self.dir = 0
        self.frame = 0
        self.posx = 350
        self.posy = 90
        self.isJump = 0
        self.v = 6
        self.m = 2
        self.f = 0

    def update(self):
        self.frame = (self.frame + 1 ) % 4
        self.x += 5 * self.dir
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
                self.v = 6



    def draw(self):
        self.image.clip_draw(self.posx + self.frame * 45 , self.posy, 40, 90, self.x, self.y)          # 350, 400, 450, 500

    def jump(self, j):
        self.isJump = j


def handle_events():
    global running
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                mario.dir += 1
                mario.posx = 350
                mario.posy = 90
            elif event.key ==SDLK_LEFT:
                mario.dir -= 1
                mario.posx = 620
                mario.posy = 0
            elif event.key == SDLK_SPACE:
                mario.isJump = 1


        elif event.type == SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                mario.dir -= 1
                mario.frame = 0
            elif event.key ==SDLK_LEFT:
                mario.dir += 1
                mario.frame = 0


# initialization code

open_canvas(1920, 1080)

grass = Grass()
mario = Mario()
running = True



# game main loop code

while running:

    handle_events() # 키 입력 받아들이는 처리..

    # Game logic
    mario.update()

    # Game drawing
    clear_canvas()
    grass.draw()
    mario.draw()

    update_canvas()

    delay(0.05)

# finalization code

