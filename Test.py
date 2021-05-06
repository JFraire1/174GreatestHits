import turtle
import random
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
z = 0
colors = ( "Blue", "Red", "Purple", "Orange" )
angles = (30, 15, 60, 120, 45, 90)
def square(y):
    a = 0
    while a < 4:
        t.forward(y)
        t.right(90)
        a = a + 1
def fillscreen(color):
    t.color(color)
    t.fillcolor(color)
    t.penup()
    t.forward(500)
    t.pendown()
    t.left(90)
    t.forward(500)
    t.right(180)
    t.begin_fill()
    square(1000)
    t.end_fill()
    t.setpos(0,0)
def squareshit(y):
    z = 0
    while z < 10:
        t.color(random.choice(colors))
        square(y)
        t.right(random.choice(angles))
        y = y*1.02
        z = z + 1
    while z >= 10 and z < 275:
        t.color(random.choice(colors))
        square(y)
        t.right(random.choice(angles))
        z = z + 1
        y = y*1.02
def circleshit(y):
    z = 0
    while z < 10:
        t.color(random.choice(colors))
        t.circle(y)
        t.right(15)
        z = z + 1
        y = y*1.02
    while z >= 10 and z < 150:
        t.color(random.choice(colors))
        t.circle(y)
        t.right(30)
        z = z + 1
        y = y*1.02

fillscreen("black")
squareshit(5)
t.penup()
t.setpos(0,0)
t.pendown()
circleshit(10)


