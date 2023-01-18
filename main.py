import turtle
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
screen = Screen()
screen.setup(1200, 600)
screen.bgcolor('black')
screen.tracer(0)

paddle_1 = Paddle(-580, 0)
paddle_2 = Paddle(580, 0)
ball = Ball()
"""Key listener"""
screen.listen()
screen.onkey(paddle_1.up, 'Up')
screen.onkey(paddle_1.down, 'Down')
screen.onkey(paddle_2.up, 'w')
screen.onkey(paddle_2.down, 's')

game_start = True
while game_start:
    time.sleep(0.1)
    screen.update()
    ball.refresh()

    """Ball bounce """
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 540 or ball.distance(paddle_1) < 50 and ball.xcor() < -540:
        ball.bounce_x()



# net_list = []
# net_position = [(0, -20), (0, -50), (0, -80), (0, -110), (0, -140),
#                 (0, 20), (0, 50), (0, 80), (0, 110), (0, 140), (0, 160), (0, 190)]
#
# for position in net_position:
#     net = Turtle()
#     net.penup()
#     net.shape('square')
#     net.color('white')
#     net.goto(position)
#     net_list.append(net)
screen.exitonclick()