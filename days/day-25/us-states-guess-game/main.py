from screen_setup import *
from GameEngine import GameEngine
from scoreboard import Scoreboard

#Constants
map_image='blank_states_img.gif'

#-------------Setup------------
screen=screen_setup()
image=display_image()
game=GameEngine()
score=Scoreboard()

#-------------Main Loop----------
def main():
    while game.lives>0:
        user_input=screen.textinput(title='Enter a state',prompt='Enter the name of the state to be guessed').title()
        if user_input in game.state_list:
            xcor,ycor=game.determine_coordinates(user_input)
            game.write_to_coordinates(xcor,ycor)
            score.update_score()
            score.update_highscore()
        else:
            game.lives-=1
        screen.mainloop()
        
if __name__=='__main__':
    main()