import turtle
import math

t = turtle.Turtle()
t.shape('turtle')

def get_angle(side_number):
	return 360 / side_number


def move_turtle_in_shape(angle, side_number):
    for i in range(side_number):
        t.left(angle)
        t.forward(50)