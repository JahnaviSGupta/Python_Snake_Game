from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self): #create the food dot
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len= 0.5)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-295, 295)
        y_cor = random.randint(-295, 295)
        self.goto(x_cor, y_cor)