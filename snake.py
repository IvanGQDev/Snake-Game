from turtle import Turtle
from food import COLORS
from random import choice
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0,0),(-20,0), (-40,0)]

class Snake:
    def __init__(self, color = ""):
        self.snakes = []    
        self.color = color
        self.create_snake()
        self.head = self.snakes[0]
        #self.create_snake()

        #we can create a snake in init class or make a other class to create a snake
        #n= 0
        #for i in range(3):
        #    new_snake = Turtle("square")
        #    new_snake.color(self.__color)
        #    new_snake.penup()
        #    new_snake.goto(n, 0)
        #    n += -20
        #    self.__snakes.append(new_snake)

    def create_snake(self):        
        for position in POSITIONS:
            self.add_snake(position)   
    
    def add_snake(self,position):
        new_snake = Turtle("circle")
        new_snake.color(self.color)
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())


    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()    
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(20)

    def snake_color(self):
        color = choice(COLORS)
        for snake in self.snakes:
            snake.color(color)
        
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
