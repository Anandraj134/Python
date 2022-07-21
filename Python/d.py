import turtle
wn = turtle.Screen()
wn.bgcolor("black")
tess = turtle.Turtle()
tess.color("red")
tess.shape("turtle")

print(list(range(5, 150, 2)))
tess.up()                     # this is new
for size in range(5, 150, 2):    # start with size = 5 and grow by 2
    tess.stamp()                 # leave an impression on the canvas
    tess.speed(3)                # turtle speed where 'fastest' :  0 'fast'    :  10  'normal'  :  6  'slow'    :  3 'slowest' :  1
    tess.forward(size)           # move tess along
    tess.right(25)               # and turn her

wn.exitonclick()
