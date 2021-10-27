#members: Gabriel Puebla, Willyigham Bahou, Haruto Hirai

#determining the equation

#intro
print("Hello, this is a graphing calculator for y = mx + b !")
#ask the y-intercrept
slope = int(input("What is the slope of the graph? :"))
y_intercept = int(input("What is the y-intercept of the graph? : "))
#return the equation of graph
print("So, the equation of the graph is", "y =", slope, "x", "+", y_intercept)


#making the graph
import turtle as trtl
t = trtl.Turtle()
t.speed(0)
t.pensize(1)
t.color("grey")
y = -400
while y < 400:
    t.penup()
    t.goto(0, y)
    t.pendown()
    t.forward(400)
    t.backward(800)
    y = y + 10

t.left(90)

x = -400
while x < 400:
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.forward(400)
    t.backward(800)
    x = x + 10
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(5)
t.color("black")
t.forward(400)
t.backward(800)
t.goto(0, 0)
t.right(90)
t.forward(400)
t.backward(800)
t.goto(0, 0)




#y - intercept
t.goto(0,0)

real_y_intercept = y_intercept * 10 

t.goto(0, real_y_intercept)

real_slope = slope * 10

#slope

t.penup()

for i in range(80): 
    t.forward(10)
    t.left(90)
    t.forward(real_slope)
    t.right(90)
t.pendown()
t.color("red")
t.goto(0, real_y_intercept)

t.right(180)
t.penup()

for i in range(80): 
    t.forward(10)
    t.left(90)
    t.forward(real_slope)
    t.right(90)
t.pendown()
t.color("red")
t.goto(0, real_y_intercept)


t.hideturtle()

wn = trtl.Screen()
wn.mainloop()

#humor

