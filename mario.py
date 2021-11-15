from pico2d import *
import game_framework
import game_world
from fire import Fire

BOTTOM = 225

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0
ACTION_PER_TIME = 0
FRAMES_PER_ACTION = 0

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
            mario.image.clip_draw(750, 0, 40, 90, mario.x, mario.y, 50, 50)

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
        mario.frame = (mario.frame + 1) % 4
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1950)


    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(350 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
        else:
            mario.image.clip_draw(615 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)


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

    def exit(mario, event):
        if event == Z:
            mario.skill()

    def do(mario):
        mario.frame = (mario.frame + 1) % 4
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1950)

        if mario.v > 0:
            # 속도가 0보다 클때는 위로 올라감
            mario.f = (0.5 * mario.m * (mario.v * mario.v))
        else:
            # 속도가 0보다 작을때는 아래로 내려감
            mario.f = -(0.5 * mario.m * (mario.v * mario.v))

        mario.y += mario.f
        mario.v -= 1
        if mario.y <= BOTTOM:
            mario.v = 7
            mario.isJump = 0
            mario.add_event(JUMP_FINISH)

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(350 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
        else:
            mario.image.clip_draw(615 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: JumpState, Z: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE: JumpState, JUMP_FINISH: IdleState, Z: RunState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState, SPACE: JumpState, JUMP_FINISH: RunState, Z: JumpState}
}

class Mario:
    def __init__(self, x, y):
        self.image = load_image('mario_sheet.png')
        self.x = x
        self.y = y
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.posx = 350
        self.posy = 90

        self.isJump = 0
        self.v = 7
        self.m = 2
        self.f = 0

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def skill(self):
        fire = Fire(self.x, self.y, self.dir*30)
        game_world.add_object(fire, 1)


    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir) + '  State:' + str(self.cur_state))

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)




