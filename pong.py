from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Pong(Turtle):
    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(starting_pos)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)



