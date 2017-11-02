import math
from exercise_4 import arc

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0 / n)


def move(t, length):
    pu(t)
    fd(t, length)
    pd(t)

world = TurtleWorld()
ray = Turtle()
ray.delay = 0.001

move(ray, 10)
flower(ray, 5, 100, 60)
wait_for_user()
