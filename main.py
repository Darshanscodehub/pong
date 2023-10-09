from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


def draw_dotted_line(line_length, gap_length):
    from turtle import Turtle  # Import Turtle class locally within the function
    dotted_line = Turtle()
    dotted_line.speed("fastest")
    dotted_line.color("white")
    dotted_line.penup()
    dotted_line.goto(0, -400)  # Start at the bottom of the screen
    dotted_line.setheading(90)  # Point upwards
    dotted_line.pendown()
    dotted_line.pensize(2)

    num_segments = 800 // (line_length + gap_length)  # Calculate the number of segments

    for _ in range(num_segments):
        dotted_line.forward(line_length)
        dotted_line.penup()
        dotted_line.forward(gap_length)
        dotted_line.pendown()

    dotted_line.hideturtle()


r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

draw_dotted_line(20, 10)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect the collision on the ball with the top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lpoint()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint()
screen.exitonclick()
