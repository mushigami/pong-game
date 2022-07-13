from turtle import Turtle

MOVE_DISTANCE = 10
SCREEN_HEIGHT = 600


class Ball(Turtle):
    def __init__(self, starting_pos=(0, 0)):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(starting_pos)
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_pong(self):
        self.x_move *= -1
        self.move_speed *= 0.9 if self.move_speed > 0.001 else 0.001

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_pong()
        self.move_speed = 0.1


