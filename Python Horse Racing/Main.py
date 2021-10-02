import Config as C
import Login as L

from tkinter import *
from PIL import ImageTk, Image
from time import sleep
import random
import json

class Game():
    bg = "#303030"

    window_width = 800
    window_height = 500
    window_x = 200
    window_y = 200

    controls_width = 300
    controls_height = window_height + 50
    controls_x = window_x + window_width + 40
    controls_y = window_y - 50

    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Horse Racing")
        self.window.resizable(False, False)
        self.window.configure(bg = self.bg)

        self.controls = Toplevel(self.window)
        self.controls.geometry("{0}x{1}+{2}+{3}".format(self.controls_width, self.controls_height, self.controls_x, self.controls_y))
        self.controls.title("Controls")
        self.controls.resizable(False, False)
        self.controls.configure(bg = self.bg)

        self.c = Canvas(self.window, bg = "green", bd = 0, highlightthickness = 0, width = self.window_width, height = 500)

    def draw(self):
        self.horses = []
        self.widths = []
        for horse in range(C.numhorse):
            horseIMG = Image.open(C.TextureMappings["horse" + str(horse+1) + "_1"])
            width, height = horseIMG.size
            horseIMG = horseIMG.resize((round(width*1.5), round(height*1.5)), Image.ANTIALIAS)
            horsePIMG = ImageTk.PhotoImage(horseIMG)

            horseLBL = Label(self.window, image = horsePIMG, bg = "green")
            horseLBL.image = horsePIMG

            horseLBL.place(x = 10+round(width*1.5), y = horse*100+10, anchor = "ne")            

            self.horses.append(horseLBL)
            self.widths.append(width)
        # self.c.create_line(round(width*1.5)+20, 0, round(width*1.5)+20, 500, fill = "white")
        self.c.create_line(800-round(width*1.5)-20, 0, 800-round(width*1.5)-20, 500, fill = "white")

        # print(800-round(width*1.5)-20)

        self.OddsLabels = []
        for i in range(C.numhorse):
            horsenum = Label(self.window, text = str(i+1), font = "Orbitron 20", bd = 4, bg = "green", fg = "white")
            horsenum.place(x = 780, y = i*100 + 60, anchor = "center")

            BetButton = Button(self.controls, text = f"Bet on horse: {str(i+1)}", font = "Orbitron 10", bd = 4, bg = self.bg, fg = "white", activebackground = self.bg, command = lambda num = i+1: self.game(num), width = 15, relief = RIDGE)
            BetButton.place(x = 10, y = i*100 + 60 + 50, anchor = "w")

            OddsLabel = Label(self.controls, text = f"Odds: {C.odds[i]}:1", font = "Orbitron 10", bd = 4, bg = self.bg, fg = "white")
            OddsLabel.place(x = 200, y = i*100 + 60+ 50, anchor = "w")

            self.OddsLabels.append(OddsLabel)

        self.funds = Label(self.controls, text = f"Money:\n£{C.playerfunds}", font = "Orbitron 12", bd = 4, bg = self.bg, fg = "white")
        self.funds.place(x = 10, y = 10)

        extrafunds = Button(self.controls, text = "£+", font = "Orbitron 10", bd = 4, bg = self.bg, fg = "white", activebackground = self.bg, command = self.increase, relief = RIDGE)
        extrafunds.place(x = 10, y = 60)

        BetAmountLabel = Label(self.controls, text = "Bet Amount:", font = "Orbitron 12", bd = 4, bg = self.bg, fg = "white")
        BetAmountLabel.place(x = 290, y = 10, anchor = "ne")

        self.BetAmount = Entry(self.controls, font = "Orbitron 13", bd = 4, bg = self.bg, fg = "white", width = 10)
        self.BetAmount.place(x = 290, y = 40, anchor = "ne")

    def increase(self):
        C.playerfunds += 100
        self.funds.config(text = f"Money:\n£{C.playerfunds}")

        f = open("Accounts.json", "r")
        data = json.load(f)

        data[C.user]["Funds"] = C.playerfunds

        with open("Accounts.json", "w") as outfile:
                json.dump(data, outfile)

        f.close()

    def game(self, betnum):
        try:
            temp = int(self.BetAmount.get())
        except:
            return
        if int(self.BetAmount.get()) > C.playerfunds:
            return
        horsenum = 0
        for horse in self.horses:
            horse.place_forget()
            horse.place(x = 10+round(self.widths[horsenum]*1.5), y = horsenum*100+10, anchor = "ne")
            horsenum += 1
        num = 2
        while True:
            horsepos = []
            for horse in self.horses:
                horsepos.append(horse.place_info()["x"])
            
            if int(max(horsepos)) < 650:
                count = 0
                for horse in self.horses:
                    x = int(horse.place_info()["x"])
                    y = int(horse.place_info()["y"])
                    horse.place_forget()
                    horse.place(x = x+random.randint(5,50)-C.odds[count]*2, y = y, anchor = "ne")

                for horse in self.horses:
                    horseIMG = Image.open(C.TextureMappings["horse" + str(count+1) + "_" + str(num)])
                    width, height = horseIMG.size
                    horseIMG = horseIMG.resize((round(width*1.5), round(height*1.5)), Image.ANTIALIAS)
                    horsePIMG = ImageTk.PhotoImage(horseIMG)

                    horse.configure(image = horsePIMG)
                    horse.image = horsePIMG
                    
                    count += 1

                if num == C.nummodels:
                    num = 1
                else:
                    num += 1
                

                self.window.update()
                sleep(0.2)
            else:
                break
        horsepos = []
        for horse in self.horses:
            horsepos.append(horse.place_info()["x"])
        distance = max(horsepos)
        winner = horsepos.index(distance)
        if betnum-1 == winner:
            winnings = int(self.BetAmount.get())*C.odds[betnum-1]
            C.playerfunds += winnings

            f = open("Accounts.json", "r")
            data = json.load(f)

            data[C.user]["Funds"] = C.playerfunds

            with open("Accounts.json", "w") as outfile:
                    json.dump(data, outfile)

            f.close()
        
        else:
            f = open("Accounts.json", "r")
            data = json.load(f)

            C.playerfunds -= int(self.BetAmount.get())

            data[C.user]["Funds"] = C.playerfunds

            with open("Accounts.json", "w") as outfile:
                    json.dump(data, outfile)

            f.close()
        self.funds.config(text = f"Money:\n£{C.playerfunds}")

        C.odds = []
        for i in range(C.numhorse):
            C.odds.append(random.randint(1, 5))

        count2 = 0
        for horse in self.OddsLabels:
            horse.config(text = f"Odds: {C.odds[count2]}:1")
            count2 += 1

    def run(self):
        result = L.login()
        if result == 1:
            self.main()
            self.draw()
            self.c.place(x = 0, y = 0)

            self.window.mainloop()

start = Game()
start.run()