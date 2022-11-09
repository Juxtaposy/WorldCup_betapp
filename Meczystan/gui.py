#Using PySimpleGUI to create GUI for the App
#Importing library
import PySimpleGUI as sg
#Some standard layout to start
layout = [[sg.Text('Tekst dolny')], [sg.Button('OK')]]
#Create window with defined abouve layout and text 'Demo'
window = sg.Window('Demo', layout)
#Loop for the GUI - events are passed to variables and depending on their value, something happens
#Here, we break the looop by clicking OK or clicking exit button in the window which break the loop
while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

#We close our super GUI here
window.close()


