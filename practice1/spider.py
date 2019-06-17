import turtle
import math

t = turtle.Turtle()
t.shape('turtle')

legs_angle = 360 / 12
for i in range(12):
	t.forward(100)
	t.stamp()
	t.left(180) # turn to face center on the way back
	t.forward(100)
	t.right(180) # turn to face border on the way forward
	t.right(legs_angle)


