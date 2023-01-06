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

    while win.isOpen():
        time.sleep(0.05)
        #TODO: Pradobodobienstwo 1/5??? o co kaman???????
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