# Author: Thomas Preston

import config as c
from getTextures import *
from drawHealth import *

from tkinter import *
from tkinter import messagebox
from pygame import mixer
mixer.init()
import random
from PIL import ImageTk, Image
from time import sleep

class Game():
    background_colour = "#73b8ba"
    background_colour2 = "#303030"

    window_width = 800
    window_height = 500
    window_x = 100
    window_y = 50

    controls_height = 50
    controls_x = window_x
    controls_y = window_y + window_height + 40

    # inventory_height = 50
    # inventory_x = window_x
    # inventory_y = controls_y + controls_height + 40

    inventory_width = 210
    inventory_height = window_height - 50
    inventory_x = window_x + window_width + 10
    inventory_y = window_y

    stats_width = inventory_width
    stats_height = controls_height + 50
    stats_x = inventory_x
    stats_y = controls_y - 50

    settings_width = inventory_width
    settings_height = inventory_height - 100
    settings_x = inventory_x + inventory_width + 10
    settings_y = inventory_y

    enemey_width = settings_width
    enemey_height = stats_height + 100
    enemey_x = settings_x
    enemey_y = stats_y + stats_height - enemey_height

    inventory2_y = controls_y + controls_height + 40

    level = 1

    mute_state = 0

    btnlist = []
    lbllist = []
    stats = {}

    score = 0

    def __init__(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Battle Game")
        self.window.resizable(False, False)
        self.window.configure(bg = self.background_colour)

        window_can = Canvas(self.window, bg = "green", bd = 0, highlightthickness = 0, width = self.window_width, height = 200)
        window_can.place(x = 0, y = 300)

        self.controls = Toplevel(self.window)
        self.controls.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.controls_height, self.controls_x, self.controls_y))
        self.controls.title("Controls")
        self.controls.resizable(False, False)
        self.controls.configure(bg = self.background_colour2)

        self.inventory = Toplevel(self.window)
        self.inventory.geometry("{0}x{1}+{2}+{3}".format(self.inventory_width, self.inventory_height, self.inventory_x, self.inventory_y))
        self.inventory.title("Inventory")
        self.inventory.resizable(False, False)
        self.inventory.configure(bg = self.background_colour2)

        self.playerstats = Toplevel(self.window)
        self.playerstats.geometry("{0}x{1}+{2}+{3}".format(self.stats_width, self.stats_height, self.stats_x, self.stats_y))
        self.playerstats.title("Stats")
        self.playerstats.resizable(False, False)
        self.playerstats.configure(bg = self.background_colour2)

        self.settings = Toplevel(self.window)
        self.settings.geometry("{0}x{1}+{2}+{3}".format(self.settings_width, self.settings_height, self.settings_x, self.settings_y))
        self.settings.title("Settings")
        self.settings.resizable(False, False)
        self.settings.configure(bg = self.background_colour2)

        self.enemeywin = Toplevel(self.window)
        self.enemeywin.geometry("{0}x{1}+{2}+{3}".format(self.enemey_width, self.enemey_height, self.enemey_x, self.enemey_y))
        self.enemeywin.title("Enemey Stats")
        self.enemeywin.resizable(False, False)
        self.enemeywin.configure(bg = self.background_colour2)

        self.inventory2 = Toplevel(self.window)
        self.inventory2.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.controls_height, self.controls_x, self.inventory2_y))
        self.inventory2.title("Inventory")
        self.inventory2.resizable(False, False)
        self.inventory2.configure(bg = self.background_colour2)

        self.window.focus_force()

    def draw(self):
        self.scorelbl = Label(self.window, text = f"Score: {self.score}", font = "Orbitron 20", bg = self.background_colour)
        self.scorelbl.place(x = 10, y = 10)

        self.attackbtn = Button(self.controls, text = "Attack", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = self.attack, width = 12, relief = RIDGE)
        self.defendbtn = Button(self.controls, text = "Defend", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = self.defend, width = 12, relief = RIDGE)
        self.healbtn = Button(self.controls, text = "Heal", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = self.heal, width = 12, relief = RIDGE)
        self.run_awaybtn = Button(self.controls, text = "Run Away", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = self.run_away, width = 12, relief = RIDGE)

        # attackbtn.grid(row = 0, column = 0)
        # defendbtn.grid(row = 0, column = 1)
        # healbtn.grid(row = 0, column = 2)
        # run_awaybtn.grid(row = 0, column = 3)

        startingx = 140
        xincrease = 130

        xincrease*0+startingx
        self.attackbtn.place(x = xincrease*0+startingx, y = 10)
        self.defendbtn.place(x = xincrease*1+startingx, y = 10)
        self.healbtn.place(x = xincrease*2+startingx, y = 10)
        self.run_awaybtn.place(x = xincrease*3+startingx, y = 10)

        exitButton = Button(self.settings, text = "Exit", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = exit, width = 12, relief = RIDGE)
        exitButton.place(x = 10, y = 311)

        lbl1 = LabelFrame(self.inventory, text = "Weapons:", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", width = 190, height = 430, relief = RIDGE)
        lbl1.place(x = 10, y = 10)

        info = Button(self.inventory, text = "Info", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = lambda msg = "Click Buttons To Enable As Primary Weapon": self.popup(msg), width = 18, relief = RIDGE)
        info.place(x = 15, y = 0*35+30)

        self.lbl2 = Label(self.playerstats, text = f"Health:  {c.player_health}", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white")
        self.lbl2.pack()

        self.c = Canvas(self.playerstats, bg = self.background_colour2, bd = 0, highlightthickness = 0, width = self.stats_width, height = 30)

        draw_health(self.c, c.player_health)

        lbl3 = LabelFrame(self.settings, text = "Volume Controls:", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", width = 190, height = 100, relief = RIDGE)
        lbl3.place(x = 10, y = 10)

        self.mutebtn = Button(self.settings, text = "Mute/Unmute", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = self.mute, width = 18, relief = RIDGE)
        self.mutebtn.place(x = 15, y = 70)

        self.volume_control = Scale(self.settings, resolution = 0.01, from_=0, to=1, bd = 0, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, highlightbackground = self.background_colour2, highlightthickness = 0, highlightcolor = self.background_colour2, orient=HORIZONTAL, length = 173, command = self.volume_set)
        self.volume_control.set(0.5)
        self.volume_control.place(x = 15, y = 30)

        mixer.music.load(background_music)
        mixer.music.play(loops = -1)

        characterIMG = Image.open(draw_player)
        width, height = characterIMG.size
        characterIMG = characterIMG.resize((width*2, height*2), Image.ANTIALIAS)
        characterIMG = characterIMG.resize((48, 100), Image.ANTIALIAS)
        characterPIMG = ImageTk.PhotoImage(characterIMG)

        characterlbl = Label(self.window, image = characterPIMG, bg = self.background_colour)
        characterlbl.image = characterPIMG

        characterlbl.place(x = 50, y = 196)

        self.lbl4 = Label(self.enemeywin, text = "", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white")
        self.lbl4.pack()

        self.lbl5 = Label(self.inventory2, text = "Inventory:", font = "Orbitron 15", bg = self.background_colour2, foreground = "white")
        self.lbl5.place(x = 10, y = 10)

        counter = 1
        for item in c.player_weapons:
            if item in c.Weapons:
                btn = Button(self.inventory, text = item, font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = lambda w = item: self.enable_weapon(w), width = 18, relief = RIDGE)
                btn.place(x = 15, y = counter*35+35)

                self.btnlist.append(btn)
            counter += 1
        self.lbl5.config(text = "Inventory: {0}".format(c.player_inventory))

    def mute(self):
        if self.mute_state == 0:
            self.mute_state = 1
            mixer.music.set_volume(0)
        else:
            self.mute_state = 0
            mixer.music.set_volume(1)

    def volume_set(self, num):
        mixer.music.set_volume(float(num))

    def game(self):
        self.attackbtn["state"] = NORMAL
        self.defendbtn["state"] = NORMAL

        chosen = []
        self.lbllist = []
        xincrease = 120
        startx = 280
        string = ""

        if self.level <= c.Difficulty["Easy"]:
            num = random.randint(1, c.max_enimies)
            for i in range(num):
                chosen.append(random.choice(c.Easy))
            number = 0
            for entity in chosen:
                draw = c.enemy[entity]["draw"]

                enemyIMG = Image.open(draw)
                width, height = enemyIMG.size
                enemyIMG = enemyIMG.resize((width*2, height*2), Image.ANTIALIAS)
                enemyPIMG = ImageTk.PhotoImage(enemyIMG)

                enemylbl = Label(self.window, image = enemyPIMG, bg = self.background_colour)
                enemylbl.image = enemyPIMG

                enemylbl.place(x = number*xincrease + startx, y = 190)
                self.lbllist.append(enemylbl)

                entitystat = {
                    entity+str(number):{
                        "health":c.enemy[entity]["health"],
                        "damage":c.enemy[entity]["damage"]
                    }
                }
                self.stats.update(entitystat)

                health = c.enemy[entity]["health"]
                damage = c.enemy[entity]["damage"]

                string += entity.title() + f": \nHealth = {health}, \nAttack Damage = {damage}\n\n"
                self.lbl4.config(text = string)
                
                number += 1
        elif self.level <= c.Difficulty["Medium"]:
            num = random.randint(1, c.max_enimies)
            for i in range(num):
                category = random.choice([c.Medium, c.Easy])
                chosen.append(random.choice(category))
            number = 0
            for entity in chosen:
                draw = c.enemy[entity]["draw"]

                enemyIMG = Image.open(draw)
                width, height = enemyIMG.size
                enemyIMG = enemyIMG.resize((width*2, height*2), Image.ANTIALIAS)
                enemyPIMG = ImageTk.PhotoImage(enemyIMG)

                enemylbl = Label(self.window, image = enemyPIMG, bg = self.background_colour)
                enemylbl.image = enemyPIMG

                enemylbl.place(x = number*xincrease + startx, y = 190)
                self.lbllist.append(enemylbl)

                entitystat = {
                    entity+str(number):{
                        "health":c.enemy[entity]["health"],
                        "damage":c.enemy[entity]["damage"]
                    }
                }
                self.stats.update(entitystat)

                health = c.enemy[entity]["health"]
                damage = c.enemy[entity]["damage"]

                string += entity.title() + f": \nHealth = {health}, \nAttack Damage = {damage}\n\n"
                self.lbl4.config(text = string)
                
                number += 1
        elif self.level <= c.Difficulty["Hard"]:
            c.max_enimies = 2
            num = random.randint(1, c.max_enimies)
            for i in range(num):
                category = random.choice([c.Hard, c.Medium])
                chosen.append(random.choice(category))
            number = 0
            for entity in chosen:
                draw = c.enemy[entity]["draw"]

                enemyIMG = Image.open(draw)
                width, height = enemyIMG.size
                enemyIMG = enemyIMG.resize((width*2, height*2), Image.ANTIALIAS)
                enemyPIMG = ImageTk.PhotoImage(enemyIMG)

                enemylbl = Label(self.window, image = enemyPIMG, bg = self.background_colour)
                enemylbl.image = enemyPIMG

                enemylbl.place(x = number*xincrease + startx, y = 190)
                self.lbllist.append(enemylbl)

                entitystat = {
                    entity+str(number):{
                        "health":c.enemy[entity]["health"],
                        "damage":c.enemy[entity]["damage"]
                    }
                }
                self.stats.update(entitystat)

                health = c.enemy[entity]["health"]
                damage = c.enemy[entity]["damage"]

                string += entity.title() + f": \nHealth = {health}, \nAttack Damage = {damage}\n\n"
                self.lbl4.config(text = string)
                
                number += 1
        else:
            c.max_enimies = 1
            num = random.randint(1, c.max_enimies)
            for i in range(num):
                category = random.choice([c.Boss, c.Hard, c.Medium])
                chosen.append(random.choice(category))
            number = 0
            for entity in chosen:
                draw = c.enemy[entity]["draw"]

                enemyIMG = Image.open(draw)
                width, height = enemyIMG.size
                enemyIMG = enemyIMG.resize((width*2, height*2), Image.ANTIALIAS)
                enemyPIMG = ImageTk.PhotoImage(enemyIMG)

                enemylbl = Label(self.window, image = enemyPIMG, bg = self.background_colour)
                enemylbl.image = enemyPIMG

                enemylbl.place(x = number*xincrease + startx, y = 190)
                self.lbllist.append(enemylbl)

                entitystat = {
                    entity+str(number):{
                        "health":c.enemy[entity]["health"],
                        "damage":c.enemy[entity]["damage"]
                    }
                }
                self.stats.update(entitystat)

                health = c.enemy[entity]["health"]
                damage = c.enemy[entity]["damage"]

                string += entity.title() + f": \nHealth = {health}, \nAttack Damage = {damage}\n\n"
                self.lbl4.config(text = string)
                
                number += 1
        
        if c.max_enimies < 3:
            c.max_enimies +=1
        self.level += 1
        

    def attack(self):
        effect = mixer.Sound(hit_music)
        effect.play()
        to_pop = []
        string = ""
        new_playdamage = c.player_damage + c.Weapons[c.primary_weapon]
        for entity in self.stats:
            self.stats[entity]["health"] -= new_playdamage
            if self.stats[entity]["health"] <= 0:
                to_pop.append(entity)
                ogentity = ''.join([i for i in entity if not i.isdigit()])
                if ogentity in c.Easy:
                    self.score += c.Score["Easy"]
                elif ogentity in c.Medium:
                    self.score += c.Score["Medium"]
                elif ogentity in c.Hard:
                    self.score += c.Score["Hard"]
                else:
                    self.score += c.Score["Boss"]
                self.scorelbl.config(text = f"Score: {self.score}")
            else:
                c.player_health -= self.stats[entity]["damage"]
                if c.player_health < 0:
                    c.player_health = 0
            break
        for entity in to_pop:
            self.stats.pop(entity)
            labl = self.lbllist.pop(0)
            labl.destroy()
        
        for entity in self.stats:
            health = self.stats[entity]["health"]
            damage = self.stats[entity]["damage"]
            result = ''.join([i for i in entity if not i.isdigit()])
            string += result.title() + f": \n Health = {health}, \n Attack Damage = {damage}\n\n"
        self.lbl4.config(text = string)

        self.c.destroy()

        self.c = Canvas(self.playerstats, bg = self.background_colour2, bd = 0, highlightthickness = 0, width = self.stats_width, height = 30)

        draw_health(self.c, c.player_health)

        self.lbl2.config(text = f"Health:  {c.player_health}")

        if len(self.stats) == 0:
            if len(c.player_inventory) < 3:
                keys = []
                yORn = random.choice([True, False])
                if yORn == True:
                    amount = random.randint(1,2)
                    for key in c.Items:
                        keys.append(key)
                    for i in range(amount):
                        c.player_inventory.append(random.choice(keys))
                        
            if self.level == c.Difficulty["Easy"]+1:
                c.player_weapons.append(c.Weaponslst[0])
            elif self.level == c.Difficulty["Medium"]+1:
                c.player_weapons.append(c.Weaponslst[1])
            
            self.UpdateInventory()

            self.nextlvl = Button(self.controls, text = "Next Level", font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = self.new_game, width = 9, relief = RIDGE)
            self.nextlvl.place(x = 10, y = 10)

            self.attackbtn["state"] = DISABLED
            self.defendbtn["state"] = DISABLED

        if c.player_health == 0:
            self.attackbtn["state"] = DISABLED
            self.defendbtn["state"] = DISABLED
            self.healbtn["state"] = DISABLED
            self.run_awaybtn["state"] = DISABLED

            mixer.music.fadeout(3000)

            self.popup("You have died")

    def new_game(self):
        self.nextlvl.destroy()
        self.game()

    def heal(self):
        for item in c.player_inventory:
            if item in c.Items:
                c.player_health += c.Items[item]
                self.c.destroy()

                self.c = Canvas(self.playerstats, bg = self.background_colour2, bd = 0, highlightthickness = 0, width = self.stats_width, height = 30)

                draw_health(self.c, c.player_health)

                self.lbl2.config(text = f"Health:  {c.player_health}")

                c.player_inventory.remove(item)
                self.UpdateInventory()

    def defend(self):
        sleep(5)
        c.player_health += random.randint(5,15)

        self.c.destroy()

        self.c = Canvas(self.playerstats, bg = self.background_colour2, bd = 0, highlightthickness = 0, width = self.stats_width, height = 30)

        draw_health(self.c, c.player_health)

        self.lbl2.config(text = f"Health:  {c.player_health}")

    def run_away(self):
        answer = messagebox.askquestion("Give Up", "Are you sure you want to run away.\nThis will quit the game!")
        if answer == "yes":
            exit()

    def enable_weapon(self, weapon):
        c.primary_weapon = weapon

        for butt in self.btnlist:
            if butt["text"] == weapon:
                butt.config(fg = "red")
            else:
                butt.config(fg = "white")


    def popup(self, msg):
        messagebox.showinfo("Information", msg)

    def UpdateInventory(self):
        for i in range(len(self.btnlist)):
            butt = self.btnlist.pop(0)
            butt.destroy()
        counter = 1
        for item in c.player_weapons:
            if item in c.Weapons:
                btn = Button(self.inventory, text = item, font = "Orbitron 10", bd = 4, bg = self.background_colour2, fg = "white", activebackground = self.background_colour2, command = lambda w = item: self.enable_weapon(w), width = 18, relief = RIDGE)
                btn.place(x = 15, y = counter*35+45)

                self.btnlist.append(btn)
                counter += 1

            
        self.lbl5.config(text = "Inventory: {0}".format(c.player_inventory))

        for butt in self.btnlist:
            if butt["text"] == c.primary_weapon:
                butt.config(fg = "red")
            else:
                butt.config(fg = "white") 
            
    def run(self):
        self.draw()
        self.game()
        self.window.mainloop()

ui = Game()
ui.run()