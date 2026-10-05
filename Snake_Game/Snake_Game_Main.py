from turtle import Screen
from typing import overload

from scoreboard import Scoreboard
from snake import Snake
from food import Food

import time

#screen setup done
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)#screen.tracer is used to turn of the animation

snake=Snake()
food=Food()
scoreboard = Scoreboard()


screen.listen()#to start listening for key strokes
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



#S2 move the Snake
game_is_on = True
while game_is_on:
    screen.update()# Eliminates Lag & Flickering When drawing complex scenes or multiple objects
    time.sleep(0.1)  # adds a 1 second delay after one segment moves
    snake.move()

    #detect collision with Food
    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.game_over()

        #detect collision with tail.
        #if the head collides with any segement in the tail:
        #trigger the game over

        #slicing concept [1:3] from position 1 to 3 it will give everything
        #[1:4:2] same concept as above but the 2 in the end tells that form the list form 1 to 4 it will
        #give the number incrimenting by 2...inshort will skip a number in between
    for segment in snake.segments[1:]:  #using slicing
        if  snake.head.distance(segment)< 10:
                game_is_on = False
                scoreboard.game_over()



screen.exitonclick()