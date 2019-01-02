from sketcher import sketch
import random as rd

w = 800
h = 800

tri = [
    (w/2, 0),
    (0, h),
    (w, h)
]


@sketch
class Sk:
    def setup(sk):
        sk.size(w, h)
        sk.frame(0.001)
        sk.x = rd.random()*w
        sk.y = rd.random()*h

    def loop(sk):
        sk.point(sk.x, sk.y)
        i = rd.randint(0, 2)
        sk.x = 0.5*(tri[i][0] + sk.x)
        sk.y = 0.5*(tri[i][1] + sk.y)
