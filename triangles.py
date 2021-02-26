import turtle

tur =  turtle.Turtle()

tur.color("red")
tur.pensize(5)
tur.shape('turtle')

for i in range(50):
    o = 20+(10*i)
    tur.forward(o)
    print(o)
    tur.right(30)
    tur.speed(10)
    tur.right(210)

input()