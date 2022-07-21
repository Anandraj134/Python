import turtle

wn = turtle.Screen()
josh = turtle.Turtle()
josh.shape("turtle")
josh.color("purple")

josh.penup()
for size in range(10) :
            josh.forward(50)
            #josh.speed(10)
            josh.stamp()
            josh.forward(-50)
            josh.right(36) 

wn.exitonclick()