import turtle
from turtle import Screen,Turtle
import pandas
FONT =("Courier", 12, "normal")
screen = Screen()
screen.title("US STATES GAME")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data_states = pandas.read_csv("50_states.csv")
x = data_states.state.to_list()

guessed_state = []
is_game_on =True
while len(guessed_state)<50 and is_game_on:
     


    answer = (screen.textinput(f"GUESS THE STATE  {len(guessed_state)}/50", "WHAT IS YOUR ANOTHER COUNTRY?")).title()


    for i in x:

        if i == answer:
            guessed_state.append(answer)

            new_state = Turtle()
            new_state.penup()
            new_state.hideturtle()

            p = data_states[data_states.state == answer]
            new_state.goto(int(p.x),int(p.y))
            new_state.write(f" {answer}", align="center", font=FONT)
        elif answer == "Exit":
            is_game_on = False

        





