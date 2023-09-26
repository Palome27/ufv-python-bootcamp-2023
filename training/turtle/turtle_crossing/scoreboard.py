from turtle import Turtle  # Importing the Turtle class from the turtle module

FONT = (
    "ARIAL",
    50,
    "bold",
)  # Setting the font properties: Font family, size, and style


# Scoreboard inherits from the Turtle class. You could say Scoreboard is a kind of Turtle!
class Scoreboard(Turtle):
    # Initialize the scoreboard when it's created
    def __init__(self):
        super().__init__()  # Initialize the turtle part of me
        self.level = 1  # We start at level 1, folks! Newbie land.

        # Turtle starts out visible, but our scoreboard doesn't need to be a turtle.
        # So we hide the turtle (i.e., ourselves) from view.
        self.hideturtle()

        self.penup()  # Pick up the pen so it doesn't draw. We're not Picasso here, we're just writing text!

        # Set the starting position for the scoreboard at top-left of the screen
        self.goto(-280, 250)

        # Update the screen with the current level
        self.update_scoreboard()

    # Update the displayed level on the screen
    def update_scoreboard(self):
        self.clear()  # Clear any previous level text, make it a clean slate!

        # Write the current level to the screen at the position set in __init__
        # align="left" keeps our text aligned to the left side of our turtle
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # Called when the player successfully crosses the screen
    def increase_level(self):
        self.level += 1  # Advance to the next level, the challenge intensifies!

        # Update the level displayed on the screen
        self.update_scoreboard()

    # When the game is over, let's write that on the screen
    def game_over(self):
        # Center the turtle for our dramatic Game Over message
        self.goto(0, 0)

        # Write "GAME OVER" to the screen, in a moment of sorrow or perhaps relief
        self.write(f"GAME OVER", align="center", font=FONT)
