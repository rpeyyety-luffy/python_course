import turtle as t
import random
tim=t.Turtle()
colours=["CornflowerBlue","DarkOrchid","IndianRed","Blue","Red","Maroon"]
direction=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")
for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen=t.Screen()
screen.exitonclick()#it exits the program after clicking on it