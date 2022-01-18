from turtle import Turtle

class Game_Object(Turtle): 
    def __init__(self) -> None:
        super().__init__()
        self.speed(0) # sets the animation speed

    def set_shape(self, shape) -> None:
        self.shape(shape)

    def set_color(self, color):
        self.color(color)

    def set_shape_size(self, length = None, width = None) -> None:
        if length:
            self.shapesize(stretch_len=length)
        if width:
            self.shapesize(stretch_width=width)

    def pen_up(self) -> None:
        self.penup() # gets the drawing pen up

    def set_position(self, x, y) -> None: 
        self.goto(x, y)

    def draw_object(self, shape, color, x=0, y=0, length=None, width=None) -> None: 
        self.set_shape(shape)
        self.set_color(color)
        self.set_shape_size(length, width)
        self.pen_up()
        self.set_position(x, y)

    def move_surfer_left(self, move_distance):
        x = self.xcor()
        if(x < -400): return -1
        x -= move_distance
        self.setx(x)

    def move_surfer_right(self, move_distance):
        x = self.xcor()
        if(x < -400): return -1
        x += move_distance
        self.setx(x)


