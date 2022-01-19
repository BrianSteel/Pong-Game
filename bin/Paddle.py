from .Game_Object import Game_Object

class Paddle(Game_Object):

    def __init__(self, right_x) -> None:
        super().__init__()
        self.window_x = right_x/2 -60

    def move_paddle_left(self, move_distance):
        x = self.xcor()
        if(x < -self.window_x): return -1
        x -= move_distance
        self.setx(x)

    def move_paddle_right(self, move_distance):
        x = self.xcor()
        if(x > self.window_x-15): return -1
        x += move_distance
        self.setx(x)

    def make_paddle_jump(self):
        pass