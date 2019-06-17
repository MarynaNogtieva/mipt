import turtle
import math

t = turtle.Turtle()
t.shape('turtle')
side_size = 50

def draw_square(t, side_size):
	for i in range(4):
		t.forward(side_size)
		t.left(90)

for i in range(10):
	draw_square(t,side_size)
	# t.forward(side_size)
	side_size += 20
	t.penup() # lift turtle
	# move turtle outside
	t.backward(10)
	t.right(90)
	t.forward(10)
	t.left(90)
	t.pendown()
