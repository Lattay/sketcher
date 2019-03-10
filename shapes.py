from sketcher import sketch, Sketch, config
from sketcher.common import Shape, Vec2
from math import pi

config.backend_use = 'pyglet'

half_pi = pi * 0.5

w, h = 500, 500
dt = 0.01

x0, y0 = w/2, h/2
triUp = Shape([
    (x0, y0 + 40),
    (x0 - 15, y0 - 10),
    (x0 + 15, y0 - 10)
])
triLeft = triUp.rotate(half_pi)
triRight = triUp.rotate(-half_pi)
triDown = triUp.rotate(pi)

x1, y1 = w/10, h/10

c = min(w, h) / 30
parra = Shape([
    (1*c, 2*c),
    (6*c, 2*c),
    (5*c, 0),
    (0, 0),
]).translate((100, 300))

star = Shape([
    (0, 0),
    (0.5*c, 1.5*c),
    (0, 3*c),
    (c, 2.5*c),
    (1.5*c, 4*c),
    (2*c, 2.5*c),
    (3*c, 3*c),
    (2.5*c, 1.5*c),
    (3*c, 0),
    (1.5*c, c),
]).translate((100, 100))

v1 = Vec2(100, 0)
@sketch
class Sk(Sketch):
    def setup(self):
        self.frame(dt)
        self.size(w, h)
        self.star = star
        self.ctr = star.center()

    def loop(self):
        global star, v1
        self.clear()
        self.rectangle(w-50, h-50, -100, -100)
        self.shape(parra)
        self.shape(parra.translate((100, -20)))
        self.shape(self.star)
        self.star = self.star.rotate(0.01, pivot=self.ctr)
        key = self.keyboard_state()
        if 'up' in key.pressed:
            self.shape(triUp)
        elif 'down' in key.pressed:
            self.shape(triDown)
        elif 'left' in key.pressed:
            self.shape(triLeft)
        elif 'right' in key.pressed:
            self.shape(triRight)
