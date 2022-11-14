#Using PySimpleGUI to create GUI for the App
#Importing library
import PySimpleGUI as sg
#Some standard layout to start
sg.change_look_and_feel('LightGrey1')
layout = [[sg.Text("Menu")], [sg.Button('Faza Grupowa'), sg.Button('Drabinka Pucharowa'), sg.Button('Typowanie'), sg.Button('Użytkownicy')]]
#We can adjust size manually here, probably will be automatic in the end to match the layout
size = (800,800)
#Create window with defined abouve layout and text 'Demo'
window = sg.Window('Meczystan', layout,ttk_theme='aqua')
#Loop for the GUI - events are passed to variables and depending on their value, something happens
#Here, we break the looop by clicking OK or clicking exit button in the window which break the loop
while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

#We close our super GUI here
window.close()


