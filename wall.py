from turtle import Turtle

COLORS = ['red', 'yellow', 'green']


class Wall:
    def __init__(self):
        self.wall = []
        self.make_wall()
        #print(len(self.wall))

    def make_wall(self):
        xpos = -360
        ypos = 280
        num_color = 0
        for i in range(54):
            wall_piece = Turtle('square')
            wall_piece.color(COLORS[num_color])
            wall_piece.shapesize(stretch_wid=1, stretch_len=4)
            wall_piece.penup()
            wall_piece.goto(x=xpos, y=ypos)
            xpos += 90
            self.wall.append(wall_piece)
            if i == 8 or i == 17 or i == 26 or i == 35 or i == 44 or i== 53:
                ypos -= 30
                xpos = -360
                if i == 17 or i == 35:
                    num_color += 1

