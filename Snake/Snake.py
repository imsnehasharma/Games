import turtle
import time
import random
import winsound

delay = 0.1


#Creating Screen
win = turtle.Screen()
win.title("SNAKE")
win.bgcolor("black")
win.setup(width=600,height=600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

segments = [head]

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.shapesize(0.5, 0.5)
food.goto(random.randint(-290,250),random.randint(-290,250))

#Eyes
eye1 = turtle.Turtle()
eye1.speed(0)
eye1.shape("circle")
eye1.color("maroon")
eye1.penup()
eye1.shapesize(0.5, 0.5)
eye1.goto(7, 7)

eye2 = turtle.Turtle()
eye2.speed(0)
eye2.shape("circle")
eye2.color("maroon")
eye2.penup()
eye2.shapesize(0.5, 0.5)
eye2.goto(-7, 7)



#Borders
bd = turtle.Turtle()
bd.speed(0)
bd.color("white")
bd.hideturtle()
bd.penup()
bd.goto(-290,250)
bd.pendown()
bd.goto(290,250)
bd.goto(290,-290)
bd.goto(-290,-290)
bd.goto(-290,250)
bd.penup()

#Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()


def update_score(nscore):
  score = max_score()

  with open("Games\Snake\Score.txt", 'w') as f:
    if int(nscore) > int(score):
        f.write(str(nscore))
    else:
        f.write(str(score))

# Returns the max score from the Score.txt file
def max_score():
  with open("Games\Snake\Score.txt", 'r') as f:
    lines = f.readlines()
    score = lines[0].strip()

  return int(score)

score = 0
hscore = max_score()


def print_score(score,hscore):
  pen.clear()
  pen.goto(-220,250)
  pen.write("Score: {}".format(score),align="center", font=("Candara",18,"normal"))
  pen.goto(200,250)
  pen.write("High Score: {}".format(hscore),align="center", font=("Candara",18,"bold"))
print_score(score,hscore)


#Function to move the snake
def move():
    if head.direction == "up":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y + 10)
        eye1.goto(head.xcor()+7, head.ycor()+7)
        eye2.goto(head.xcor()-7, head.ycor()+7)
 
    if head.direction == "down":
        y = head.ycor() #y coordinate of the turtle
        head.sety(y - 10)
        eye1.goto(head.xcor()+7, head.ycor()-7)
        eye2.goto(head.xcor()-7, head.ycor()-7)
 
    if head.direction == "right":
        x = head.xcor() #x coordinate of the turtle
        head.setx(x + 10)
        eye1.goto(head.xcor()+7, head.ycor()+7)
        eye2.goto(head.xcor()+7, head.ycor()-7)
 
    if head.direction == "left":
        x = head.xcor() #x coordinate of the turtle
        head.setx(x - 10)
        eye1.goto(head.xcor()-7, head.ycor()+7)
        eye2.goto(head.xcor()-7, head.ycor()-7)

def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"

def add_segment():
  new_segment = turtle.Turtle()
  new_segment.speed(0)
  new_segment.shape("circle")
  new_segment.penup()
  new_segment.color("green")
  if len(segments) == 1:
    new_segment.color("white")
  segments.append(new_segment)
add_segment()


def die():
  time.sleep(1)
  global delay
  delay = 0.1
  head.goto(0, 0)
  eye1.goto(7, 7)
  eye2.goto(-7, 7)
  head.direction = "stop"

  global segments
  # Hide the segments
  for segment in segments[1:]:
    segment.goto(1000, 1000) 
  # clear segment list
  segments = [head]
  add_segment()
  print_score(score,hscore)

def play_sound(occurrence):
  if occurrence == 'dead':
    winsound.PlaySound("Games\Sound Effects\lose.wav", winsound.SND_ASYNC)
  if occurrence == 'score':
    winsound.PlaySound("Games\Sound Effects\win.wav",winsound.SND_ASYNC)

   


 
  




#Keyboard Bindings
win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

while True:
    win.update()
    move()
    time.sleep(delay)

    if head.distance(food) < 15:
    # move the food to a random position on screen
      x = random.randint(-270, 240)
      y = random.randint(-270, 240)
      food.goto(x, y)
      add_segment()
      delay-=0.001
      score += 10

      print_score(score,hscore)
      play_sound('score')
    
    for index in range(len(segments)-1, 0, -1):
      x = segments[index-1].xcor()
      y = segments[index-1].ycor()
      segments[index].goto(x, y)



    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 240 or head.ycor() < -280:
      
      if score > hscore:
        hscore = score
        score = 0
      play_sound('dead')
      die()


    for segment in segments[2:]:
      if segment.distance(head) < 10:
        if score > hscore:
          hscore = score
        score = 0
        play_sound('dead')
        die()

    update_score(hscore)
