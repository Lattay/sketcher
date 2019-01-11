from sketcher import sketch, Sketch


@sketch
class Sk:
    def setup(self):
        self.pressed = False
        self.size(800, 800)
        self.frame(0.05)

    def loop(self):
        self.clear()
        m = self.mouse_state()
        if 1 in m.pressed:
            self.pressed = True
        if 1 in m.released:
            self.pressed = False
        if self.pressed:
            x, y = m.pos
            self.ellipse(x, y, 100)
