
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

l_paddle = Paddle(370, 0)
r_paddle = Paddle(-380, 0)
ball = Ball()
screen = Screen()
score = Scoreboard()

game_on = True

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Jong")

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")

while game_on:

    score.update_score_board()
    ball.move()

    print(ball.BALL_SPEED)

    if ball.ycor() >= 275 or ball.ycor() <= -275:
        ball.change_direction()

    if ball.xcor() > 280 and ball.distance(l_paddle) < 40:
        ball.colition_with_paddle_r()
        ball.BALL_SPEED += 2

    if ball.xcor() < -280 and ball.distance(r_paddle) < 40:
        ball.colition_with_paddle_l()
        ball.BALL_SPEED += 2

    if ball.xcor() > 400:
        ball = Ball()
        ball.direction = 115
        ball.move()
        score.refresh_score_player_1()

    if ball.xcor() < -420:
        ball = Ball()
        ball.direction = 45
        ball.move()
        score.refresh_score_player_2()

screen.exitonclick()
