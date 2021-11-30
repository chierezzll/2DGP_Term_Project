from pico2d import *
import game_framework
import game_world
from fire import Fire
import server
import collision
BOTTOM = 225

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

JUMP_SPEED_MPS = 0.3
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

GRAVITY_MPS = -1.0
GRAVITY_PPS = GRAVITY_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, JUMP_FINISH, Z = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_z): Z,
}

class IdleState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS

    def exit(mario, event):
        if event == Z:
            mario.skill()

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8


    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(350, 90, 40, 90, mario.x, mario.y, 50, 50)
        else:
            mario.image.clip_draw(750 - 5, 0, 40, 90, mario.x, mario.y, 50, 50)

class RunState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
         if event == Z:
            mario.skill()

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1950)


    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(350 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
        else:
            mario.image.clip_draw(615 - 5 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)


class JumpState:
    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)

        mario.jump = True

    def exit(mario, event):
        if event == Z:
            mario.skill()

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1950)

        if mario.jump == True:
            mario.jumptime += game_framework.frame_time
            mario.y += JUMP_SPEED_PPS * mario.jumptime + (GRAVITY_PPS * mario.jumptime ** 2 / 2)

        if mario.y <= BOTTOM:
            mario.y = BOTTOM
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.block1):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)





    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(350 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
        else:
            mario.image.clip_draw(615 - 5 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: JumpState, Z: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE: JumpState, JUMP_FINISH: IdleState, Z: RunState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState, SPACE: JumpState, JUMP_FINISH: RunState, Z: JumpState}
}

class Mario:
    def __init__(self, x, y):
        self.image = load_image('mario_sheet.png')
        self.image_heart = load_image('heart.png')
        self.image_coin = load_image('coin_score.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.posx = 350
        self.posy = 90

        self.font = load_font('ENCR10B.TTF', 40)

        self.jumptime = 0
        self.jump = False

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.parent = None

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        return self.x - 15, self.y - 27, self.x + 15, self.y + 27

    def get_bb_foot(self):
        return self.x - 12, self.y - 27, self.x + 15, self.y - 17

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if collision.collide_foot_head(self, server.block1):
            self.set_parent(server.block1)
            self.y = server.block1.y + 40

            print("collision")
            if self.x > server.block1.x + 20 or self.x < server.block1.x - 20:
                self.parent = None




    def skill(self):
        fire = Fire(self.x, self.y, self.dir)
        game_world.add_object(fire, 1)

    def fall(self):
        self.y -= GRAVITY_PPS * game_framework.frame_time


    def draw(self):
        self.cur_state.draw(self)
        #draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_foot())
        debug_print('Parent :' + str(self.parent) + ' Dir:' + str(self.dir) + '  State:' + str(self.cur_state) + ' mario.y : ' + str(self.y))

        self.image_heart.draw(50, 1000, 70, 70)
        self.font.draw(100, 990, 'x 5', (0, 0, 0))

        self.image_coin.draw(300, 1000, 60, 60)
        self.font.draw(350, 990, 'x 0', (0, 0, 0))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def set_parent(self, block):
        self.parent = block




