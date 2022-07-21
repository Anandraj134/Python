def star(bob, size):
    if size <= 10 :
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            bob.speed(0)
            bob.forward(size)
            star(bob, size/3)
            bob.left(216)
        bob.end_fill()

import turtle
bob = turtle.Turtle()
bob.getscreen().bgcolor("#994444")

bob.penup()
bob.goto((-200, 100))
bob.pendown()



star(bob, 360)

turtle.done()