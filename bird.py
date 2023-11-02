from pico2d import load_image, get_time


class StateMachine:
    def __init__(self, boy):
        self.boy = boy

    def start(self):
        self.cur_state.enter(self.boy, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.boy)

    def draw(self):
        self.cur_state.draw(self.boy)


class Bird:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.action = 0
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()


    def update(self):
        self.state_machine.update()

    def draw(self):
        self.state_machine.draw()
