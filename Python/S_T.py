import turtle

bob = turtle.Turtle()
bob.color("blue","CYAN")

bob.begin_fill()
for i in range(4) :
    bob.forward(100)
    bob.left(90)

turtle.penup()
bob.right(90)
bob.forward(100)
turtle.pendown()

for i in range(4) :
    bob.forward(100)
    bob.left(90)
turtle.penup()
bob.right(90)
bob.forward(100)
turtle.pendown()

for i in range(4) :
    bob.forward(100)
    bob.left(90)
turtle.penup()
bob.right(90)
bob.forward(100)
turtle.pendown()

for i in range(4) :
    bob.forward(100)
    bob.left(90)
turtle.penup()
bob.right(90)
bob.forward(100)
turtle.pendown()
bob.end_fill()


turtle.done()