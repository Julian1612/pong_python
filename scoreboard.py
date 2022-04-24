from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 240)
        self.score_player_l = 0
        self.score_player_r = 0
        self.update_score_board()

    def update_score_board(self):
        self.write(f"{self.score_player_l}  :  {self.score_player_r}", align=ALIGNMENT, font=("Courier", 60, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

    def refresh_score_player_1(self):
        self.clear()
        self.score_player_l += 1
        self.update_score_board()

    def refresh_score_player_2(self):
        self.clear()
        self.score_player_r += 1
        self.update_score_board()
