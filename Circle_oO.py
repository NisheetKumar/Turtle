import turtle


tur =  turtle.Turtle()

tur.color("red")
tur.pensize(5)
tur.shape('turtle')

i = 0
o = 1
while True:
    if i == 360:
        o += 1
        i = 0
    elif i > 180:
        tur.forward(o)
        tur.left(2)
        tur.speed(0)
    elif i < 180:
        tur.forward(o)
        tur.right(2)
        tur.speed(0)
    
    i += 1
    if o > 6: input()



