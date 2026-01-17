from Turtle_Race import TurtleRace
def play():
    colors=['red','green','yellow','blue','brown','orange']
    turtle_race=TurtleRace(colors)
    user_input=turtle_race.ask_input()
    turtle_race.generate_turtles()
    turtle_race.set_initial_position()
    winner=turtle_race.start_race()
    if turtle_race.verify_bet(bet=user_input,winner=winner):
        print("You Win!!")
    print(f"{winner.pencolor()} Turtle Reached first!")
play()