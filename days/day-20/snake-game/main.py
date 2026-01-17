from screen_setup import screen_setup
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen=screen_setup()
screen.tracer(0)#control animations
snake_game=Snake()#Init the snake class
snake_game.create_snake_body() #Create a snake body with 3 blocks
food=Food() #Initialise food class, with food being rendered at random location
score=Score()
screen.listen()
#Start listening to Keyboard inputs
screen.onkey(snake_game.move_left,'Left')
screen.onkey(snake_game.move_right,'Right')
screen.onkey(snake_game.move_up,'Up')
screen.onkey(snake_game.move_down,'Down')
def play():
    while snake_game.game_is_on:
        time.sleep(0.06)
        screen.update()
        #Keep the snake moving
        snake_game.forward()
        snake_head=snake_game.snake_head
        #Detect collision with food, if collided, create food at a new location
        #Increase score by 1
        if snake_head.distance(food.food)<20:
            score.refresh_score()#Update the score
            snake_game.extend_snake()#Increase the length of the snake by 1 block
            food.render_food()
        #Detect wall collisions
        #If snake head hits wall, game Ends.
        if snake_head.xcor()>290 or snake_head.xcor()<-290 or snake_head.ycor()>290 or snake_head.ycor()<-290:
            score.reset()#Reset the scoreboard
            snake_game.reset_snake()
            time.sleep(1)
            food.render_food()
            
        #Detect Tail collision
        for segment in snake_game.segments[1:]:
            if snake_head.distance(segment)<10:
                #If the head collides with its own body:
                score.reset()#Reset the scoreboard
                snake_game.reset_snake()
                food.render_food()
                
play()
screen.exitonclick()
