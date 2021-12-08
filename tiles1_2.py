from pico2d import *
import collision
import server

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Tiles:
    def __init__(self):
        self.image = load_image('tiles_001.png')
        self.x = 300
        self.y = 200

    def get_bb(self):
        return self.x + 33, self.y - 200, self.x + 85, self.y

    def get_bb_2(self):
        return self.x + 665, self.y - 200, self.x + 640 + 70, self.y

    def draw(self):
        k = 0
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_2())
        for i in range(23):
            if k < 300 or 400 < k < 950 or k > 1050:
                self.image.clip_draw(0, 10, 95, 100, 0 + k, self.y - 50 )
            k += 90

    def update(self):
        if collision.collide_3(self, server.mario) or collision.collide_2(self, server.mario):
            server.mario.y -= RUN_SPEED_PPS / 200

            if server.mario.y < 50:
                server.state = 1
                server.life -= 1
                server.mario.x = 50
                server.mario.y = 900

        if 50 < server.mario.x < 60:
            server.mario.y -= RUN_SPEED_PPS / 300


    # 300 ~ 400, 950 ~ 1050