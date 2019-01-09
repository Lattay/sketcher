from sketcher import sketch

w, h = 800, 800

tri = [(w/2, 0), (0, h), (w, h)]


@sketch
class Sk:
    def setup(s):
        s.size(w, h)
        s.background('black')
        s.stroke_color('red')
        s.x = int(s.rd.random()*w)
        s.y = int(s.rd.random()*h)

    def loop(s):
        s.point(s.x, s.y)
        i = s.rd.randint(0, 2)
        s.x = int(0.5*(tri[i][0] + s.x))
        s.y = int(0.5*(tri[i][1] + s.y))
        print(s.x, s.y)
