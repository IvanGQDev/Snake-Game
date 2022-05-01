from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score_board
from random import choice
import time


screen = Screen()
screen.setup(width=600, height =600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

user_choice = screen.textinput(title="Select", prompt="Which color do you want? :")
snake = Snake(color=user_choice)
food = Food()
score = Score_board()
screen.update()


screen.listen()
screen.onkey(snake.move_up, 'w')
screen.onkey(snake.move_down, 's')
screen.onkey(snake.move_left, 'a' )
screen.onkey(snake.move_right, 'd')

game_is_on =  True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #verify if snake eat food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score()
        snake.extend()
        if score.score % 2 == 0:
            for i in range(5):
                snake.snake_color()

    #verify if snake out of screen
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.game_over()
        game_is_on = False

    #verify if snake eat herself
    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False


screen.exitonclick()