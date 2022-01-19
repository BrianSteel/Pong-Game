import turtle
from bin.Ball import Ball 
from bin.Paddle import Paddle 


# def run_game():
game_window = turtle.Screen()
game_window.title("Pong on Steroids (Ah Not Really!!)")
game_window.bgcolor("black")
game_window.setup(width=600, height=750)
# stops the window from updating and makes the game faster
game_window.tracer(0) 

# paddle Board A
paddle_1 = Paddle(600)
paddle_1.draw_object("square", "white", 0, 370, 5)

# paddle Board B
paddle_2 = Paddle(600)
paddle_2.draw_object("square", "white", 0, -362, 5)

# ball
ball_1 = Ball()
ball_1.draw_object("circle", "blue", 0, 0)
# ball_1.set_delta_xy(2)

# listen to windows key presses
game_window.listen()
game_window.onkeypress(lambda : paddle_1.move_paddle_left(20), 'a')
game_window.onkeypress(lambda: paddle_1.move_paddle_right(20), 'd')
game_window.onkeypress(lambda: paddle_2.move_paddle_left(20), 'Left')
game_window.onkeypress(lambda: paddle_2.move_paddle_right(20), 'Right')

try: 
    while True:
        game_window.update()
        ball_1.move_ball(0.5)

except: 
    print("Terminating the Game Window.")

# if name == "__main__":
#     run_game()
