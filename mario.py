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

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, JUMP_FINISH, Z, O = range(8)

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
        if mario.state == 1:        # 작은 마리오
            if mario.dir == 1:
                mario.image.clip_draw(0, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(1005, 0, 40, 90, mario.x, mario.y, 50, 50)

        elif mario.state == 2:      # 큰 마리오
            if mario.dir == 1:
                mario.image.clip_draw(350, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(750 - 5, 0, 40, 90, mario.x, mario.y, 50, 50)

        elif mario.state == 3:      # 꽃 마리오
            if mario.dir == 1:
                mario.image.clip_draw(745, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(350, 0, 40, 90, mario.x, mario.y, 50, 50)

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
        if mario.state == 1:
            if mario.dir == 1:
                mario.image.clip_draw(0 + int(mario.frame) * 45, 90, 38, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(960 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

        elif mario.state == 2:
            if mario.dir == 1:
                mario.image.clip_draw(350 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(615 - 5 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

        elif mario.state == 3:      # 꽃 마리오
            if mario.dir == 1:
                mario.image.clip_draw(744 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(217 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)


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

        if collision.collide_foot_head(mario, server.block2):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.block3):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.block4):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.block5):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile2):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile3):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile4):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile5):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile6):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile7):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile8):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.air_tile9):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.item_block1):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.item_block2):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.item_block3):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.item_block4):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.item_block5):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

        if collision.collide_foot_head(mario, server.pipe):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)
        if collision.collide_foot_head(mario, server.pipe2):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)
        if collision.collide_foot_head(mario, server.pipe3):
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)


        if collision.collide_foot_head(mario, server.gumba):
            mario.jumptime = 0.005
        if collision.collide_foot_head(mario, server.gumba2):
            mario.jumptime = 0.005
        if collision.collide_foot_head(mario, server.gumba3):
            mario.jumptime = 0.005
        if collision.collide_foot_head(mario, server.gumba4):
            mario.jumptime = 0.005

        if collision.collide_foot_head(mario, server.turtle):
            mario.jumptime = 0.005
        if collision.collide_foot_head(mario, server.turtle2):
            mario.jumptime = 0.005
        if collision.collide_foot_head(mario, server.turtle3):
            mario.jumptime = 0.005


    def draw(mario):
        if mario.state == 1:
            if mario.dir == 1:
                mario.image.clip_draw(0 + int(mario.frame) * 45, 90, 38, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(960 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)
        elif mario.state == 2:
            if mario.dir == 1:
                mario.image.clip_draw(350 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(615 - 5 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

        elif mario.state == 3:      # 꽃 마리오
            if mario.dir == 1:
                mario.image.clip_draw(744 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(217 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

class FallState:
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
            mario.y += (GRAVITY_PPS * mario.jumptime ** 2 / 2)

        if mario.y <= BOTTOM:
            mario.y = BOTTOM
            mario.jumptime = 0
            mario.jump = False
            mario.add_event(JUMP_FINISH)

    def draw(mario):
        if mario.state == 1:
            if mario.dir == 1:
                mario.image.clip_draw(0 + int(mario.frame) * 45, 90, 38, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(960 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

        elif mario.state == 2:
            if mario.dir == 1:
                mario.image.clip_draw(350 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(615 - 5 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)

        elif mario.state == 3:      # 꽃 마리오
            if mario.dir == 1:
                mario.image.clip_draw(744 + int(mario.frame) * 45, 90, 40, 90, mario.x, mario.y, 50, 50)
            else:
                mario.image.clip_draw(217 + int(mario.frame) * 45, 0, 40, 90, mario.x, mario.y, 50, 50)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: JumpState, Z: IdleState, O:FallState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, SPACE: JumpState, JUMP_FINISH: IdleState, Z: RunState, O:FallState},
    JumpState: {RIGHT_UP: JumpState, LEFT_UP: JumpState, LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState, SPACE: JumpState, JUMP_FINISH: RunState, Z: JumpState, O:FallState},
    FallState: {RIGHT_UP: FallState, LEFT_UP: FallState, RIGHT_DOWN: FallState, LEFT_DOWN: FallState, SPACE: JumpState, JUMP_FINISH: RunState, Z: IdleState, O:FallState}
}

class Mario:
    def __init__(self, x, y):
        self.image = load_image('mario_sheet2.png')
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

        self.state = 1                        # 1: 작은 마리오  2: 큰 마리오 3: 꽃 마리오

        self.jumptime = 0
        self.jump = False

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.parent = None

    def add_event(self, event):
        self.event_que.insert(0, event)

    def get_bb(self):
        if self.state == 1:
            return self.x - 15, self.y - 27, self.x + 15, self.y + 27
        else:
            return self.x - 15, self.y - 27, self.x + 15, self.y + 27

    def get_bb_head(self):
        if self.state == 1:
            return self.x - 10, self.y + 3, self.x + 13, self.y + 6
        else:
            return self.x - 10, self.y + 22, self.x + 13, self.y + 25

    def get_bb_foot(self):
        if self.state == 1:
            return self.x - 12, self.y - 27, self.x + 15, self.y - 25
        else:
            return self.x - 12, self.y - 27, self.x + 15, self.y - 25

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)



#--------------발, 머리----------
        if collision.collide_foot_head(self, server.block1):
            self.set_parent(server.block1)
            self.y = server.block1.y + 40
            if self.x > server.block1.x + 20 * server.block1.l or self.x < server.block1.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.block2):
            self.set_parent(server.block2)
            self.y = server.block2.y + 40
            if self.x > server.block2.x + 20 * server.block2.l or self.x < server.block2.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.block3):
            self.set_parent(server.block3)
            self.y = server.block3.y + 40
            if self.x > server.block3.x + 20 * server.block3.l or self.x < server.block3.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.block4):
            self.set_parent(server.block4)
            self.y = server.block4.y + 40
            if self.x > server.block4.x + 20 * server.block4.l or self.x < server.block4.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.block5):
            self.set_parent(server.block5)
            self.y = server.block5.y + 40
            if self.x > server.block5.x + 20 * server.block5.l or self.x < server.block5.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile):
            self.set_parent(server.air_tile)
            self.y = server.air_tile.y + 40
            if self.x > server.air_tile.x + 20 * server.air_tile.l or self.x < server.air_tile.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile2):
            self.set_parent(server.air_tile2)
            self.y = server.air_tile2.y + 40
            if self.x > server.air_tile2.x + 20 * server.air_tile2.l or self.x < server.air_tile2.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile3):
            self.set_parent(server.air_tile3)
            self.y = server.air_tile3.y + 40
            if self.x > server.air_tile3.x + 20 * server.air_tile3.l or self.x < server.air_tile3.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile4):
            self.set_parent(server.air_tile4)
            self.y = server.air_tile4.y + 40
            if self.x > server.air_tile4.x + 20 * server.air_tile4.l or self.x < server.air_tile4.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile5):
            self.set_parent(server.air_tile5)
            self.y = server.air_tile5.y + 40
            if self.x > server.air_tile5.x + 20 * server.air_tile5.l or self.x < server.air_tile5.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile6):
            self.set_parent(server.air_tile6)
            self.y = server.air_tile6.y + 40
            if self.x > server.air_tile6.x + 20 * server.air_tile6.l or self.x < server.air_tile6.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile7):
            self.set_parent(server.air_tile7)
            self.y = server.air_tile7.y + 40
            if self.x > server.air_tile7.x + 20 * server.air_tile7.l or self.x < server.air_tile7.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile8):
            self.set_parent(server.air_tile8)
            self.y = server.air_tile8.y + 40
            if self.x > server.air_tile8.x + 20 * server.air_tile8.l or self.x < server.air_tile8.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.air_tile9):
            self.set_parent(server.air_tile9)
            self.y = server.air_tile9.y + 40
            if self.x > server.air_tile9.x + 20 * server.air_tile9.l or self.x < server.air_tile9.x - 20:
                self.parent = None
                self.add_event(O)



        if collision.collide_foot_head(self, server.item_block1):
            self.set_parent(server.item_block1)
            self.y = server.item_block1.y + 40
            if self.x > server.item_block1.x + 10 or self.x < server.item_block1.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.item_block2):
            self.set_parent(server.item_block2)
            self.y = server.item_block2.y + 40
            if self.x > server.item_block2.x + 10 or self.x < server.item_block2.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.item_block3):
            self.set_parent(server.item_block3)
            self.y = server.item_block3.y + 40
            if self.x > server.item_block3.x + 10 or self.x < server.item_block3.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.item_block4):
            self.set_parent(server.item_block4)
            self.y = server.item_block4.y + 40
            if self.x > server.item_block4.x + 10 or self.x < server.item_block4.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.item_block5):
            self.set_parent(server.item_block5)
            self.y = server.item_block5.y + 40
            if self.x > server.item_block5.x + 10 or self.x < server.item_block5.x - 20:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.pipe):
            self.set_parent(server.pipe)
            self.y = server.pipe.y + 52
            if self.x > server.pipe.x + 30 or self.x < server.pipe.x - 15:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.pipe2):
            self.set_parent(server.pipe2)
            self.y = server.pipe2.y + 52
            if self.x > server.pipe2.x + 30 or self.x < server.pipe2.x - 15:
                self.parent = None
                self.add_event(O)

        if collision.collide_foot_head(self, server.pipe3):
            self.set_parent(server.pipe3)
            self.y = server.pipe3.y + 52
            if self.x > server.pipe3.x + 30 or self.x < server.pipe3.x - 15:
                self.parent = None
                self.add_event(O)


#--------------머리, 발--------------
        if collision.collide_head_foot(self, server.block1):
            self.add_event(O)
        if collision.collide_head_foot(self, server.block2):
            self.add_event(O)
        if collision.collide_head_foot(self, server.block3):
            self.add_event(O)
        if collision.collide_head_foot(self, server.block4):
            self.add_event(O)
        if collision.collide_head_foot(self, server.block5):
            self.add_event(O)

        if collision.collide_head_foot(self, server.item_block1):
            self.add_event(O)
        if collision.collide_head_foot(self, server.item_block2):
            self.add_event(O)
        if collision.collide_head_foot(self, server.item_block3):
            self.add_event(O)
        if collision.collide_head_foot(self, server.item_block4):
            self.add_event(O)
        if collision.collide_head_foot(self, server.item_block5):
            self.add_event(O)

        if collision.collide_head_foot(self, server.air_tile):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile2):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile3):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile4):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile5):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile6):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile7):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile8):
            self.add_event(O)
        if collision.collide_head_foot(self, server.air_tile9):
            self.add_event(O)



    def skill(self):
        fire = Fire(self.x, self.y, self.dir)
        game_world.add_object(fire, 1)

    def fall(self):
        self.y -= GRAVITY_PPS * game_framework.frame_time


    def draw(self):
        self.cur_state.draw(self)
        #draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_foot())
        draw_rectangle(*self.get_bb_head())
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




