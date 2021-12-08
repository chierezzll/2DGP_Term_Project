from pico2d import *
import game_framework
import game_world
import random
import time
import collision
import server

class Boss_bgm:
    def __init__(self, x, y, d, num):
        self.image = load_image('boss.png')
        self.x = x
        self.y = y
        self.tx = x
        self.d = d  # 이동범위
        self.dir = 1
        self.life = 10
        self.num = num  # 갯수
        self.frame = 0
        self.boss_bgm = load_music('music_bossbgm.mp3')
        self.boss_bgm.set_volume(15)
        self.boss_bgm.repeat_play()
        self.clear_bgm = load_music('clear.mp3')
        self.clear_bgm.set_volume(10)

    def update(self):
        if server.boss.life < 0:
            game_world.remove_object(server.boss)
            self.clear_bgm.play()
            time.sleep(8)
            game_framework.quit()


    def draw(self):
        def draw(self):
            draw_rectangle(*self.get_bb())
            draw_rectangle(*self.get_bb_head())
            debug_print('Dir:' + str(self.life))
            if self.dir == 1:
                self.image.clip_draw(0 + int(self.frame) * 80, 30, 80, 80, self.x, self.y, 110, 110)
            else:
                self.image.clip_draw(0 + int(self.frame) * 80, 140, 80, 80, self.x, self.y, 110, 110)