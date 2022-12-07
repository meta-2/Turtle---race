from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500 , height=400) #screen.setup is used for set the dimension of screen
user_bet = screen.textinput(title="make your bet", prompt="which Turtle win the race? Enter a color: ") #screen.textinput is used to show the pop up window
colors = ["red","orange","yellow","green","blue","purple"]
y_position = [-70, -40, -10, 20 ,50, 80]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:  #xcordinate
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win! the {winning_color} turtle is the winner")
            else:
                print(f"you loss! the {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()