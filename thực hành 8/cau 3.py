print("Nguyen Minh Thắng","\nMSSV: 235752021610097")
import turtle
colors=['blue','red']
painter=turtle.Turtle()
painter.pensize(5)
painter.speed (500)
for i in range (500):
    color=colors[i%len(colors)]
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
    painter.setposition(0,0)

