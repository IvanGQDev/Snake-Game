from turtle import Turtle
FONT = ("Cascadia Code", 20, "normal")

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 250)
        self.score = 0
        self.color("white")
        self.penup()
        self.write(arg=f"Score: {self.score}",align="center",font=("Cascdia Code", 20, "normal"))
        self.hideturtle()
    
    def increment_score(self):
        self.clear()
        self.score += 10
        self.write(arg=f"Score: {self.score}",align="center",font=("Cascdia Code", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over :C",align="center",font=FONT)