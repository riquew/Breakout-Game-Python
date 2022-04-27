from turtle import Turtle


class User:
    def __init__(self):
        self.user_paddle = []
        self.make_user_paddle()

    def make_user_paddle(self):
        user = Turtle('square')
        user.color('white')
        user.shapesize(stretch_wid=1, stretch_len=5)
        user.penup()
        user.goto(x=0, y=-270)
        self.user_paddle.append(user)

    def left(self):
        if self.user_paddle[0].xcor() > -340:
            new_x = self.user_paddle[0].xcor() - 20
            self.user_paddle[0].goto(new_x, self.user_paddle[0].ycor())

    def right(self):
        if self.user_paddle[0].xcor() < 340:
            new_x = self.user_paddle[0].xcor() + 20
            self.user_paddle[0].goto(new_x, self.user_paddle[0].ycor())


