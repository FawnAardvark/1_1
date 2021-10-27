#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)
  t.pendown()

#  
startx = -70
starty = 0
direction = 45

#
for t in my_turtles:
  new_color = turtle_colors.pop()
  t.color(new_color)
  t.penup()
  t.goto(startx, starty)
  t.right(45)
  t.setheading(direction)
  t.pendown()
  t.forward(50)


#	
  direction -= 45
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()