import random

from pico2d import load_image, get_time

import game_framework

# Bird Run Speed
# fill here
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 50.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
# fill here
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Fly:

    @staticmethod
    def enter(bird, e):
        pass

    @staticmethod
    def exit(bird, e):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        if bird.frame == 4:
            bird.action -= 1
        elif bird.action == 0 and bird.frame == 3:
            bird.action = 2
        bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time
        if bird.x > 1600:
            bird.dir = -1
        elif bird.x < 0:
            bird.dir = 1

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_composite_draw(int(bird.frame)*180, bird.action*168, 184, 168, 0, '', bird.x, bird.y, 130, 120)
        elif bird.dir == -1:
            bird.image.clip_composite_draw(int(bird.frame)*180, bird.action*168, 184, 168, 0, 'h', bird.x, bird.y, 130, 120)


class StateMachine:
    def __init__(self, bird):
        self.bird = bird
        self.cur_state = Fly


    def start(self):
        self.cur_state.enter(self.bird, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.bird)

    def draw(self):
        self.cur_state.draw(self.bird)


class Bird:
    image = None
    def __init__(self):
        self.x, self.y = random.randrange(0, 1600), 500
        self.frame = 0
        self.action = 2
        self.dir = 1
        if Bird.image == None:
            self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()
