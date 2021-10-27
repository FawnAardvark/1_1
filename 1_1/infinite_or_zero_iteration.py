#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

t = trtl.Turtle()
t.speed(0)

# Add a loop with a zero-iteration condition
x = 5 # This is the line you need to change.

while (x < 5): 
  t.pendown()
  t.circle(5)
  t.penup()
  t.forward(20)
  x = x + 1

# Add an infinite loop
x = 4 # This is the line you need to change.

while (x < 5): 
  t.pendown()
  t.circle(5)
  t.penup()
  t.forward(20)
  x = x - 1

wn = trtl.Screen()
wn.mainloop()