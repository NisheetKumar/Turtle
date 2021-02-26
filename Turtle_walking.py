import turtle
import random
import math


red = turtle.Turtle()
green = turtle.Turtle()
blue = turtle.Turtle()
orange = turtle.Turtle()
white = turtle.Turtle()

red.color('red')
green.color('green')
blue.color('blue')
orange.color('orange')
white.color('black')


red.shape('turtle')
green.shape('turtle')
blue.shape('turtle')
orange.shape('turtle')
white.shape('turtle')

turtles_list = []
turtles_list.append(red)
turtles_list.append(green)
turtles_list.append(blue)
turtles_list.append(orange)
turtles_list.append(white)


turtle.speed(0)
turtle.tracer(0)

for j in range(100000):       
    for t in turtles_list:
        t.pensize(2)
        t.seth(random.randrange(0,360,90))
        t.forward(10)
    turtle.update()


input()