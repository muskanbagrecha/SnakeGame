from turtle import Turtle

import winsound

FONT = ('Arial', 15, 'normal')
ALIGNMENT = "CENTER"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscores.txt", mode='r') as file:
            self.highscore = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}    High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}    High Score = {self.highscore}", align='center', font=FONT)

    def reset_game(self):
        winsound.Beep(frequency=1500, duration=700)
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscores.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()
