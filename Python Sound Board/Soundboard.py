from tkinter import *
from pygame import mixer
mixer.init()
import glob

class Soundboard():
    bg = "#303030"
    sounds = glob.glob("mp3/*.mp3")
    print(sounds)

    def main(self):
        self.window = Tk()
        self.window.geometry("500x600+100+100")
        self.window.resizable(False, False)
        self.window.config(bg = self.bg)
        self.window.title("Soundboard")

    def draw(self):
        row = 0
        column = 0
        colours = ["#CD212A", "#34568B", "#88B04B", "#F5DF4D", "#00A170", "#D2386C", "#FFA500", "#56C6A9", "#FA7A35", "#00758F", "#A2242F", "#D9CE52", "#DC793E"]
        
        for i in range(len(self.sounds)):
            # lbl = Label(self.window, text = "________________________________", font = "arial 20", bg = self.bg, fg = self.colours[i])
            # lbl.pack()
            frame = Frame(self.window, width=100, height=100) #their units in pixels
            button1 = Button(frame, text="", bg = colours[0], activebackground = colours[0], command = lambda num = i: self._play(num))

            zero = colours[0]
            tempcolours = colours[1:]
            tempcolours.append(zero)
            colours = tempcolours

            frame.grid_propagate(False) #disables resizing of frame
            frame.columnconfigure(0, weight=1) #enables button to fill frame
            frame.rowconfigure(0,weight=1) #any positive number would do the trick

            if column < 5:
                frame.grid(row=row, column=column) #put frame where the button should be
                button1.grid(sticky="wens") #makes the button expand
            else:
                column = 0
                row += 1
                frame.grid(row=row, column=column) #put frame where the button should be
                button1.grid(sticky="wens") #makes the button expand
            
            column += 1

    def _play(self, num):
        mixer.stop()
        mixer.music.load(self.sounds[int(num)])
        mixer.music.play()


    def run(self):
        self.main()
        self.draw()

        self.window.mainloop()

ui = Soundboard()
ui.run()