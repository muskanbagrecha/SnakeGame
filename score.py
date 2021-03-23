from turtle import Turtle
import winsound
FONT = ('Arial', 15, 'normal')
ALIGNMENT = "CENTER"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align='center', font=FONT)

    def game_over(self):
        winsound.Beep(frequency=1500, duration=700)
        self.setposition(0, 0)
        self.write("GAME OVER!", align='center', font=FONT)
