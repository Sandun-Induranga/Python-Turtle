import turtle
import math

"""
* @author : Sandun Induranga
* @since : 0.1.0
"""

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

# t = turtle.Turtle()
# t.color("red", "yellow")
# t.speed(10)
#
# t.begin_fill()
# for i in range(100):
#     t.forward(150)
#     t.left(170)

t = turtle.Turtle()
t.color('blue')
t.width(30)

t.begin_fill()
t.left(-90)
t.forward(150)
t.left(-180)
t.forward(75)
t.right(90)
t.forward(100)
t.left(90)
t.forward(75)
t.left(-180)
t.forward(150)


t.down()

turtle.done()
