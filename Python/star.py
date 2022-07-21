import turtle
import math

bob = turtle.Turtle()
bob.color("blue","cyan")
bob.speed(10)

bob.begin_fill()
for i in range(200):
    bob.forward(math.sqrt(i)*30)
    bob.left(170)

bob.end_fill()


turtle.done()