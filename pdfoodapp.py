from collections import defaultdict
import PySimpleGUI as sg

def dictToString(dict):
  return str(dict).replace('], ','\n\n').replace(', ','\n').replace("'","").replace("[","").replace("]","").replace(": ",":\n")[1:-1]

sg.theme('BluePurple')

layout = [[sg.Text('Where did you try this food?')],
          [sg.Input(key='Country')],
          [sg.Text('What food is it?')],
          [sg.Input(key='Food')],
          [sg.Button('Add Food'), sg.Button('Delete Food'), sg.Button('Display Notebook'), sg.Button('Quit')] ]

window = sg.Window('What new food did you try?', layout)

foodList = defaultdict(list)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Add Food':
        # Update the "output" text element to be the value of "input" element
        country = values['Country']
        food = values['Food']
        if food not in foodList[country]:
            foodList[country].append(food)
            print("Added", food, "to", country)   
    elif event == 'Delete Food':
        # Update the "output" text element to be the value of "input" element
        country = values['Country']
        food = values['Food']
        if food in foodList[country]:
            foodList[country].remove(food)
            print("Deleted", food, "from", country)
        if len(foodList[country]) == 0:
            del foodList[country]
            print("Deleted", country, "from Notebook")
    elif event == "Display Notebook":
        print(dict(foodList))
        sg.Popup("Food Notebook", dictToString(dict(foodList)), keep_on_top=True)
    

window.close()