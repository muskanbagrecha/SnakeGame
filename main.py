from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
import winsound
FREQUENCY = 1000
DURATION = 100

screen = Screen()
screen.setup(600, 600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        snake.increase_snake_size()
        food.update_food()
        score.update_score()
        winsound.Beep(frequency=FREQUENCY, duration=DURATION)
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.game_over()
        game_on=False
    for seg in snake.all_segments[1:]:
        if snake.head.distance(seg)<10:
            score.game_over()
            game_on=False
            break
screen.exitonclick()
