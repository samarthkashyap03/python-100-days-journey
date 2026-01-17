from turtle import Turtle
class Player:
    #CONSTANTS
    STARTING_POINT=-280 #starting posittion of Player
    ENDING_POINT=280 #Ending position of Player
    FORWARD_DISTANCE=12 #Distance a player has to move wach time when pressed 'W' Key
    PLAYER_HEADING=90 #Direction the player has to face (NORTH)
    
    def __init__(self):
        """Sets up a player_object, shaped as a turtle, can be modified \n
        Methods:\n
        1.move() - moves the player with a distance specified\n
        2.reset_position() - resets the position of the player to init\n
        3.has_player_won() - checks if the player has one, returns true or false"""
        self.player=Turtle(shape='turtle')
        self.player.penup()
        self.player.color('black')
        self.player.setheading(Player.PLAYER_HEADING)
        self.reset_position()
        self.game_is_on=True
    def move(self)->None:
        self.player.forward(Player.FORWARD_DISTANCE)
    def reset_position(self)->None:
        self.player.sety(Player.STARTING_POINT)
    def has_player_won(self)->bool:
        return self.player.ycor()>Player.ENDING_POINT
    


        