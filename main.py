import turtle
from unicodedata import name 
from bin.Game_Object import Game_Object 

# def run_game():
game_window = turtle.Screen()
game_window.title("Pong on Steroids (Ah Not Really!!)")
game_window.bgcolor("black")
game_window.setup(width=960, height=750)
# stops the window from updating and makes the game faster
game_window.tracer(0) 

# Surfer Board A
surfer_1 = Game_Object()
surfer_1.draw_object("square", "white", 0, 350, 5)

# Surfer Board B
surfer_2 = Game_Object()
surfer_2.draw_object("square", "white", 0, -350, 5)

# ball
ball_1 = Game_Object()
ball_1.draw_object("circle", "blue", 0, 0)

# listen to windows key presses
game_window.listen()
game_window.onkeypress(lambda : surfer_1.move_surfer_left(20), 'a')
game_window.onkeypress(lambda: surfer_1.move_surfer_right(20), 'd')
game_window.onkeypress(lambda: surfer_2.move_surfer_left(20), 'Left')
game_window.onkeypress(lambda: surfer_2.move_surfer_right(20), 'Right')

try: 
    while True:
        game_window.update()
except: 
    print("Terminating the Game Window.")

# if name == "__main__":
#     run_game()
