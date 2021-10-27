#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as spider,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.speed(0)
spider.left(90)
spider.back(20)
spider.right(90)
spider.pensize(40)
spider.circle(20)
spider.pensize(5)
n_less_than = 8
direction_facing = 45
leg_length = 100
n = 0
while (n < n_less_than):
  spider.goto(0,0)
  spider.setheading(direction_facing * n + 22.5)
  spider.forward(leg_length)
  n = n + 1

eye = 15
for i in range(2):
    spider.color("red")
    spider.penup()
    spider.goto(eye, -25)
    spider.begin_fill()
    spider.circle(5)
    spider.end_fill()
    eye -= 30



spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()