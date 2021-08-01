from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(
    title="Take your guess", prompt="Which turtle will win the race? Enter a color: "
)
colors = [
    "blue",
    "green",
    "orange",
    "purple",
    "red",
    "yellow",
]
y_positions = [-70, -40, -10, 20, 50, 70]

if user_guess == None or user_guess not in colors:
    user_guess = random.choice(colors)

print(user_guess)
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. The {winning_color} turtle won!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
