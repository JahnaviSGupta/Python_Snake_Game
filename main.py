from turtle import Turtle,Screen

from snake import Snake

from food import Food

from scoreboard import Scoreboard

scoreboard= Scoreboard()
screen= Screen()
snake = Snake()
food = Food()
game_is_on=False
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

game_is_on=True
while game_is_on:
    scoreboard.show_score()
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    '''Snake hits the wall'''
    if snake.head.xcor() > 288 or snake.head.xcor()< -288 or snake.head.ycor() > 288 or snake.head.ycor() <-288:
        scoreboard.reset_score()
        snake.reset_snake()

    '''Snake hits its body'''
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
