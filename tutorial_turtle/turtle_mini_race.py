import turtle
import random
import sys

# turtles
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)


# homes
player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)

die = [1, 2, 3, 4, 5, 6]

# Loop will run 20 times
for i in range(20):
    print(sys.modules)
    # Check if the position of player_one is greater than or equal to the coordinate (300, 100)
    if player_one.pos() >= (300, 100):
        # If the above condition is met, this means player_one has reached or passed the coordinate (300, 100)
        # Announce that player_one wins and exit the loop
        print("Player One Wins!")
        break

    # Check if the position of player_two is greater than or equal to the coordinate (300, -100)
    elif player_two.pos() >= (300, -100):
        # If the above condition is met, this means player_two has reached or passed the coordinate (300, -100)
        # Announce that player_two wins and exit the loop
        print("Player Two Wins!")
        break

    else:
        # If neither of the above conditions is met, the game continues

        # Player_one's turn to roll the die
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        # Move player_one forward based on the die roll multiplied by 20
        player_one.fd(20 * die_outcome)

        # Player_two's turn to roll the die
        player_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        # Move player_two forward based on the die roll multiplied by 20
        player_two.fd(20 * die_outcome)
