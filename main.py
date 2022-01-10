import turtle
import pandas
from pandas._libs import missing

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=800, height=600)
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(data.state):

    answer_state = screen.textinput(
        title=f"{len(guessed_states)} / {len(data.state)} States", prompt="What's another state's name?\nOr\nType 'exit' to quit and generate\na file 'states_to_learn.scv'").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.scv")

        screen.bye()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())
        t.write(answer_state)


turtle.mainloop()
