import turtle 
import time
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
bob = turtle.Pen() 
turtle.bgcolor('black')
for x in range(150): 
	bob.pencolor(colors[x%6]) 
	bob.width(x/100 + 1) 
	bob.forward(x) 
	bob.left(59) 
	bob.speed(0)
time.sleep(10)