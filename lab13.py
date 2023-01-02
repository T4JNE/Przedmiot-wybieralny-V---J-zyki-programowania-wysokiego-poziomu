import math
import random
from graphics import *

# ==========================
print("Zad 1")
win = GraphWin('Zad 1', 500, 500)
win.setBackground('black')

try:
    win.getMouse()
except GraphicsError:
    pass
win.close()

# ==========================
print("Zad 2")
win = GraphWin('Zad 2', 500, 500)
win.setBackground('grey')

colors = {
    0: 'black',
    1: 'red',
    2: 'blue',
    3: 'lime',
    4: 'yellow'
}

for i in range(1000):
    pt = Point(random.randint(0, 499), random.randint(0, 499))
    pt.setOutline(colors[random.randint(0, len(colors) - 1)])
    pt.draw(win)

try:
    win.getMouse()
except GraphicsError:
    pass

win.close()
# ==========================
print("Zad 3")
win = GraphWin('Zad 3', 500, 500)
win.setBackground('grey')


try:
    for i in range(50):
        pt = Point(random.randint(0, 499), random.randint(0, 499))
        c = Circle(pt, random.randint(10, 30))
        c.setOutline(colors[random.randint(0, len(colors) - 1)])
        c.setWidth(2)
        c.draw(win)
        time.sleep(0.1)

    win.getMouse()
except GraphicsError:
    pass

win.close()

# ==========================
print("Zad 4")
win = GraphWin('Zad 4', 500, 500)
win.setBackground('grey')

try:
    for i in range(4):
        pt1 = Point(random.randint(0, 499), random.randint(0, 499))
        pt2 = Point(random.randint(0, 499), random.randint(0, 499))
        o = Oval(pt1, pt2)
        o.setOutline(colors[random.randint(0, len(colors) - 1)])
        o.setWidth(2)
        o.draw(win)

        r = Rectangle(pt1, pt2)
        r.setOutline(colors[random.randint(0, len(colors) - 1)])
        r.setWidth(2)
        r.draw(win)

    win.getMouse()
except GraphicsError:
    pass

win.close()
# ==========================
print("Zad 5")
win = GraphWin('Zad 5', 500, 500)
win.setBackground('grey')

try:
    pt1 = Point(random.randint(0, 499), random.randint(0, 499))
    pt2 = Point(random.randint(0, 499), random.randint(0, 499))
    pt0 = pt1
    for i in range(9):
        l = Line(pt1, pt2)
        pt1 = pt2
        pt2 = Point(random.randint(0, 499), random.randint(0, 499))
        l.setOutline('red')
        l.setWidth(2)
        l.draw(win)
    l = Line(pt1, pt0)
    l.setOutline('red')
    l.setWidth(2)
    l.draw(win)

    win.getMouse()
except GraphicsError:
    pass

win.close()

# ==========================
print("Zad 6")
n = int(input("Podaj n:"))

radius = 200
offset_x = 250
offset_y = 250

win = GraphWin('Zad 6', 500, 500)
win.setBackground('grey')

inner_angle = 360 / n
try:
    current_angle = -90
    radian_angle = math.radians(current_angle)
    pt2 = Point(int(radius * math.cos(radian_angle)) + offset_x, int(radius * math.sin(radian_angle)) + offset_y)
    for i in range(n):
        current_angle += inner_angle
        radian_angle = math.radians(current_angle)

        pt1 = pt2
        pt2 = Point(radius * math.cos(radian_angle) + 250, radius * math.sin(radian_angle) + 250)
        l = Line(pt1, pt2)
        l.setWidth(2)
        l.setOutline('blue')
        l.draw(win)

    win.getMouse()
except GraphicsError:
    pass

win.close()