import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)
# starting location of the tower
y = -150
# height of tower and a counter for each floor
num_floors = 63
floor = 0
# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  painter.goto(-150, y)
  if (floor == 21)
  y = -150
  if (floor > 21):
    painter.goto(-100, y)
  if (floor == 42)
  y = -150
  if (floor > 42):
    painter.goto(-50, y)
  painter.color("gray")
  rem = floor % 6
  if (rem > 2):
    painter.color("blue")
  y = y + 5 # location of next floor
  floor = floor + 1
   #draw the floor
  painter.pendown()
  painter.forward(50)
wn = trtl.Screen()
wn.mainloop()