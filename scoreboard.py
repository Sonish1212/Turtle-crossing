from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('navy')
        self.level = 0
        self.update()

    def update(self):
        self.goto(-200, 260)
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def score(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align='center', font=FONT)




