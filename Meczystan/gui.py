#Using PySimpleGUI to create GUI for the App
#Importing library
import PySimpleGUI as sg
#Some standard layout to start with basic color theme
sg.change_look_and_feel('LightGrey1')
#Menu definition - template
menu_def = ['&File', ['&New File', '&Open...','Open &Module','---', '!&Recent Files','C&lose']],['&Save',['&Save File', 'Save &As','Save &Copy'  ]],['&Edit', ['&Cut', '&Copy', '&Paste']]

def open_fg():
    layout = [[sg.Text("Faza Grupowa")]]
    window = sg.Window("FG Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def open_dp():
    layout = [[sg.Text("Drabinka Pucharowa")]]
    window = sg.Window("DP Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def open_t():
    layout = [[sg.Text("Typowanie")]]
    window = sg.Window("T Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def open_u():
    layout = [[sg.Text("Użytkownicy")]]
    window = sg.Window("U Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

#Main function
def main():
    #Horizontal layout definition for buttons
    layout = [[sg.Menu(menu_def)], [sg.Button('Faza Grupowa',key="fg"), sg.Button('Drabinka Pucharowa',key="dp"), sg.Button('Typowanie',key="t"), sg.Button('Użytkownicy',key="u")]]
    #Create window with control parameters for the App
    window = sg.Window('Meczystan', layout)

    #Some options for the User to do
    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "fg": open_fg()
        if event == "dp": open_dp()
        if event == "t": open_t()
        if event == "u": open_u()
    window.close()

if __name__ == "__main__":
    main()



