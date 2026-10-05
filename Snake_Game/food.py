from turtle import Turtle
import random


class Food(Turtle):#in bracket the class we want to inherit from

    def __init__(self):
        super().__init__()#it is the super clss so it goes to thaty class first
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)