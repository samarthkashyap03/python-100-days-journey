from screen_setup import set_screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time

#---------Setup-----------------
screen=set_screen()
screen.tracer(0)
player=Player()
score=Scoreboard()
screen.listen()
screen.onkeypress(player.move,'w')

#--------Main Game Loop---------
def play():
    CAR_SPEED=0.1 #Set the initial speed of the car animation
    LOOP_COUNT=0 #Counter to keep track of loop execution
    INCREMENT=0.01
    COLLISION_CONSTANT=20 #If the distance between the player and car is less than this number, then game over

    while player.game_is_on:
        time.sleep(CAR_SPEED)
        screen.update()
        #Spawn cars every 10th time the loop runs
        if LOOP_COUNT%10==0:
            car=Car()
            Car.CARS.append(car)
        #Move the car_objects
        car.move_cars()
        #Detect collision with cars
        for car in Car.CARS:
            if player.player.distance(car.car_body)<COLLISION_CONSTANT:
                score.game_over()
                player.game_is_on=False
        #Detect if player reaches the other end
        if player.has_player_won(): #if the player has reached finish line, then:
            score.update_score() #Update score by 1
            player.reset_position() #Reset the player to init position
            CAR_SPEED-=INCREMENT #Increase the speed by decreasing the timer offset
        LOOP_COUNT+=1
        screen.update()
play() 
screen.exitonclick()