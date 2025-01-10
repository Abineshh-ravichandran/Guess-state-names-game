import turtle
from turtle import Screen
import pandas as pd

screen = Screen()
screen.addshape('blank_states_img.gif')
turtle.shape("blank_states_img.gif")
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

df = pd.read_csv("50_states.csv")
states = df.state.to_list()
crt_guesses = []

while len(crt_guesses) < 50:
    correct_state = screen.textinput(title=f"{len(crt_guesses)}/50 States Correct",
                                     prompt="What is another State's name?").title()
    if correct_state == 'Exit':
        with open('missed.csv',mode='w') as missed:
            for i in states:
                if i not in crt_guesses:
                    missed.write(i + "\n")
        break
    if correct_state in states:
        crt_guesses.append(correct_state)
        coordinates = df[df['state'] == correct_state]
        tim.goto(coordinates.x.item(), coordinates.y.item())
        tim.write(correct_state, align='center')


screen.exitonclick()
