import turtle

win = turtle.Screen()
win.title('pong')
win.bgcolor("black")
win.setup(width = 800,height=600)
win.tracer(1)

#score
score_a = 0
score_b = 0


#pad1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape("square")
pad1.color("white")
pad1.shapesize(stretch_wid = 5 ,stretch_len = 1)
pad1.penup()
pad1.goto(-350,0)
#pad2
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape("square")
pad2.color("white")
pad2.shapesize(stretch_wid = 5 ,stretch_len = 1)
pad2.penup()
pad2.goto(350,0)
pad2.dy = 3
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#pan
pan = turtle.Turtle()
pan.speed(0)
pan.color("white")
pan.penup()
pan.hideturtle()
pan.goto(-190,260)
pan.write('Palyer A: 0 Player B: 0',font = ("Courier", 24 , "normal"))


#fnuction
def pad1_up():
    y = pad2.ycor()
    y += 20
    pad2.sety(y)

def pad1_down():
    y = pad2.ycor()
    y -= 20
    pad2.sety(y)    
#keyboard
win.listen()
win.onkeypress(pad1_up,"w") 
win.onkeypress(pad1_down,"s")   

#main loop
while True:
    win.update()
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #move pad2
    pad1.sety(ball.ycor())
    #border cheaking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dy *= -1
        score_a += 1
        pan.clear()
        pan.write(f'Palyer A: {score_a} Player B: {score_b}',font = ("Courier", 24 , "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pan.clear()
        pan.write(f'Palyer A: {score_a} Player B: {score_b}',font = ("Courier", 24 , "normal"))
    #pad and ball 
    if ball.xcor() < -340 and ball.ycor() < pad1.ycor() + 50 and ball.ycor() > pad1.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < pad2.ycor() + 50 and ball.ycor() > pad2.ycor() - 50:
        ball.dx *= -1


'''
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor()):
           ball.setx(340)
           ball.dx *= -1
    elif ball.xcor() > 340 and ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() - 40:       
           ball.setx(340)
           ball.dx *= -1       
'''           