from sketcher import sketch, config

w, h = 800, 800
dt = 0.01


class Ball:
    def __init__(self):
        self.x = w/2
        self.y = h/2
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0

    def accelerate(self, acc=(0, 0)):

        # friction

        self.ax = acc[0]
        self.ay = acc[1] - 1000
        nv = (self.vx*self.vx + self.vy*self.vy)**0.5
        self.ax -= dt*self.vx*nv
        self.ay -= dt*self.vy*nv

    def update(self):

        # dynamic
        self.x += dt*self.vx
        self.y += dt*self.vy
        self.vx += dt*self.ax
        self.vy += dt*self.ay

        # floor
        if self.y < 28:
            self.vy = 0
            self.y = 28
            self.ay = 0

    def draw(self, sk):
        sk.image(self.x, self.y, 'horrible_smiley.png')


@sketch
class Sk:
    def setup(self):
        pass  # Here come the initialisation
        self.ball = Ball()
        self.frame(dt)
        self.size(w, h)

    def loop(self):
        self.clear()

        push = [0, 0]

        key = self.keyboard_state()
        if 'up' in key.pressed:
            push[1] += 9000
        if 'down' in key.pressed:
            push[1] -= 9000
        if 'left' in key.pressed:
            push[0] -= 2000
        if 'right' in key.pressed:
            push[0] += 2000

        self.ball.accelerate(push)
        self.ball.update()
        self.ball.draw(self)
