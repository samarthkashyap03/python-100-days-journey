from game_screen import screen_setup
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Setup
my_screen=screen_setup()
paddle_right=Paddle(paddle_position=335)
paddle_left=Paddle(paddle_position=-335)
ball=Ball()
my_screen.listen()
my_screen.onkeypress(paddle_right.move_up,'Up')
my_screen.onkeypress(paddle_right.move_down,'Down')
my_screen.onkeypress(paddle_left.move_up,'w')
my_screen.onkeypress(paddle_left.move_down,'s')
player_right_score=Scoreboard(50)
player_left_score=Scoreboard(-50)

#Main Game Loop
def play()->None:
    while ball.game_is_on:
        time.sleep(0.0001)
        my_screen.update()
        ball.move_ball()#Keep moving the ball forward in respective direction
        #Detect collisions with top and bottom wall
        if  ball.ball_object.ycor()<-340 or ball.ball_object.ycor()>340:
            ball.react_to_wall_collisions()
        #Detect paddle collision
        if ball.ball_object.distance(paddle_right.paddle_object.position())<40 and ball.ball_object.xcor()>315:
            ball.react_to_paddle_collisions()
        if ball.ball_object.distance(paddle_left.paddle_object.position())<40 and ball.ball_object.xcor()<-315:
            ball.react_to_paddle_collisions()
        #Detect if player_right misses the ball
        if ball.ball_object.xcor()>350:
            #player_left score increases
            player_left_score.update_score() 
            ball.reset_ball(winner='B')#resetting ball with a parameter so that ball is served in player_right direction
            #wait time for ball to reset and player gets ready
            for _ in range(40):
                time.sleep(0.01)
                my_screen.update()
            
        #Detect if player left misses the ball
        if ball.ball_object.xcor()<-350:
            #player_right score increases
            player_right_score.update_score()
            ball.reset_ball(winner="A") 
            for _ in range(40):
                time.sleep(0.01)
                my_screen.update()
play()
my_screen.exitonclick()