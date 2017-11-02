from math import *
import copy
from swampy.World import World


class Point(object):
    """Represent a point in 2-D space"""
    x = 0.0
    y = 0.0


class Rectangle(object):
    """Represents a Rectangle
    attributes: width, length, corner"""
    width = 0.0
    length = 0.0
    corner = Point()


class Circle(object):
    """Represents a Circle
    attributes: radius, x-coordinate, y-coordinate"""
    radius = 0
    xc = 0
    yc = 0


def distance_between_points(p1, p2):
    return round(sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2), 2)


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.length/2.0
    return p


def move_rectangle(rect, dx, dy):
    r = copy.deepcopy(rect)
    r.corner.x += dx
    r.corner.y += dy
    return r


def draw_rectangle(canvas, rect, colour):
    bbox = [[rect.corner.x, rect.corner.y], [rect.corner.x + rect.length, rect.corner.y+rect.width]]
    canvas.rectangle(bbox, outline='black', width=10, fill=colour)


def draw_point(canvas, point):
    p = point
    canvas.line(coords=[[0, 0], [100, 0]], fill='black', width=1)
    canvas.line(coords=[[0, 0], [0, 100]], fill='black', width=1)
    canvas.line(coords=[[0, p.y], [p.x, 0]], fill='blue', width=50)
    # canvas.text(coord=[p.x, p.y], text='({0}, {1}).'.format(p.x, p.y), fill='black', width=100)


def draw_circle(canvas, circle, colour):
    c = circle
    canvas.circle(coord=[c.xc, c.yc], r=c.radius, fill=colour)


def draw_flag(canvas):
    points = [[-100, -100], [50, -10], [-100, 100]]
    points2 = [[300, 10], [20, 10], [-100, -100], [300, -100]]
    canvas.polygon(points, fill='blue')
    canvas.polygon(points2, fill='red')

p1 = Point()
p2 = Point()

p1.x, p1.y = -3, -4
p2.x, p2.y = -5, 5

box = Rectangle()
box.corner = p1
box.width = 100.0
box.length = 200.0

center = find_center(box)
new_corner = move_rectangle(box, 5, 10)

circle1 = Circle()
circle1.radius = 40
circle1.xc = 0
circle1.yc = 0

circle2 = Circle()
circle2.radius = 30
circle2.xc = 5
circle2.yc = 0

circle3 = Circle()
circle3.radius = 50
circle3.xc = 0
circle3.yc = 5

world = World()

canvas = world.ca(width=500, height=500, background='white')
# draw_rectangle(canvas=canvas, rect=box, colour='blue')
# draw_point(canvas=canvas, point=p1)
draw_circle(canvas, circle3, 'white')
draw_circle(canvas, circle1, 'blue')
draw_circle(canvas, circle2, 'black')
# draw_flag(canvas)
world.mainloop()
# print(box.corner.x, box.corner.y)
# print(new_corner.corner.x, new_corner.corner.y)
