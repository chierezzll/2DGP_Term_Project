from pico2d import *
import game_world

class Fire:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        self.frame = 0
        if Fire.image == None:
            #Fire.image = load_image('ball21x21.png')
            Fire.image = load_image('fire.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        #self.image.draw(self.x, self.y)
        self.image.clip_draw(0 + self.frame * 17, 80, 15, 15, self.x, self.y, 25, 25)

    def update(self):
        self.x += self.velocity
        self.frame = (self.frame + 1) % 3

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
