from turtle import Turtle
from random import choice,randint

COLORS = ["green","white","blue","yellow","purple","orange","red","brown"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(choice(COLORS))
        self.speed("fastest")
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        self.color(choice(COLORS))
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)