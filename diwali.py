import turtle
import time
import random


wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgcolor("#121212")
wn.colormode(255)

t = turtle.Turtle()

def h():
    t.penup()
    t.setpos(-300, 200)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(180)
    t.fd(100)

def a1():
    t.penup()
    t.setpos(-200, 200)
    t.pendown()
    t.left(90)
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(180)
    t.fd(50)
    t.right(60)
    t.fd(50)

def p1():
    t.penup()
    t.setpos(-50, 200)
    t.pendown()
    t.left(150)
    t.fd(80)
    t.right(180)
    t.circle(25)

def p2():
    t.penup()
    t.setpos(50, 200)
    t.pendown()
    t.left(180)
    t.fd(80)
    t.right(180)
    t.circle(25)

def y():
    t.penup()
    t.setpos(150, 200)
    t.pendown()
    t.left(150)
    t.fd(110)
    t.right(180)
    t.fd(60)
    t.right(120)
    t.fd(60)
    t.right(180)
    t.fd(60)
    t.right(60)
    t.fd(50)
    t.left(120)

def d():
    t.penup()
    t.setpos(-350, 0)
    t.pendown()
    t.left(90)
    t.fd(100)
    t.right(90)
    t.circle(-50, 180, 30)
    t.right(180)

def i1():
    t.penup()
    t.setpos(-250, 0)
    t.pendown()
    t.fd(50)
    t.left(180)
    t.fd(25)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(25)
    t.backward(50)

def w():
    t.penup()
    t.setpos(-150, 100)
    t.pendown()
    # t.color("blue")
    t.right(90)
    t.fd(100)
    t.left(135)
    t.fd(50)
    t.right(90)
    t.fd(50)
    t.left(135)
    t.fd(100)
    t.right(180)
    t.fd(100)

def a2():
    t.penup()
    t.setpos(-50, 0)
    t.pendown()
    t.left(90)
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(50)
    t.right(120)
    t.forward(50)
    t.right(180)
    t.fd(50)
    t.right(60)
    t.fd(50)
    # t.color("white")

def l():
    t.penup()
    t.setpos(100, 0)
    t.pendown()
    t.left(150)
    t.fd(100)
    t.right(180)
    t.fd(100)
    t.left(90)
    t.fd(60)

def i2():
    t.penup()
    t.setpos(200, 0)
    t.pendown()
    t.fd(50)
    t.left(180)
    t.fd(25)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(25)
    t.backward(50)


for i in range(5):
    radius = random.randint(80, 200)
    x_coord = random.randint(-400, 400)
    y_coord = random.randint(-300, 300)
    t.penup()
    t.setpos(x_coord,y_coord)
    t.pendown()
    B = random.randint(0,255)
    R = random.randint(0,255)
    G = random.randint(0,255)
    t.pencolor(R,G,B)
    for i in range(18):
        t.fd(radius)
        t.backward(2*radius)
        t.fd(radius)
        t.right(10)

t.setheading(0)
t.color("white")
t.pensize(10)

h()
a1()
p1()
p2()
y()
d()
i1()
w()
a2()
l()
i2()
t.hideturtle()

time.sleep(4)

# Initials #
t.pencolor("white")
t.penup()
t.setpos(300, -200)
t.pendown()
t.setheading(0)
t.pensize(4)

# For Gradient background
for x in range(3):
    for i in range(0, 255):
        red = 255 - i
        green = 0
        blue = i
        wn.bgcolor(red, green, blue)
        time.sleep(0.01)
    for i in range(0, 255):
        red = i
        green = 0
        blue = 255 - i
        wn.bgcolor(red, green, blue)
        time.sleep(0.01)