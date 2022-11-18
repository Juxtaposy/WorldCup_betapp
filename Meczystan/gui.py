#Using PySimpleGUI to create GUI for the App
#Importing library
import PySimpleGUI as sg
#We import os in order to acquire working current directory for file opening
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
#We import pickle to save user objects in a file for database purposes
import pickle

#Class for users
class Users:
    #We keep track of created users in order to avoid name conflicts
    instances = []
    #Constructor
    def __init__(self,name: str) -> None:
        self.name = name
        #Placeholder
        self.typy_gr = [] #Faza grupowa
        self.typy_p = []  #Faza pucharowa
        Users.instances.append(self)

#Class for Groups creation
class Kraj:
    def __init__(self,name: str) -> None:
        self.name = name
        self.table = [['RM', 'W', 'R', 'P', 'BZ', 'BS', 'RB', 'Pkt'], [0, 0, 0, 0, 0, 0, 0, 0]]
    def updatescore(self,list: list) -> None:
        self.table[1] = list
    def __str__(self) -> str:
        return f'{self.name} ma obecnie statystyki:\n\
        Rozegrane Mecze:    {self.table[1][0]}\n\
        Wygrane:            {self.table[1][1]}\n\
        Remisy:             {self.table[1][2]}\n\
        Przegrane:          {self.table[1][3]}\n\
        Bramki zdobyte:     {self.table[1][4]}\n\
        Bramki stracone:    {self.table[1][5]}\n\
        Bilans Bramkowy:    {self.table[1][6]}\n\
        Punkty:             {self.table[1][7]}\n'
class Grupy:
    def __init__(self,letter,team1,team2,team3,team4) -> None:
        self.letter = letter
        self.table = [['RM', 'W', 'R', 'P', 'BZ', 'BS', 'RB', 'Pkt']]


#Nations and groups definition
Katar = Kraj('Katar')
Ekwador = Kraj('Ekwador')
Senegal = Kraj('Senegal')
Holandia = Kraj('Holandia')
Grupa_A = Grupy('A',Katar,Ekwador,Senegal,Holandia)


Anglia = Kraj('Anglia')
Iran = Kraj('Iran')
USA = Kraj('USA')
Walia = Kraj('Walia')
Grupa_B = Grupy('B',Anglia,Iran,USA,Walia)

Argentyna = Kraj('Argentyna')
Arabia_Saudyjska = Kraj('Arabia Saudyjska')
Meksyk = Kraj('Meksyk')
Polska = Kraj('Polska')
Grupa_C = Grupy('C',Argentyna,Arabia_Saudyjska,Meksyk,Polska)


Francja = Kraj('Francja')
Australia = Kraj('Australia')
Dania = Kraj('Dania')
Tunezja = Kraj('Tunezja')
Grupa_D = Grupy('D',Francja,Australia,Dania,Tunezja)

Hiszpania = Kraj('Hiszpania')
Kostaryka = Kraj('Kostaryka')
Niemcy = Kraj('Niemcy')
Japonia = Kraj('Japonia')
Grupa_E = Grupy('E',Hiszpania,Kostaryka,Niemcy,Japonia)

Belgia = Kraj('Belgia')
Kanada = Kraj('Kanada')
Maroko = Kraj('Maroko')
Chorwacja = Kraj('Chorwacja')
Grupa_F = Grupy('F',Belgia,Kanada,Maroko,Chorwacja)

Brazylia = Kraj('Brazylia')
Serbia = Kraj('Serbia')
Szwajcaria = Kraj('Szwajcaria')
Kamerun = Kraj('Kamerun')
Grupa_G = Grupy('G',Brazylia,Serbia,Szwajcaria,Kamerun)

Portugalia = Kraj('Portugalia')
Ghana = Kraj('Ghana')
Urugwaj = Kraj('Urugwaj')
Korea_Południowa = Kraj('Korea Południowa')
Grupa_H = Grupy('H',Portugalia,Ghana,Urugwaj,Korea_Południowa)

print(Katar)

#Some standard layout to start with basic color theme
sg.change_look_and_feel('LightGrey1')

#Menu definition - template
menu_def = ['&File', ['&New File', '&Open...','Open &Module','---', '!&Recent Files','C&lose']],['&Save',['&Save File', 'Save &As','Save &Copy'  ]],['&Edit', ['&Cut', '&Copy', '&Paste']]

#Read database file
def db_read():
    try:
        file = open(''.join((__location__, "\\users_data.pkl")),'rb')
        database = pickle.load(file)
        file.close()
        return database
    except:
        database = []
        return database
#Write database file
def db_write(database):
    file = open(''.join((__location__, "\\users_data.pkl")),'wb')
    pickle.dump(database,file,pickle.HIGHEST_PROTOCOL)
    file.close()

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
def open_wu():
    #Dynamic layout building using list comprehension for text and button
    database = db_read()   
    if not database:
        sg.Popup('Baza jest pusta!')
    else:
        layout = [[[sg.Text(i.name), sg.Button("Usuń",key="usun")] for i in database]]
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
    database = db_read()
    if database:
        for obj in database:
            if values[0] == obj.name: 
                sg.Popup('Nazwa zajęta, wybierz inną!')
                values[0] = False
    if values[0]: 
        obj = Users(values[0])
        database.append(obj)
        db_write(database)
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



