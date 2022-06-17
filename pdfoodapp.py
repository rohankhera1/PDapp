from collections import defaultdict
from reprlib import recursive_repr
import PySimpleGUI as sg

# Function to beautify output of list in GUI
def list_to_string(list):
  return str(list).replace(', ','\n').replace("'","").replace("[","").replace("]","")

# Choosing theme of GUI
sg.theme('BluePurple')

food_list = defaultdict(list)

def recipe_screen(food):
    layout = [[sg.T("Ingredient: "), sg.Input(key = 'Ingredient'), sg.Button('Add Ingredient'), sg.Button('Quit')]]
    window = sg.Window("Add Recipe", layout, modal=True)
    while True:
        event, ingredient = window.read()
        if event == sg.WIN_CLOSED or event == 'Quit':
            return
        food_list[food].append(ingredient)

# Layout of GUI on launch
layout = [[sg.Text('What food did you try?')],
          [sg.Input(key='Food')],
          [sg.Button('Add Food'), sg.Button('Delete Food'), sg.Button('Display Notebook'), sg.Button('Add Recipe'), sg.Button('Quit')] ]


window = sg.Window('What new food did you try?', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Add Food':
        food = values['Food']
        if food not in food_list:
            food_list[food] = []
            print("Added", food, "to notebook")
    elif event == 'Add Recipe':
        food = values['Food']
        if food not in food_list:
            print("Food not in food_list!")
            sg.Popup("Food not in food_list!")
        else:
            recipe_screen(food)
    elif event == 'Delete Food':
        food = values['Food']
        if food in food_list:
            del(food_list[food])
            print("Deleted", food, "from Notebook")
    elif event == "Display Notebook":
        print((dict(food_list)))
        sg.Popup("Food Notebook", list_to_string(dict(food_list)))
    

window.close()