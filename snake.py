from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for i in START_POSITION:
            self.add_segment(i)


    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def increase_snake_size(self):
        self.add_segment(self.all_segments[-1].position())

    def move_snake(self):
        for segno in range(len(self.all_segments)-1,0,-1):
            x = self.all_segments[segno-1].xcor()
            y = self.all_segments[segno-1].ycor()
            self.all_segments[segno].goto(x,y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

