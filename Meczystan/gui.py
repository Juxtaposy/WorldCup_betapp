#Using PySimpleGUI to create GUI for the App
#Importing library
import PySimpleGUI as sg
#We import os in order to acquire working current directory for file opening
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
#We import pickle to save user objects in a file for database purposes
import pickle

#Class for Users
class Users:
    #We keep track of created users in order to avoid name conflicts
    instances = []
    #Constructor
    def __init__(self,name: str,password: str) -> None:
        self.name = name
        self.__password = password
        #Placeholder
        self.typy_gr = {k: '0' for k in range(96)} #Faza grupowa
        self.typy_p = {}  #Faza pucharowa
        Users.instances.append(self)
    #Method for password check
    def checkpass(self,attempt: str) -> bool:
        if attempt == self.__password: return True
        else: return False

#Class for match pairs
class Mecz():
    id = 0
    def __init__(self,team1,team2) -> None:
        self.team1 = team1
        self.team2 = team2
        self.name = f'{team1.name} - {team2.name}'
        self.score = [0,0]
        self.status = False
        self.id = Mecz.id
        Mecz.id += 1
    def updatescore(self,v1: int,v2: int) ->None:
        self.score = [v1,v2]
    def __str__(self) -> str:
        if self.status:
            return (f'{self.team1.name} {self.score[0]} - {self.score[1]} {self.team2.name}')
        else:
            return f'{self.team1.name} - - - {self.team2.name}'
    
    
#Class for Groups creation
class Kraj:
    def __init__(self,name: str) -> None:
        self.name = name.center(40)
        self.table = [['RM', 'W', 'R', 'P', 'BZ', 'BS', 'RB', 'Pkt'], [0, 0, 0, 0, 0, 0, 0, 0]]
    def updatescore(self,list: list) -> None:
        self.table[1] = list
    def __str__(self) -> str:
        return f'{self.name}:\n\
        Rozegrane Mecze:     {self.table[1][0]}\n\
        Wygrane:                  {self.table[1][1]}\n\
        Remisy:                    {self.table[1][2]}\n\
        Przegrane:                {self.table[1][3]}\n\
        Bramki zdobyte:        {self.table[1][4]}\n\
        Bramki stracone:       {self.table[1][5]}\n\
        Bilans Bramkowy:      {self.table[1][6]}\n\
        Punkty:                     {self.table[1][7]}\n'

class Grupy:
    def __init__(self,letter,team1,team2,team3,team4) -> None:
        #Setting name of a group and nations within it
        self.letter = letter
        self.team1 = team1
        self.team2 = team2
        self.team3 = team3
        self.team4 = team4
        #List of matches in a group
        self.matches = [Mecz(self.team1,self.team2), Mecz(self.team3,self.team4),
         Mecz(self.team1,self.team3), Mecz(self.team4,self.team2),
         Mecz(self.team2,self.team3), Mecz(self.team4,self.team1)]
    def __str__(self) -> str:
        return f'{self.team1.name}\n{self.team2.name}\n{self.team3.name}\n{self.team4.name}\n'

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
Arabia_Saudyjska = Kraj('Arabia Saud.')
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
Korea_Południowa = Kraj('Korea Płd.')
Grupa_H = Grupy('H',Portugalia,Ghana,Urugwaj,Korea_Południowa)

#A list of created group objects
gr_list = [Grupa_A,Grupa_B,Grupa_C,Grupa_D,Grupa_E,Grupa_F,Grupa_G,Grupa_H]

#Some standard layout to start with basic color theme
sg.change_look_and_feel('LightGrey1')

#Menu definition - template
menu_def = ['&File', ['&New File', '&Open...','Open &Module','---','!&Recent Files','C&lose']],\
    ['&Save',['&Save File', 'Save &As','Save &Copy'  ]],['&Edit', ['&Cut', '&Copy', '&Paste']]

#Read database file
def db_read():
    try:
        file = open(''.join((__location__, "\\users_data.pkl")),'rb')
        database= pickle.load(file)
        file.close()
        return database
    except:
        database = {}
        return database
#Write database file
def db_write(database):
    file = open(''.join((__location__, "\\users_data.pkl")),'wb')
    d = {database[k].name: database[k] for k in range(len(database))}
    pickle.dumps(d,file,pickle.HIGHEST_PROTOCOL)
    file.close()

#Function to display Nations in given group and display their statistics
def open_gr(Grupa):
    layout = [[sg.Text(f"Drużyny w grupie {Grupa.letter}",pad = (270,20))], [sg.Text(Grupa.team1.__str__(),pad=(70,0)),
    sg.Text(Grupa.team2.__str__(),pad=(70,0))], [sg.Text(Grupa.team3.__str__(),pad=(70,0)), sg.Text(Grupa.team4.__str__(),pad=(70,0))] ]
    window = sg.Window("",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

#Function to open Faza Grupowa window and its layout
def open_g():
    layout = [[sg.Button("Grupa A",pad=(70,0),key='A'), sg.Button("Grupa B",pad=(70,0),key='B')], [sg.Text(Grupa_A), sg.Text(Grupa_B)],
    [sg.Button("Grupa C",pad=(70,0),key='C'), sg.Button("Grupa D",pad=(70,0),key='D')], [sg.Text(Grupa_C), sg.Text(Grupa_D)],
    [sg.Button("Grupa E",pad=(70,0),key='E'), sg.Button("Grupa F",pad=(70,0),key='F')], [sg.Text(Grupa_E), sg.Text(Grupa_F)],
    [sg.Button("Grupa G",pad=(70,0),key='G'), sg.Button("Grupa H",pad=(70,0),key='H')], [sg.Text(Grupa_G), sg.Text(Grupa_H)]]

    window = sg.Window("",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "A": open_gr(gr_list[0])
        if event == "B": open_gr(gr_list[1])
        if event == "C": open_gr(gr_list[2])
        if event == "D": open_gr(gr_list[3])
        if event == "E": open_gr(gr_list[4])
        if event == "F": open_gr(gr_list[5])
        if event == "G": open_gr(gr_list[6])
        if event == "H": open_gr(gr_list[7])
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
    window = sg.Window("",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()
def open_log():
    layout = [[sg.Text("Wprowadz nazwe uzytkownika"), sg.InputText()],[sg.Text("Wprowadz haslo"), sg.InputText(password_char="*")], [sg.Submit(),sg.Cancel()]]
    window = sg.Window("Logowanie",layout)
    database = db_read()
    user = []
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        if not database:
            sg.Popup('Baza jest pusta!')
            break
        if not values[0] or not values[1]:
            sg.Popup('Wprowadz nazwe uzytkownika i haslo')
        if values[0] and values[1]:
            for i in database:
                if values[0] in i.name:
                    if i.checkpass(values[1]):
                        sg.Popup(f'Zalogowano {i.name}')
                        user = i
                        window.close()
                        return user
                    else:
                        sg.Popup('Zle hasło!')
                else: sg.Popup("Brak uzytkownika o podanej nazwie"); break    
    window.close()
#Function to open Użytkownicy w bazie window and its layout.
def open_wu():
    #Dynamic layout building using list comprehension for text and button
    database = db_read()   
    
    if not database:
        sg.Popup('Baza jest pusta!')
    else:
        layout = [[sg.Text(i.name)] for i in database]
        values = [i.name for i in database]
        window = sg.Window("Użytkownicy w bazie",layout)
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
        window.close()

#Function for adding new users to database file
def open_du():
    layout = [[sg.Text("Enter username"), sg.InputText()],[sg.Text("Enter password"), sg.InputText(password_char="*")], [sg.Submit(),sg.Cancel()]]
    window = sg.Window("Nowy użytkownik",layout)
    database = db_read()
    check = True
    while True:
        event, values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
                break  
        if not values[0] or not values[1]:
            sg.Popup('Wprowadz nazwe uzytkownika i haslo')
            check = False
            
        if database:
            for obj in database:
                if values[0] == obj.name: 
                    sg.Popup('Nazwa zajeta')
                    check = False        
        if check: 
            obj = Users(values[0],values[1])
            database.append(obj)
            db_write(database)
            break
    window.close()

def open_uu():
    layout = [[sg.Text("Enter username"), sg.InputText()],[sg.Text("Enter password"), sg.InputText()], [sg.Submit(),sg.Cancel()]]
    window = sg.Window("Usuwanie Uzytkownika",layout)
    database = db_read()
    if not database:
        sg.Popup('Baza jest pusta')
    else:  
    
        while True:
            event, values = window.read()
            if event == "Cancel" or event == sg.WIN_CLOSED:
                    break  
            
            if not values[0] or not values[1]:
                sg.Popup('Wprowadz nazwe uzytkownika i haslo')
                check = False   
            if database:
                for obj in database:
                    if values[0] == obj.name and obj.checkpass(values[1]):
                        sg.Popup('Uzytkownik usuniety')
                        database.remove(obj)
                        db_write(database)
                        break       
    window.close()

#Function for opening user database and loading it into program
def open_u():
    #Open existing database and load users into program
    layout = [[sg.Button("Wyświetl Użytkowników", key = "wu")], [sg.Button("Dodaj Użytkownika", key = "du")], [sg.Button("Usun Uzytkownika", key = 'uu')]]
    window = sg.Window("",layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "wu": open_wu() 
        if event == "du": open_du()     
        if event == "uu": open_uu()       
    window.close()

#Function to dynamically add matches from individual groups to display in window by open_fg()
def add_mgr(ind,obj,user):
    ll = ['A','B','C','D','E','F','G','H']
    if not user: 
        obj.append([sg.Text(f'Mecze grupy {ll[ind]}')])
        m = [[sg.Text(gr_list[ind].matches[i].__str__())] for i in range(6)]
    if user: 
        obj.append([sg.Text(f'Mecze grupy {ll[ind]}'),sg.Button("Typuj",key = 'type')])
        m = [[sg.InputText(size=(3,1)), sg.Text(f'({user.typy_gr[2*i]})',font='bold'), sg.Text(gr_list[ind].matches[i].__str__()), sg.Text(f'({user.typy_gr[2*i+1]})',font='bold'), sg.InputText(size=(3,1))] for i in range(6)]
   
    for x in range(6): obj.append(m[x])
    return obj

#Function to hangle Faza Grupowa window
def open_fg(i):
    column = [[]]
    if not i: sg.Popup("Zaloguj sie aby typowac mecze")
    for x in range(len(gr_list)): column = add_mgr(x,column,i)
    layout = [[sg.Column(column, scrollable = True,vertical_scroll_only=True,element_justification='center',expand_x=True)]]
    window = sg.Window('',layout,size=(600,600))
    while True:
        event, values = window.read()
        if event == "type": 
            i.typy_gr = {k: (values[k] if values[k] else i.typy_gr[k]) for k in range(96)}
            window.close()
            open_fg(i)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

#Function to hangle Faza Pucharowa window
def open_fp():
    layout = [[sg.Text('Drabinka')]]
    window = sg.Window('',layout)
    while True:
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

#Main function
def main():
    #Horizontal layout definition for buttons
    layout = [[sg.Menu(menu_def)], [sg.Button('Zaloguj',key='l'), sg.Button('Wyloguj',key='lo'), sg.Button('Grupy',key="g"), sg.Button('Faza Grupowa',key="fg"), sg.Button('Faza Pucharowa',key="fp"), sg.Button('Użytkownicy',key="u")]]
    #Create window with control parameters for the App
    window = sg.Window('Meczystan', layout)
    #Some options for the User to do
    i = None
    while True:
        
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "fg":
             open_fg(i)

        if event == "g": open_g()
        if event == "fp": open_dp()
        if event == "u": open_u()
        if event == "l":
            if not i: i = open_log()
            else: sg.Popup(f'Uzytkownik {i.name} juz jest zalogowany')
        if event == "lo": i = None; sg.Popup("Wylogowano")

    window.close()

if __name__ == "__main__":
    main()



