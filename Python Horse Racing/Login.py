import json
from tkinter import *
import Config as C

def login():
    global loginwin
    global Entry1, Entry2, Entry3, Entry4
    height = 400
    width = 300
    bg = "#303030"

    loginwin = Tk()
    loginwin.geometry("{0}x{1}+{2}+{3}".format(width, height, 200, 200))
    loginwin.title("Login")
    loginwin.resizable(False, False)
    loginwin.configure(bg = bg)

    SignIn = Label(loginwin, text = "Sign In:", font = "Orbitron 25 bold", bd = 4, bg = bg, fg = "white")
    SignIn.place(x = 10, y = 10)

    Username = Label(loginwin, text = "Username:", font = "Orbitron 13", bd = 4, bg = bg, fg = "white")
    Username.place(x = 10, y = 60)

    Entry1 = Entry(loginwin, font = "Orbitron 13", bd = 4, bg = bg, fg = "white", width = 10)
    Entry1.place(x = 130, y = 60)

    Password = Label(loginwin, text = "Password:", font = "Orbitron 13", bd = 4, bg = bg, fg = "white")
    Password.place(x = 10, y = 110)

    Entry2 = Entry(loginwin, font = "Orbitron 13", bd = 4, bg = bg, fg = "white", width = 10)
    Entry2.place(x = 130, y = 110)

    Button1 = Button(loginwin, text = "Sign In", font = "Orbitron 10", bd = 4, bg = bg, fg = "white", activebackground = bg, command = lambda process = 1: loginProcess(process), width = 30, relief = RIDGE)
    Button1.place(x = 10, y = 160)




    SignUp = Label(loginwin, text = "Create an Account:", font = "Orbitron 18 bold", bd = 4, bg = bg, fg = "white")
    SignUp.place(x = 10, y = 210)

    CreateUsername = Label(loginwin, text = "Username:", font = "Orbitron 13", bd = 4, bg = bg, fg = "white")
    CreateUsername.place(x = 10, y = 260)

    Entry3 = Entry(loginwin, font = "Orbitron 13", bd = 4, bg = bg, fg = "white", width = 10)
    Entry3.place(x = 130, y = 260)

    CreatePassword = Label(loginwin, text = "Password:", font = "Orbitron 13", bd = 4, bg = bg, fg = "white")
    CreatePassword.place(x = 10, y = 310)

    Entry4 = Entry(loginwin, font = "Orbitron 13", bd = 4, bg = bg, fg = "white", width = 10)
    Entry4.place(x = 130, y = 310)

    Button2 = Button(loginwin, text = "Sign Up", font = "Orbitron 10", bd = 4, bg = bg, fg = "white", activebackground = bg, command = lambda process = 2: loginProcess(process), width = 30, relief = RIDGE)
    Button2.place(x = 10, y = 360)

    loginwin.mainloop()

    try:
        return returned
    except:
        pass

def loginProcess(process):
    global returned
    if process == 1:
        try:
            f = open("Accounts.json", "r")
            data = json.load(f)

            if data[Entry1.get()]["Password"] == Entry2.get():
                C.playerfunds = data[Entry1.get()]["Funds"]
                C.user = Entry1.get()
                loginwin.destroy()
                returned = 1
            
            f.close()
            
        except:
            pass

    elif process == 2:
        try:
            f = open("Accounts.json", "r")
            data = json.load(f)

            if Entry3.get() not in data.keys():
                data[Entry3.get()] = {
                    "Password": Entry4.get(),
                    "Funds": C.newAccountFunds
                }

                with open("Accounts.json", "w") as outfile:
                    json.dump(data, outfile)
                
                C.playerfunds = data[Entry3.get()]["Funds"]
                C.user = Entry1.get()
                loginwin.destroy()
                returned = 1
            f.close()
        except Exception as e:
            pass