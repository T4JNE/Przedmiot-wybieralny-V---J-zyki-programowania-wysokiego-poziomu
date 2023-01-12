import math
import random
from graphics import *

# ==========================
print("Zad 1")
win = GraphWin('Zad 1', 500, 500)
win.setBackground('grey')


try:
    o = Oval(Point(300, 200), Point(325, 300))
    o.setFill('blue')
    o.draw(win)

    c = Circle(Point(250, 250), 20)
    c.setFill('red')
    c.draw(win)

    r = Rectangle(Point(400, 200), Point(425, 300))
    r.setFill('yellow')
    r.draw(win)

    for i in range(50):
        if win.isClosed():
            break
        time.sleep(0.05)
        c.move(3, 0.2)
    win.getMouse()
except GraphicsError:
    pass
win.close()

# ==========================
print("Zad 2")
win = GraphWin('Zad 2', 500, 500)
win.setBackground('grey')


try:
    c = Circle(Point(250, 250), 20)
    c.setFill('red')
    c.draw(win)

    k = win.getKey()
    while k != 'q':
        if k == 'w':
            c.move(0, -10)
        elif k == 's':
            c.move(0, 10)
        elif k == 'a':
            c.move(-10, 0)
        elif k == 'd':
            c.move(10, 0)
        k = win.getKey()
except GraphicsError:
    pass
win.close()

# ==========================
print("Zad 3")
win = GraphWin('Zad 3', 500, 500)
win.setBackground('grey')


try:
    c = Circle(Point(250, 250), 20)
    c.setFill('red')
    c.draw(win)

    rand = random.randint(1, 4)
    while win.isOpen():
        time.sleep(0.05)

        #Pradobodobienstwo 1/5
        if random.randint(1, 5) == 1:
            rand = random.randint(1, 4)

        if rand == 1:
            c.move(0, -10)
        elif rand == 2:
            c.move(0, 10)
        elif rand == 3:
            c.move(-10, 0)
        elif rand == 4:
            c.move(10, 0)

except GraphicsError:
    pass
win.close()

# ==========================
print("Zad 4")
win = GraphWin('Zad 4', 500, 500)
win.setBackground('grey')

try:
    c = Circle(Point(100, 100), 20)
    c.setFill('red')
    c.draw(win)

    alpha = 0

    while win.isOpen():
        time.sleep(0.05)
        alpha += random.randint(-20, 20)
        alpha_radians = math.radians(alpha)
        c.move(10 * math.cos(alpha_radians), 10 * math.sin(alpha_radians))

except GraphicsError:
    pass

win.close()

# ==========================
print("Zad 5")
win = GraphWin('Zad 5', 500, 500)
win.setBackground('grey')

try:
    c = Circle(Point(100, 100), 20)
    c.setFill('red')
    c.draw(win)

    alpha = 0

    while win.isOpen():
        time.sleep(0.05)
        alpha += random.randint(-20, 20)

        #TOP
        if win.coords(1)[1] <= 10:
            #print("top", win.coords(1)[1])
            #win.getMouse()
            alpha = 90
        #LEFT
        elif win.coords(1)[0] <= 10:
            #print("left", win.coords(1)[0])
            #win.getMouse()
            alpha = 0
        #BOTTOM
        elif win.coords(1)[3] >= 490:
            #print("bottom", win.coords(1)[3])
            #win.getMouse()
            alpha = 270
        #RIGHT
        elif win.coords(1)[2] >= 490:
            #print("right", win.coords(1)[2])
            #win.getMouse()
            alpha = 180
        alpha_radians = math.radians(alpha)
        c.move(10 * math.cos(alpha_radians), 10 * math.sin(alpha_radians))

except GraphicsError:
    pass

win.close()

# ==========================
print("Zad 6")
win = GraphWin('Zad 6', 500, 500)
win.setBackground('grey')

try:
    c = Circle(Point(250, 150), 50)
    c.setFill('red')
    c.draw(win)

    c2 = Circle(Point(245, 265), 50)
    c2.setFill('blue')
    c2.draw(win)

    alpha = 0

    while win.isOpen():
        time.sleep(0.05)
        alpha += 5
        if alpha >= 360:
            alpha = 0

        alpha_radians = math.radians(alpha)
        c.move(10 * math.cos(alpha_radians), 10 * math.sin(alpha_radians))

except GraphicsError:
    pass

win.close()
