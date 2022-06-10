import turtle

# Lines

# t = turtle.Turtle()
#
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.right(90)
# t.forward(100)
#
# turtle.done()

# Squares

t = turtle.Turtle()

t.color('blue', '#a2d2ff')

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.forward(150)
t.pendown()

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

turtle.done()
