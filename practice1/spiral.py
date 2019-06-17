import turtle

t = turtle.Turtle()
t.shape('turtle')
step = 3
for step in range(100):
	t.forward(step)
	t.left(20)