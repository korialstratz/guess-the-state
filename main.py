import turtle
from turtle import Screen
import pandas
from namer import Namer

# turtle'da mouse koordinatlarını bulma
# def get_mouse_click_coor(x, y):
#   print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop

namer = Namer()
data = pandas.read_csv("50_states.csv")
screen = Screen()
screen.title("US States")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

known_names = 0

# def answer():
#     answer_state = screen.textinput(title=f"{known_names} / 50 states gone", prompt="What's another state's name? ")
#     answer = answer_state.title()
#     return answer

state_list = data["state"].to_list()
guessed_states = []

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{known_names} / 50 states gone", prompt="What's another state's name? ")

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_on = False

    for state in state_list:
        if state == answer_state.title():
            guessed_states.append(state)
            known_names += 1
            known_state = data[data["state"] == answer_state.title()]
            x = known_state.x
            y = known_state.y
            print(x)
            print(y)
            namer.place_name(state, int(x), int(y))
        elif known_names == 50:
            game_on = False
        else:
            pass

screen.exitonclick()
