import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"D:\python\Day 25\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(r"D:\Python\Day 25\50_states.csv")
list_state = data["state"].to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in list_state:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(state_data.x.item(),state_data.y.item())
        tim.write(f"{answer_state}", align= "center",font=("Courier",14,"normal"))
    elif answer_state == "Exit":
        miss_state = []
        for state in list_state:
            if state not in guessed_states:
                miss_state.append(state)
        new_data = pandas.DataFrame(miss_state)
        new_data.to_csv("D:\Python\Day 25\states_to_learn.csv")
        break


