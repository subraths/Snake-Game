from turtle import Screen, heading
from snake import Snake
from food import Food
from score_board import Score_Board
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Score_Board()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (
        snake.head.xcor() > 380
        or snake.head.xcor() < -380
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_on = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
