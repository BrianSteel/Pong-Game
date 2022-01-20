from .Game_Object import Game_Object
from random import choice


class Ball(Game_Object):

    direction_coefficient_x = 1
    direction_coefficient_y = 1

    def __init__(self) -> None:
        super().__init__()
        self.direction_coefficient_x = choice([-1, 1])
        self.direction_coefficient_y = choice([-1, 1])

    def set_dxy(self, change): 
        self.dx = change
        self.dy = change

    def move_ball(self, change, paddle_1_coor, paddle_2_coor):
        # get current ball coordinates
        ball_x, ball_y = self.xcor(), self.ycor()

        # set dx and dy
        self.set_dxy(change)

        # handle x or length window boundary 
        if ball_x > 290:
            self.direction_coefficient_x = -1
        if ball_x < -290:
            self.direction_coefficient_x = 1

        # handle y or height window boundary
        if ball_y > 365:
            ball_x = 0
            ball_y = 0
            self.direction_coefficient_y = -1
        if ball_y < -365:
            ball_x = 0
            ball_y = 0
            self.direction_coefficient_y = 1

        # handle collision with paddle
        # solve by naming the each boundary and each position of ball and paddle 1 and 2
        # then handle the conditions
        if ball_y > paddle_1_coor[1] - 20 and ball_x < paddle_1_coor[0] + 50 and ball_x > paddle_1_coor[0] -50:
            self.direction_coefficient_y = -1
        if ball_y < paddle_2_coor[1] + 20 and ball_x < paddle_2_coor[0] + 50 and ball_x > paddle_2_coor[0] -50:
            self.direction_coefficient_y = 1



        # calculate new ball positions
        ball_new_x, ball_new_y = (
            ball_x + self.direction_coefficient_x * self.dx,
            ball_y + self.direction_coefficient_y * self.dy,
        )

        # set new ball position
        self.setx(ball_new_x)
        self.sety(ball_new_y)
