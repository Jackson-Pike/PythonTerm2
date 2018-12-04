import turtle
import random


c = ["black", "red", "green", "blue"]
x = turtle.Pen()
x.reset()
x.speed(0)
x.width(10)
z = 0
g = 500
a = 90
for i in range(400):
    x.forward(g)
    x.right(a)
    x.color(random.choice(c))
    z+=1
    if z >= 4:
        g-=1
        a+=0.5
        z = 0
input()

