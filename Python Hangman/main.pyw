# *************************************************************************************************
#
#   Made by Thomas Preston (September 2022)
#
#   To add more words to the program. Add them as a new line in the chosen category in resources
#   or add a new category to the CATEGORIES constant below and then create a txt file in resources
#   with the same name and put new words in there.
#
# *************************************************************************************************

# Includes
from tkinter import *
import random

# Constants
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

DEFAULT_FONT = "Berlin Sans FB"

BACKGROUND = "#303030"
WHITE = "#FFFFFF"
LIGHT_GREY = "#C8C8C8"
GREY = "#505050"
GREEN = "#009E2F"
RED = "#E62937"

CATEGORIES = ["Algorithms", "Computer Law",
              "CPU", "Error Checking",
              "Malware", "Network",
              "Programming", "Storage Types",
              "Translators", "Utility Software"]

# Game Class
class Hangman():
    def __init__(self):
        initWidth = "900"
        initHeight = "432"

        self.root = Tk()
        self.root.title("Hangman (By Thomas Preston)")
        self.root.configure(background=BACKGROUND)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        initX = int((screen_width/2) - (int(initWidth)/2))
        initY = int((screen_height/2) - (int(initHeight)/2))

        self.root.geometry(f"{initWidth}x{initHeight}+{initX}+{initY}")

        self.root.bind("<KeyPress>", self.keyPress)

        self.category = "Random"

        self.gameLogic()
        self.window()

    def gameLogic(self):
        if self.category == "Random":
            category = random.choice(CATEGORIES)
            self.labelCategory = category
        else:
            category = self.category
        file = open(f"Resources\\{category}.txt")

        answersStr = file.read()
        answers = answersStr.split('\n')
        self.answer = random.choice(answers)
        self.answerUppercase = self.answer.upper()
        file.close()

        self.solutionLetters = []
        for letter in self.answerUppercase:
            if not (letter in LETTERS):
                continue
            if not (letter in self.solutionLetters):
                self.solutionLetters.append(letter)

        self.solutionLettersSize = len(self.solutionLetters)
        self.validGuesses = []
        self.invalidGuesses = []
        self.puzzle = ""
        self.updatePuzzleString()

        self.livesLeft = 10

    def window(self):
        titleFrame = Frame(self.root, bg=BACKGROUND)
        titleFrame.pack(expand=True, fill="x")
        title = Label(titleFrame, text="Hangman", font=(DEFAULT_FONT, "80"), bg=BACKGROUND, fg=WHITE)
        title.pack()

        puzzleFrame = Frame(self.root, bg=BACKGROUND)
        puzzleFrame.pack(expand=True, fill="x")
        self.puzzleTitle = Label(puzzleFrame, text=f"{self.puzzle}", font=(DEFAULT_FONT, "50"), bg=BACKGROUND, fg=WHITE)
        self.puzzleTitle.pack()

        gameFrame = Frame(self.root, bg=BACKGROUND)
        gameFrame.pack(expand=True, fill="both")
        gameFrame.columnconfigure(0, weight=1)
        gameFrame.columnconfigure(1, weight=1)
        gameFrame.rowconfigure(0, weight=1)

        letterFrame = Frame(gameFrame, bg=BACKGROUND)
        letterFrame.grid(row=0, column=0)

        for column in range(0, 5):
            letterFrame.columnconfigure(column, weight=1)
        for row in range(0, 6):
            letterFrame.rowconfigure(row, weight=1)

        row = 0
        column = 0
        self.letterButtons = {}
        for letter in LETTERS:
            btn = Button(letterFrame, height=3, width=3,
                                text=f"{letter}", font=(DEFAULT_FONT, 20),
                                background=BACKGROUND, foreground=WHITE,
                                highlightbackground=LIGHT_GREY, highlightcolor=WHITE,
                                activebackground=GREY, activeforeground=WHITE,
                                bd=2, relief=FLAT
                                )
            btn.grid(row=row, column=column)
            btn.configure(command = lambda x = letter: self.processGuess(x))
            self.letterButtons[letter] = btn

            column += 1
            if column == 5:
                row += 1
                column = 0

        reset = Button(letterFrame, height=3, width=3,
                                text="↻", font=(DEFAULT_FONT, 20),
                                background=BACKGROUND, foreground=WHITE,
                                highlightbackground=LIGHT_GREY, highlightcolor=WHITE,
                                activebackground=GREY, activeforeground=WHITE,
                                bd=2, relief=FLAT, command = self.reset
                                )
        reset.grid(row=row, column=column)
        column+=1
        categoryChange = Button(letterFrame, height=3, width=3,
                                text="CAT", font=(DEFAULT_FONT, 20),
                                background=BACKGROUND, foreground=WHITE,
                                highlightbackground=LIGHT_GREY, highlightcolor=WHITE,
                                activebackground=GREY, activeforeground=WHITE,
                                bd=2, relief=FLAT, command = self.changeCategoryWindow
                                )
        categoryChange.grid(row=row, column=column)
        column+=1
        exit = Button(letterFrame, height=3, width=3,
                                text="ESC", font=(DEFAULT_FONT, 20),
                                background=BACKGROUND, foreground=WHITE,
                                highlightbackground=LIGHT_GREY, highlightcolor=WHITE,
                                activebackground=GREY, activeforeground=WHITE,
                                bd=2, relief=FLAT, command = self.root.destroy
                                )
        exit.grid(row=row, column=column)

        infoFrame = Frame(gameFrame, bg=BACKGROUND)
        infoFrame.grid(row=0, column=1)

        self.badGuessesTitle = Label(infoFrame, text="Bad Guesses:\n", font=(DEFAULT_FONT, "30"), bg=BACKGROUND, fg=WHITE)
        self.badGuessesTitle.pack()

        self.livesTitle = Label(infoFrame, text=f"Lives: {self.livesLeft}", font=(DEFAULT_FONT, "30"), bg=BACKGROUND, fg=WHITE)
        self.livesTitle.pack()

        self.categoryTitle = Label(infoFrame, font=(DEFAULT_FONT, "30"), bg=BACKGROUND, fg=WHITE)
        if self.category == "Random":
            self.categoryTitle.configure(text=f"Category: {self.labelCategory}")
        else:
            self.categoryTitle.configure(text=f"Category: {self.category}")
        self.categoryTitle.pack()

    def changeCategoryWindow(self):
        menu = Toplevel(self.root)
        menu.title("Category Chooser")
        menuFrame = Frame(menu, bg=BACKGROUND)
        menuFrame.pack(expand=True, fill="both")

        newCategories = CATEGORIES

        for column in range(0, int(len(newCategories))+1):
            menuFrame.columnconfigure(column, weight=1)
        for row in range(0, 5):
            menuFrame.rowconfigure(row, weight=1)

        row, column = 0, 0
        for i in range(0, len(newCategories)+1):
            try:
                selectedCategory = newCategories[i]
            except IndexError as e:
                selectedCategory = "Random"
            button = Button(menuFrame,
                                text=f"{selectedCategory}", font=(DEFAULT_FONT, 20),
                                background=BACKGROUND, foreground=WHITE,
                                highlightbackground=LIGHT_GREY, highlightcolor=WHITE,
                                activebackground=GREY, activeforeground=WHITE,
                                bd=2, relief=FLAT, command = lambda x = menu, y = selectedCategory: self.changeCategory(x, y))
                               
            button.grid(row=row, column=column)
            row += 1
            if row == 5:
                row = 0
                column += 1

        menu.mainloop()

    def changeCategory(self, menu, category):
        self.category = category
        menu.destroy()
        self.reset()

    def updatePuzzleString(self):
        puzzle = ""

        for letter in self.answerUppercase:
            if(letter == " " or letter in self.validGuesses or not (letter in LETTERS)):
                puzzle += letter        
            else:
                puzzle += "-"

        self.puzzle = puzzle

    def processGuess(self, letter):
        button = self.letterButtons[letter]
        if button["state"] != DISABLED:
            button["state"] = DISABLED
            button.configure(fg = GREY)

            if letter in self.solutionLetters: # Correct Guess
                button.configure(bg = GREEN)
                self.validGuesses.append(letter)
                self.updatePuzzleString()
                self.puzzleTitle.configure(text=self.puzzle)
   
            else: # Incorrect Guess
                button.configure(bg = RED)
                self.invalidGuesses.append(letter)
                self.livesLeft-=1
                self.badGuessesTitle.configure(text=self.badGuessesTitle.cget('text')+letter)
                self.livesTitle.configure(text=f"Lives: {self.livesLeft}")

            if len(self.validGuesses) == self.solutionLettersSize: # Win condition
                self.disableAllButtons()
                self.puzzleTitle.configure(fg=GREEN)

            elif self.livesLeft == 0: # Loose Condition
                self.disableAllButtons()
                self.validGuesses = self.solutionLetters
                self.updatePuzzleString()
                self.puzzleTitle.configure(text=self.puzzle)
                self.puzzleTitle.configure(fg=RED)
           
    def disableAllButtons(self):
        for letter in LETTERS:
            button = self.letterButtons[letter]
            button["state"] = DISABLED

    def enableAllButtons(self):
        for letter in LETTERS:
            button = self.letterButtons[letter]
            button["state"] = NORMAL
            button.configure(bg = BACKGROUND, fg = WHITE)

    def reset(self):
        self.enableAllButtons()
        self.gameLogic()
        self.puzzleTitle.configure(text=self.puzzle)
        self.puzzleTitle.configure(fg=WHITE)
        self.badGuessesTitle.configure(text="Bad Guesses:\n")
        self.livesTitle.configure(text=f"Lives: {self.livesLeft}")
        if self.category == "Random":
            self.categoryTitle.configure(text=f"Category: {self.labelCategory}")
        else:
            self.categoryTitle.configure(text=f"Category: {self.category}")

    def keyPress(self, event):
        if event.keysym == 'Escape':
            self.root.destroy()
        if event.keysym.upper() in LETTERS:
            self.processGuess(event.keysym.upper())

    def gameloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Hangman()
    game.gameloop()