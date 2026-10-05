import turtle as turtle_module
import random

turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list=[(239, 242, 247), (245, 240, 231), (246, 239, 244), (237, 245, 241), (200, 158, 118), (60, 96, 130)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(colour_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen=turtle_module.Screen()
screen.exitonclick()