import turtle as trtl
t = trtl.Turtle()
t.penup()
t.goto(-200, -200)
t.pendown()
x = 3
while x < 3:
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.right(90)
    x = x + 1