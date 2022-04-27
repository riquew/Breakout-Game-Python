from turtle import Turtle
from random import choice
MOVEMENT = (1, -1)
ALIGN = 'center'
FONT = ('Arial', 100, 'bold')


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.goto(x=0, y=-245)
        self.moving()
        self.flash = 0.1



    def moving(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)
        if self.ycor() >= 280:
            self.y_move *= -1
        elif self.ycor() <= -280:
            self.out_of_bounds()

    def paddle_touch(self):
        # random_mov = choice(MOVEMENT)
        # self.x_move *= random_mov
        self.y_move *= -1

    def side_wall_touch(self):
        self.x_move *= -1

    def great_wall_touch(self):
        random_mov = choice(MOVEMENT)
        self.x_move *= random_mov
        self.y_move *= -1

    def out_of_bounds(self):
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=-50)
        self.write(f'YOU LOST', move=False, align=ALIGN, font=FONT)

    def winner(self):
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=-50)
        self.write(f'YOU WON!', move=False, align=ALIGN, font=FONT)

