from turtle import (
    Turtle,
)  # Importing the Turtle class because our cars are also going to be turtles! 🐢🚗
import random  # Gonna use this to add some unpredictability to our game

# Defining some constants that we'll use
COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
]  # Cars can be of any of these colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of our cars
MOVE_INCREMENT = 10  # Speed increase each time we "level up"


# CarManager class is the big boss here. It handles everything related to our cars.
class CarManager:
    # Initializer method, like a car factory assembly line
    def __init__(self):
        self.all_cars = []  # A list to store all the car objects we create
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    # Time to make a car! But we're feeling lucky—only a 1 in 6 chance to actually make one each time
    def create_car(self):
        random_chance = random.randint(1, 25)  # Roll the dice
        if (
            random_chance == 1
        ):  # If we roll a 1, we create a car. It's like car lottery!
            new_car = Turtle(
                "square"
            )  # Our car shape is a square (or a rectangle when we stretch it)
            new_car.shapesize(
                stretch_wid=1, stretch_len=2
            )  # Stretch it to make it look like a car
            new_car.penup()  # Lift the pen because we don't want tire tracks
            new_car.color(random.choice(COLORS))  # Randomly color our car
            random_y = random.randint(
                -250, 250
            )  # Random y-coordinate within our screen limits
            new_car.goto(
                300, random_y
            )  # Position our car on the rightmost part of the screen
            self.all_cars.append(new_car)  # Add the new car to our list of all cars

    # SEE we leave some space in the bottom and the top for the game to be playable

    # Move the cars from right to left, or "forward" in turtle terms but we're using backward to go left!
    def move_cars(self):
        for car in self.all_cars:  # For each car in our all_cars list
            car.backward(
                self.car_speed
            )  # Move the car leftward (backward) at the current speed

    # Level up = Faster cars. Who said life gets easier?
    def level_up(self):
        self.car_speed += MOVE_INCREMENT  # Increase the speed of our cars
