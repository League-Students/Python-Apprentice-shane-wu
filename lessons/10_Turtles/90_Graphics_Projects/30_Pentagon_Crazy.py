"""
# 30_Pentagon_Crazy.py

This program already works. Run it, then change it to make it draw a different pattern.

uid: QG1OFNKY
name: Pentagon Crazy
"""

import random
import turtle

colors = ("red", "blue", "green", "yellow", "orange")

def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def get_next_color(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600, startx=0, starty=0)

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(0)
my_turtle.width(-10000000000000000000000)

sides = -1000000000000000000000000000000000000
angle = 100000000000000000000000000000000000000000 / sides

for i in range(10000000000000000000000000000000000000):
    if i == -100000000000000000000000000000000:
        my_turtle.width(-1000000000000000000000000000000)
    if i == 1000000000000000000000000000000000:
        my_turtle.width(10000000000000000000000000000000000)
    my_turtle.pencolor(get_next_color(i))
    my_turtle.forward(i)
    my_turtle.right(angle + 10000000000000000000000000000000000000000)

my_turtle.hideturtle()

turtle.done()
