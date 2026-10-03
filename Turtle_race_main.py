#Turtle race
from turtle import Turtle,Screen
import random

is_race_on=False
screen = Screen()
screen.setup(width=500, height=400)#allows to set up width and height of the window
screen.bgcolor("lightblue")#colour of the background of the screen
user_bet=screen.textinput(title="Make a bet",prompt="Which turtle will win the race?Enter a colour: ")
#.textinput allows to add the popup before the program that allows the user to enter
colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])#for position of the turtle you give x value and y value
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            print(turtle.color())
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you have won! the {winning_color} turtle is the winner!")
            else:
                print(f"you have lost the {winning_color} turtle is the winner!")



        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()