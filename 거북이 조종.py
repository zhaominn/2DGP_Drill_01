import turtle
import random

def w():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)
    
def a():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)
    
def s():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)
    
def d():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def E():
    turtle.reset()
    

turtle.shape('turtle')

turtle.onkey(w,'w')
turtle.onkey(a,'a')
turtle.onkey(s,'s')
turtle.onkey(d,'d')
turtle.onkey(E,'Escape')


turtle.listen()

