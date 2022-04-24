from turtle import Turtle
ANGEL = 45
ANGEL_PADDLE = 115


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed(0)
        self.penup()
        self.direction = 45
        self.BALL_SPEED = 10

    def move(self):
        self.setheading(self.direction)
        self.forward(self.BALL_SPEED)
        print(self.direction)

    def change_direction(self):
        if self.direction == 45:
            self.direction = -45
        elif self.direction == -45:
            self.direction = 45
        elif self.direction == -115:
            self.direction = 115
        elif self.direction == 115:
            self.direction = -115

    def colition_with_paddle_r(self):
        if self.direction == 45:
            self.direction = 115
        else:
            self.direction = -115

    def colition_with_paddle_l(self):
        if self.direction == 115:
            self.direction = 45
        else:
            self.direction = -45
