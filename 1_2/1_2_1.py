# a121_catch_a_turtle.py
#-----import statements-----
import random as rand
import turtle as trtl
import turtle as score_writer
import turtle as counter
#-----game configuration----
score = 0
spot_color = "cyan"
spot_size = 2
spot_shape = "circle"
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----

score_writer.speed(0)
score_writer.penup()
score_writer.goto(-250, 250)
score_writer.hideturtle()

counter.speed()
counter.penup()
counter.goto(-250, 250)
counter.hideturtle()

spot = trtl.Turtle()
spot.speed(0)
spot.penup()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
#-----game functions--------
def spot_clicked(x, y):
    update_score(x, y)
    change_position()
def change_position():
    new_xpos = rand.randint(-350, 350)
    new_ypos = rand.randint(-300, 300)
    spot.goto(new_xpos, new_ypos)
def update_score(x, y):
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


#-----events----------------
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()

#------high scores-------------
# 1. 42
# 2. 41
# 3. 41
# 4. 
# 5. 
