from sketcher import sketch, Sketch
from sketcher.common import Shape
from math import pi

half_pi = pi * 0.5

w, h = 800, 800
dt = 0.01

x0, y0 = w/2, h/2
triUp = Shape([
    (x0, y0 - 40),
    (x0 - 15, y0 + 10),
    (x0 + 15, y0 + 10)
])
triLeft = triUp.rotate(half_pi)
triRight = triUp.rotate(-half_pi)
triDown = triUp.rotate(pi)


@sketch
class Sk(Sketch):
    def setup(self):
        pass  # Here come the initialisation
        self.frame(dt)
        self.size(w, h)

    def loop(self):
        self.clear()
        key = self.keyboard_state()
        if 'Up' in key.pressed:
            self.shape(triUp)
        elif 'Down' in key.pressed:
            self.shape(triDown)
        elif 'Left' in key.pressed:
            self.shape(triLeft)
        elif 'Right' in key.pressed:
            self.shape(triRight)
