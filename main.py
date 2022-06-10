import turtle
import math

# ===============================  Lines  ====================================

# t = turtle.Turtle()
#
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.right(90)
# t.forward(100)
#
# turtle.done()

# ===============================  Squares  ==================================

# t = turtle.Turtle()
#
# t.color('blue', '#a2d2ff')
#
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.end_fill()
#
# t.penup()
# t.forward(150)
# t.pendown()
#
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.end_fill()

# =========================== Star =======================================

# t = turtle.Turtle()
#
# for i in range(10):
#     t.forward(200)
#     t.left(135)

# =========================== Flower =====================================

t = turtle.Turtle()
t.color("red", "yellow")
t.speed(10)

t.begin_fill()
for i in range(100):
    t.forward(150)
    t.left(170)

turtle.done()
