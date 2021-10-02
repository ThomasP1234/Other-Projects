import turtle as t

t.bgcolor("black")
colours = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
t.speed(500)

degree = 0

t.pencolor("white")



t.right(degree)
for i in range(32):
    t.circle(150)
    t.left(11.25)

for i in range(12):
    t.pencolor(colours[0])
    temp = colours.pop(0)
    colours.append(temp)
    for j in range(32):
        for k in range(4):
            t.forward(12.5*(i+1))
            t.left(90)
        t.left(11.25)
    t.left(5)
    degree += 5

t.exitonclick()