#Using PySimpleGUI to create GUI for the App
#Importing library
import PySimpleGUI as sg
#We import os in order to acquire working current directory for file opening
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

#Some standard layout to start with basic color theme
sg.change_look_and_feel('LightGrey1')
#Menu definition - template
menu_def = ['&File', ['&New File', '&Open...','Open &Module','---', '!&Recent Files','C&lose']],['&Save',['&Save File', 'Save &As','Save &Copy'  ]],['&Edit', ['&Cut', '&Copy', '&Paste']]
#Function to open Faza Grupowa window and its layout
def open_fg():
    layout = [[sg.Text("Faza Grupowa")]]
    window = sg.Window("FG Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()
#Function to open Drabinka Pucharowa window and its layout
def open_dp():
    layout = [[sg.Text("Drabinka Pucharowa")]]
    window = sg.Window("DP Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()
#Function to open Typowanie window and its layout
def open_t():
    layout = [[sg.Text("Typowanie")]]
    window = sg.Window("T Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()
#Function to open Użytkownicy w bazie window and its layout.
#This function allows for deleting existing users.
def open_wu():
    #Dynamic layout building using list comprehension for text and button   
    try:
        users = open(''.join((__location__, "\\users_data.txt")),'r')
        database = [line.rstrip() for line in users]
    except: 
        sg.Popup('Baza jest pusta!')
        return None
    #TO DO: NEED TO FIGURE OUT DYNAMIC KEY FOR DYNAMIC DELETION OF USERS

    layout = [[[sg.Text(database[i]), sg.Button("Usuń",key="usun")] for i in range(len(database))]]
    window = sg.Window("Użytkownicy w bazie",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "usun": print('ZAKTUALIZUJ DYNAMICZNE USUWANIE')
    window.close()
#Function for adding new users to database file
def open_du():
    layout = [[sg.Text("Enter username"), sg.InputText()], [sg.Submit(),sg.Cancel()]]
    window = sg.Window("Nowy użytkownik",layout)
    event, values = window.read()
    users = open(os.path.join(__location__, "users_data.txt"),'a')
    users.write(values[0]+"\n")
    users.close()
    window.close()
#Function for opening user database and loading it into program
def open_u():
    #Open existing database and load users into program
    layout = [[sg.Button("Wyświel Użytkowników", key = "wu")], [sg.Button("Dodaj Użytkownika", key = "du")]]
    window = sg.Window("U Window",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "wu": open_wu() 
        if event == "du": open_du()          
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



