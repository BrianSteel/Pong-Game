from bin.helper import *
from bin.constants import *

# variables
window_pause = False

# create game window
game_window = create_window("Pong on Steroids (Ah Not Really!!)", "black", WINDOW_WIDTH, WINDOW_HEIGHT)
# create paddle 1 and 2
paddle_1 = create_paddle(WINDOW_WIDTH, PADDLE_SHAPE, PADDLE_COLOR, PADDLE_X, WINDOW_HEIGHT/2 - 5, PADDLE_LENGTH)
paddle_2 = create_paddle(WINDOW_WIDTH, PADDLE_SHAPE, PADDLE_COLOR, PADDLE_X, -(WINDOW_HEIGHT/2 -13), PADDLE_LENGTH)
# create ball 1
ball_1 = create_ball(BALL_MOVEMENT_LIMITER, BALL_SHAPE, BALL_COLOR, BALL_X, BALL_Y)

# listen to windows key presses
game_window.listen()
game_window.onkeypress(lambda: paddle_1.move_paddle_left(PADDLE_MOVEMENT_LIMITER), 'a')
game_window.onkeypress(lambda: paddle_1.move_paddle_right(PADDLE_MOVEMENT_LIMITER), 'd')
game_window.onkeypress(lambda: paddle_2.move_paddle_left(PADDLE_MOVEMENT_LIMITER), 'Left')
game_window.onkeypress(lambda: paddle_2.move_paddle_right(PADDLE_MOVEMENT_LIMITER), 'Right')
# game_window.onkey(pause_window, 'space')

try: 
    while not window_pause:
        game_window.update()
        current_paddle_1_coor = paddle_1.get_current_coor()
        current_paddle_2_coor = paddle_2.get_current_coor()
        ball_1.move_ball(current_paddle_1_coor, current_paddle_2_coor)

except: 
    print("Terminating the Game Window.")

# if name == "__main__":
#     run_game()
