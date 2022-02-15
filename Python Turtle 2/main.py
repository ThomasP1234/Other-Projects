import turtle as t
import time

t.bgcolor("black")
colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
t.speed(500)
t.pencolor("white")

t.left(60)
for i in range(36):
    for j in range(3):
        t.forward(100)
        t.right(120)
    t.right(10)