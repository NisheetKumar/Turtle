import turtle
from turtle import Screen, Turtle
import random
from time import sleep

turtle.bgcolor("black")

red = Turtle("arrow")
red.color('red')
red.speed(10)
red.pensize(10)

box = Turtle("circle")
box.color('orange')
box.speed(10)
box.pensize(10)


box.penup()
box.goto(200,200)
box.pendown()
box.right(90)
for i in range(4):
    box.forward(420)
    box.right(90)

input()

for i in range(10):
    red.color(random.choice(['red','blue','green','orange','white']))
    for j in range(100):       

        red.seth(random.randrange(0,360,90))
        red.forward(20)
        
        if red.xcor() >= 200 or red.xcor() <= -200:
            red.right(180)
            red.forward(20)
            red.penup()
        elif red.ycor() >= 200 or red.ycor() <= -200:
            red.right(180)
            red.forward(20)
            red.penup()
        else:
            red.pendown()
            print(i,j)
 
        turtle.update()
