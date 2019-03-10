from sketcher import sketch


@sketch
class Sk:
    def setup(self):
        self.size(200, 200)

    def loop(self):
        self.clear()
        key = self.keyboard_state()
        if 'a' in key.pressed:
            self.text(100, 100, 'a')
