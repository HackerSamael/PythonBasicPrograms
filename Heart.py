import turtle
from time import sleep

#To create the upper semi circles
def semCircle():
    for i in range(200):
        t.right(1)
        t.fd(1)
        

#To create the full heart
def heart(t,size):
    t.fillcolor("red")
    t.hideturtle()
    t.begin_fill()
    t.penup()
    t.goto(-30,-100)
    t.pendown()
    t.left(135)
    t.fd(size)
    semCircle()
    t.left(135)
    semCircle()
    t.fd(size)
    t.end_fill()
    
    

t = turtle.Turtle()
sleep(2)
heart(t,142)
sleep(10)
