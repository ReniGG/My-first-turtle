import turtle
import random

ws = turtle.Screen()
ws.title("Turtle practice")
ws.bgcolor("azure")

tess = turtle.Turtle()
tess.shape("turtle")
tess.color("lightpink")
tess.pensize(5)
tess.speed(0)

def random_color():
    return random.random(), random.random(), random.random()

def change_bg_color():
    if is_drawing:
        ws.bgcolor(random_color())
        ws.ontimer(change_bg_color, 1000)

is_drawing = True
change_bg_color()

dist = 2

for _ in range(100):
    tess.color(random_color())
    tess.left(50)
    tess.forward(dist)
    dist += 2

is_drawing = False
turtle.done()

