from turtle import Screen
from user import User
from wall import Wall
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)

user = User()
wall = Wall()
ball = Ball()

screen.listen()
screen.onkey(key='Right', fun=user.right)
screen.onkey(key='Left', fun=user.left)
#
continua = True
while continua:
    screen.update()
    ball.moving()

    #Check paddle collision:
    if ball.distance(user.user_paddle[0].position()) < 35 and ball.ycor() > -260:
        ball.paddle_touch()

    # Check side-wall collision:
    if ball.xcor() >= 360 or ball.xcor() <= -360:
        ball.side_wall_touch()

    # Check great wall collision:
    for piece in wall.wall:
        if ball.distance(piece) < 50:
            ball.great_wall_touch()
            piece.color('black')
            wall.wall.remove(piece)
            print(len(wall.wall))
        if len(wall.wall) == 0:
            ball.winner()


    # Check out of bounds:
    if ball.ycor() <= -280:
        ball.out_of_bounds()
        continua = False


screen.exitonclick()