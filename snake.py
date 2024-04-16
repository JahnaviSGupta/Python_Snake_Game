from turtle import Turtle,Screen
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()
MOVE_DISTANCE= 20
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,coordinates):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(coordinates)
        self.segments.append(snake)
    screen.update()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(self.segments) - 1, 0,-1):  # 2-1-0 (start stop step)  [segment - 1 because lenght is 3 and we want 2 to 0]
             # at position x_y=[(0,0),(-20,0),(-40,0)] --- 2,1,0 respectively
            new_x = self.segments[seg_num - 1].xcor()  # seg at position 1
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)  # segment 2 will goto coordinate of segment 1 i.e (-20,0)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != 270:
          self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
         self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
           self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
          self.head.setheading(0)










