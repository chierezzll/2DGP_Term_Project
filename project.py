from pico2d import *
import random
# Game object class here

class Grass:
    def __init__(self): # 생성자
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(960, 540)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = random.randint(0, 7)

    def update(self): # 소년의 행위 구현
        self.x += 5 # 속성값을 바꿈으로써, 행위(오른쪽으로 이동) 구현
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame* 100, 0, 100, 100, self.x, self.y)

class Mario:

    def __init__(self):
        self.image = load_image('mario_sheet.png')
        self.x = 300
        self.y = 400
        self.dir = 0
        self.frame = 350
        self.width = 40

    def update(self):
        self.frame = (self.frame + 1 ) % 4
        self.x += 5 * self.dir


    def draw(self):
        self.image.clip_draw(350 + self.frame * 45 , 90, 40, 90, self.x, self.y)          # 350, 400, 450, 500

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
            elif event.key ==SDLK_LEFT:
                mario.dir -= 1

        elif event.type == SDL_KEYUP:
            if event.key ==SDLK_RIGHT:
                mario.dir -= 1
            elif event.key ==SDLK_LEFT:
                mario.dir += 1


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

