import turtle

from bin.Ball import Ball 
from bin.Paddle import Paddle 


def create_window(title, color, width, height):
    game_window = turtle.Screen()
    game_window.title(title)
    game_window.bgcolor(color)
    game_window.setup(width=width, height=height)
    game_window.tracer(0) 
    return game_window

def create_paddle(window_width, shape, color, x, y, length):
    paddle = Paddle(window_width)
    paddle.draw_object(shape, color, x, y, length)
    return paddle

def create_ball(speed, shape, color, x, y):
    ball = Ball(speed)
    ball.draw_object(shape, color, x, y)
    return ball

# def pause_window():
#     global window_pause # global must be mentioned
#     print(window_pause)
#     window_pause = not window_pause
#     print(window_pause)