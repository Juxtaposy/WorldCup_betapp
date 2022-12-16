#Main function
def main():
    #Horizontal layout definition for buttons
    layout = [[sg.Menu(menu_def)], [sg.Button('Zaloguj',key='l'), sg.Button('Wyloguj',key='lo'), sg.Button('Grupy',key="g"), sg.Button('Faza Grupowa',key="fg"), sg.Button('Faza Pucharowa',key="fp"), sg.Button('Użytkownicy',key="u"), sg.Button('Admin',key='a')]]
    #Create window with control parameters for the App
    window = sg.Window('Meczystan', layout)
    #Database load and creating empty login container
    i = None
    database = db_read()
    match_data = match_read()
    fp_matches = fp_match_read()
    #Main while loop for GUI - options for user to do
    while True:
        #Get data from events of user
        event, values = window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        #Group phase handle
        if event == "fg": open_fg(i,match_data)
        #Groups information handle
        if event == "g": open_g()
        #Knockout phase handle
        if event == "fp": open_fp(i,fp_matches)
        #Users window handle
        if event == "u": database == open_u(database)
        #Log in handle
        if event == "l":
            if not i: i,database = open_log(database)
            else: sg.Popup(f'User {i.name} is already logged - logout first')
        if event == "lo": i = None; sg.Popup("Logged out")
        #Admin panel handle
        if event == "a":  match_data = open_admin(match_data)
    window.close()
    #Database save after successful program shutdown
    db_write(database)
    match_write(match_data)
    fp_match_write(fp_matches)
    
if __name__ == "__main__":
    main()