from turtle import Screen
from paddle import Paddle
from  ball import Ball
from scoreboard import Score
import time

sc=Screen()
sc.tracer(0)
sc.setup(height=600, width=800)
sc.bgcolor("Black")
sc.title("PONG_GAME")


r_paddle=Paddle((380,0))
l_paddle=Paddle((-390,0))
ball =Ball()
score=Score()

sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")
sc.onkey(l_paddle.go_up, "w")
sc.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    sc.update()
    ball.move()
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor() >330 or ball.distance(l_paddle) <50 and ball.xcor() <-330:
        ball.bounce_x()
    # detect r_paddle misses
    if ball.xcor()>380 :
        ball.reset_position()
        score.l_point()
    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




sc.exitonclick()