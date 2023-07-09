import turtle
import winsound


single = False

wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("lime green")
p1.shapesize(stretch_wid=5,stretch_len=1)
p1.penup()
p1.goto(-350,0)

#Paddle B
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("cyan")
p2.shapesize(stretch_wid=5,stretch_len=1)
p2.penup()
p2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = 0.2
ball.dy = 0.2

#Score
score_1 = 0
score_2 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()


#Border Line
bd = turtle.Turtle()
bd.speed(0)
bd.color("white")
bd.hideturtle()
bd.penup()
bd.goto(-400,250)
bd.pendown()
bd.goto(400,250)
bd.penup()



#Functions

def p1_up():
    y = p1.ycor()
    y += 60
    p1.sety(y)

def p1_down():
    y = p1.ycor()
    y -= 60
    p1.sety(y)

def p2_up():
    y = p2.ycor()
    y += 60
    p2.sety(y)

def p2_down():
    y = p2.ycor()
    y -= 60
    p2.sety(y)

def print_score(single,score1,score2):
    #Check if mode is Single Player or Multiplayer
    if single == True:
        Player1 = "Player"
        Player2 = "CPU"
    else:
        Player1 = "Player 1"
        Player2 = "Player 2"
    pen.clear()
    pen.color("sea green")
    pen.goto(-335,260)
    pen.write("{} : {}".format(Player1, score1),align="left", font=("Century Gothic",24,"bold"))
    pen.color("sky blue")
    pen.goto(335,260)
    pen.write("{} : {}".format(Player2, score2),align="right", font=("Century Gothic",24,"bold"))
print_score(single, score_1, score_2)

def play_sound(occurrence):
    if occurrence == 'collision':
        winsound.PlaySound("Games\Sound Effects\impact.wav", winsound.SND_ASYNC)
    if occurrence == 'score':
        winsound.PlaySound("Games\Sound Effects\win.wav",winsound.SND_ASYNC)

def check_single():
    global single
    single = not single
    print_score(single, score_1, score_2)

def single_player():
    if single == True:
        if ball.xcor() > 0:
            if ball.ycor() > p2.ycor():
                p2_up()
            if ball.ycor() < p2.ycor():
                p2_down()


#Keyboard binding
wn.listen()
wn.onkeypress(p1_up,"w")
wn.onkeypress(p1_down,"s")
wn.onkeypress(p2_up,"Up")
wn.onkeypress(p2_down,"Down")
wn.onkeypress(check_single,"space")


#Main game loop

while True:
  wn.update()

  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  if single == True:
    single_player()

#Border checking

  if ball.ycor() > 240:
      ball.sety(240)
      ball.dy *= -1
      play_sound('collision')
  if ball.ycor() < -290:
      ball.sety(-290)
      ball.dy *= -1
      play_sound('collision')
  if ball.xcor() > 390:
      ball.goto(0,0)
      ball.dx *= -1
      score_1 += 1
      print_score(single, score_1, score_2)
      play_sound('score')
  if ball.xcor() < -390:
      ball.goto(0,0)
      ball.dx *= -1
      score_2 += 1
      print_score(single, score_1, score_2)
      play_sound('score')
      

#Paddle not colliding with borders
  if p2.ycor() > 200:
      p2.sety(200)
  if p2.ycor() < -240:
      p2.sety(-240)
  if p1.ycor() > 200:
      p1.sety(200)
  if p1.ycor() < -240:
      p1.sety(-240)


#Paddle and ball collisions

  if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < p2.ycor() + 70 and ball.ycor() > p2.ycor() - 70):
      ball.setx(340)
      ball.dx *= -1
      play_sound('collision')
  
  if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < p1.ycor() + 70 and ball.ycor() > p1.ycor() - 70):
      ball.setx(-340)
      ball.dx *= -1
      play_sound('collision')
