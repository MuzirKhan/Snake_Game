from turtle import Turtle
import random as r
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        new_x = r.randint(-280, 280)
        new_y = r.randint(-280, 280)
        self.goto(new_x, new_y)
