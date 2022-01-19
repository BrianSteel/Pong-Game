from .Game_Object import Game_Object
from random import choice


class Ball(Game_Object):

    direction_coefficient_x = 1
    direction_coefficient_y = 1

    def __init__(self) -> None:
        super().__init__()
        self.direction_coefficient_x = choice([-1, 1])
        self.direction_coefficient_y = choice([-1, 1])

    def set_dx(self, dx):
        self.dx = dx

    def set_dy(self, dy):
        self.dy = dy

    def move_ball(self, change):
        ball_x, ball_y = self.xcor(), self.ycor()
        self.set_dx(change)
        self.set_dy(change)
        if ball_x > 290:
            self.direction_coefficient_x = -1
        if ball_x < -290:
            self.direction_coefficient_x = 1
        if ball_y > 365:
            self.direction_coefficient_y = -1
        if ball_y < -365:
            self.direction_coefficient_y = 1
        ball_new_x, ball_new_y = (
            ball_x + self.direction_coefficient_x * self.dx,
            ball_y + self.direction_coefficient_y * self.dy,
        )
        self.setx(ball_new_x)
        self.sety(ball_new_y)
