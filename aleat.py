from sketcher import sketch


w, h = 1200, 800


@sketch
class Sk:
    def setup(s):
        s.background('black')
        s.frame(0.001)
        s.size(w, h)
        s.x = w/2
        s.y = h/2
        s.col = [240, 0, 0]

    def loop(s):
        theta = 2*s.m.pi*s.rd.random()
        x1 = (s.x + 10*s.m.cos(theta)) % w
        y1 = (s.y + 10*s.m.sin(theta)) % h

        s.col = [(x + s.rd.random()) % 255 for x in s.col]
        s.stroke_color(s.col)
        if abs(x1 - s.x) <= 10 and abs(y1 - s.y) <= 10:
            s.line(s.x, s.y, x1, y1)
        s.x, s.y = x1, y1
