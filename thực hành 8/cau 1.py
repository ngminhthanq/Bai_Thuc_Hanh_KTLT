print("Nguyen Minh Thắng","\nMSSV: 235752021610097")
import turtle
wd=turtle.Screen()
wd.bgcolor("lightgreen")
painter=turtle.Turtle()
painter.fillcolor('blue')
painter.pencolor('pink')
painter.pensize(5)
def drawsq(t, s):
    for i  in range(4):
        t.forward(s)
        t.left(90)
for i in range(1,50):
    painter.left(18)
    drawsq(painter,100)
