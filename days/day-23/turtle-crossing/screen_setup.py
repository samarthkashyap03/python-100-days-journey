from turtle import Screen
def set_screen()->object:
    """
    Sets the screen, can be used for games
    """
    screen=Screen()
    screen.bgcolor('white')
    screen.setup(width=600,height=600)
    return screen