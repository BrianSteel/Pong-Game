import turtle
from bin.Ball import Ball 
from bin.Paddle import Paddle 

# constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 750
PADDLE_LENGTH = 5
PADDLE_MOVEMENT_LIMITER = 20
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_X = 0
BALL_SHAPE = "circle"
BALL_COLOR = "blue"
BALL_X, BALL_Y = 0, 0
BALL_MOVEMENT_LIMITER = 0.3

# variables
window_pause = False

def pause_window():
    global window_pause # global must be mentioned
    print(window_pause)
    window_pause = not window_pause
    print(window_pause)

# def run_game():
game_window = turtle.Screen()
game_window.title("Pong on Steroids (Ah Not Really!!)")
game_window.bgcolor("black")
game_window.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
# stops the window from updating and makes the game faster
game_window.tracer(0) 

# paddle Board A
paddle_1 = Paddle(WINDOW_WIDTH)
paddle_1.draw_object(PADDLE_SHAPE, PADDLE_COLOR, PADDLE_X, WINDOW_HEIGHT/2 - 5, PADDLE_LENGTH)

# paddle Board B
paddle_2 = Paddle(WINDOW_WIDTH)
paddle_2.draw_object(PADDLE_SHAPE, PADDLE_COLOR, PADDLE_X, -(WINDOW_HEIGHT/2 -13), PADDLE_LENGTH)

# ball
ball_1 = Ball()
ball_1.draw_object(BALL_SHAPE, BALL_COLOR, BALL_X, BALL_Y)
# ball_1.set_delta_xy(2)

# listen to windows key presses
game_window.listen()
game_window.onkeypress(lambda: paddle_1.move_paddle_left(PADDLE_MOVEMENT_LIMITER), 'a')
game_window.onkeypress(lambda: paddle_1.move_paddle_right(PADDLE_MOVEMENT_LIMITER), 'd')
game_window.onkeypress(lambda: paddle_2.move_paddle_left(PADDLE_MOVEMENT_LIMITER), 'Left')
game_window.onkeypress(lambda: paddle_2.move_paddle_right(PADDLE_MOVEMENT_LIMITER), 'Right')
game_window.onkeypress(pause_window, 'space')

try: 
    while not window_pause:
        game_window.update()
        current_paddle_1_coor = paddle_1.get_current_coor()
        current_paddle_2_coor = paddle_2.get_current_coor()
        ball_1.move_ball(BALL_MOVEMENT_LIMITER, current_paddle_1_coor, current_paddle_2_coor)

except: 
    print("Terminating the Game Window.")

# if name == "__main__":
#     run_game()
