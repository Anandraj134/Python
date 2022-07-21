from turtle import *
color('black', 'Red')

begin_fill()
while True:
    speed(9)
    forward(200)
    right(170)
    if abs(pos()) < 1:
        break
end_fill()
done()