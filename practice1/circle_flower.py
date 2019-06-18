import turtle
import math

t = turtle.Turtle()
t.shape('turtle')
t.speed(1)

pedals_number = 8
angle = 30

while pedals_number//2 > 0:
	for i in range(2):
		t.circle(20)
		t.right(180)
	t.right(angle)
	pedals_number -= 1