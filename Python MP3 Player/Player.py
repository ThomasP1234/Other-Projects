import os
from tkinter import *
from tkinter import filedialog
import glob
import pygame
pygame.mixer.init()

# root = Tk()

# style = ttk.Style(root)
# style.theme_use("clam")


# def c_open_file_old():
#     rep = filedialog.askdirectory()
#     Library = glob.glob(rep+"/*.mp3")
#     print(Library)

# ttk.Button(root, text="Select Folder with Music", command=c_open_file_old).grid(row=1, column=0, padx=4, pady=4, sticky='ew')

# root.mainloop()

class Music():
    bg = "#303030"
    window_width = 300
    window_height = 500
    window_x = 200
    window_y = 100

    nowplaying = "None"

    def main(self):
        self.window = Tk()
        self.window.geometry("{0}x{1}+{2}+{3}".format(self.window_width, self.window_height, self.window_x, self.window_y))
        self.window.title("Music Player")
        self.window.resizable(False, False)
        self.window.configure(bg = self.bg)

    def draw(self):
        Button(self.window, text = "Select Music Folder", command = self.OpenFile).pack()

        Button(self.window, text = "Pause/Unpause", command = self.pause).pack()   
        
        self.lbl1 = Label(self.window, text = f"Now Playing: {self.nowplaying}", bg = self.bg, fg = "white")
        self.lbl1.pack()        

    def OpenFile(self):
        rep = filedialog.askdirectory()
        self.Library = glob.glob(rep+"/**/*.mp3", recursive = True)
        self.strip = rep + "\\"
        self.play()

    def play(self):
        self.SONG_END = pygame.USEREVENT + 1
        pygame.mixer.music.load(self.Library[0])
        pygame.mixer.music.play()
        self.nowplaying = self.Library[0]
        self.lbl1.config(text = f"Now Playing: {self.nowplaying.strip(self.strip)}")
        self.Library = self.Library[1:] + [self.Library[0]]

    def pause(self):
        busy = pygame.mixer.music.get_busy()
        if busy == 0:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    def run(self):
        self.main()

        self.draw()

        self.window.mainloop()

runPlayer = Music()
runPlayer.run()