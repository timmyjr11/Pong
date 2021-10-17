import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by timmyjr11")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
left_score = 0
right_score = 0

# paddle Left
paddle_Left = turtle.Turtle()
paddle_Left.speed(0)
paddle_Left.shape("square")
paddle_Left.color("white")
paddle_Left.shapesize(stretch_wid=5, stretch_len=1)
paddle_Left.penup()
paddle_Left.goto(-350, 0)

# paddle Right
paddle_Right = turtle.Turtle()
paddle_Right.speed(0)
paddle_Right.shape("square")
paddle_Right.color("white")
paddle_Right.shapesize(stretch_wid=5, stretch_len=1)
paddle_Right.penup()
paddle_Right.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = -0.08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Left Player: 0  Right Player: 0", align="center", font=("Courier", 16, "normal"))

# Quit Notice
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(0, 245)
pen2.write("press u to end game", align="center", font=("Courier", 12, "normal"))


# function
def paddle_left_up():
    y = paddle_Left.ycor()
    y += 20
    paddle_Left.sety(y)


def paddle_left_down():
    y = paddle_Left.ycor()
    y -= 20
    paddle_Left.sety(y)


def paddle_right_up():
    y = paddle_Right.ycor()
    y += 20
    paddle_Right.sety(y)


def paddle_right_down():
    y = paddle_Right.ycor()
    y -= 20
    paddle_Right.sety(y)


def quit():
    global running
    running = False


# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_left_up, "w")
wn.onkeypress(paddle_left_down, "s")
wn.onkeypress(paddle_right_up, "Up")
wn.onkeypress(paddle_right_down, "Down")
wn.onkeypress(quit, "u")
# Game Loop

running = True

while running:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check the Boarder
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        left_score += 1
        pen.clear()
        pen.write("Left Player: {}  Right Player: {}".format(right_score, left_score), align="center",
                  font=("Courier", 16, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        right_score += 1
        pen.clear()
        pen.write("Left Player: {}  Right Player: {}".format(right_score, left_score), align="center",
                  font=("Courier", 16, "normal"))

        # Ball collision with paddles
    if 340 < ball.xcor() < 350 and (paddle_Right.ycor() + 40 > ball.ycor() > paddle_Right.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if -340 > ball.xcor() > -350 and (paddle_Left.ycor() + 40 > ball.ycor() > paddle_Left.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
