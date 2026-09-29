import turtle as t
import random
tim=t.Turtle()
colours=["CornflowerBlue","DarkOrchid","IndianRed","Blue","Red","Maroon"]
def draw_shape(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.left(angle)

for shape in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape)
screen=t.Screen()
screen.exitonclick()#