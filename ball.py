from turtle import Turtle, Screen
import  random

screen = Screen()
BALL = [10, 20, 30, -10, -20, -30]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.goto(random.choice(BALL), random.choice(BALL))
        self.color("white")
        self.y = 10
        self.x = 10

    def refresh(self):
        x_cor = self.xcor() + self.x
        y_cor = self.ycor() + self.y
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1