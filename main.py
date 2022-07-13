from turtle import Screen
from pong import Pong
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_pong = Pong((350, 0))
l_pong = Pong((-350, 0))
ball = Ball()
score_board = Scoreboard()
screen.listen()
screen.onkeypress(r_pong.up, "Up")
screen.onkeypress(r_pong.down, "Down")

screen.onkeypress(l_pong.up, "w")
screen.onkeypress(l_pong.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # to be placed after the modifications are done
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with the pongs
    if ball.distance(r_pong) < 50 and ball.xcor() > 320:
        ball.bounce_pong()

    if ball.distance(l_pong) < 50 and ball.xcor() < -320:
        ball.bounce_pong()

    # Detect out of bounds
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()
        time.sleep(1)

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
        time.sleep(1)
    print(ball.move_speed)


screen.exitonclick()