from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setheading(90)
        self.penup()
        self.goto(x, y)

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)