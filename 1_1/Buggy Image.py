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
n_less_than = 6
direction_facing = 60
leg_length = 100
n = 0
while (n < n_less_than):
  spider.goto(0,0)
  spider.setheading(direction_facing * n)
  spider.forward(leg_length)
  n = n + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()