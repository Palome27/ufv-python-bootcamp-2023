from turtle import (
    Turtle,
)  # Importing Turtle class from turtle module, we're gonna subclass it

# Defining some constants to keep our code clean and easy to understand.
STARTING_POSITION = (0, -280)  # Starting coordinates of the turtle
MOVE_DISTANCE = 20  # Distance moved by the turtle each time
FINISH_LINE_Y = 280  # Y-coordinate of the finish line


# Creating Player class, which is a subclass of Turtle. Yep, our Player is a special kind of Turtle!
class Player(Turtle):
    # Initialize the Player
    def __init__(self):
        super().__init__()  # Initialize our superclass (Turtle)
        self.shape(
            "turtle"
        )  # Our player is shaped like a turtle. Could be a sports car but we're going traditional.
        self.penup()  # We're not drawing anything, so lift that pen up!

        # Move the turtle to its starting position on screen.
        self.go_to_start()

        # Make the turtle face upwards. Default is rightwards. We're not going sideways, we're going up!
        self.setheading(90)

    # Method to move the turtle up by a distance defined in MOVE_DISTANCE
    def go_up(self):
        self.forward(
            MOVE_DISTANCE
        )  # Forward is up for us because we set the heading to 90 (upwards).

    # Send the turtle back to the starting position. Could be used after reaching goal or after a 'life lost'
    def go_to_start(self):
        self.goto(
            STARTING_POSITION
        )  # Using turtle's goto method to move to STARTING_POSITION coordinates

    # Check if the turtle has crossed the finish line
    def is_at_finish_line(self):
        # If y-coordinate of turtle is greater than the y-coordinate of the finish line, you're a winner!
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:  # Else, keep trying, young padawan!
            return False
