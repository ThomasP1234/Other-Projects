from multiprocessing.dummy import active_children
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from console import Console

def get_number_of_toplevel_windows(master, count=0):
        for a,b in master.children.items(): #Getting list of root window's children and using recursion 
            if isinstance(b, Toplevel):
                count+=1 #If toplevel then count += 1
            count += get_number_of_toplevel_windows(b, count)
        return count

class IDE(Frame):
    def __init__(self):
        self.root = Tk()
        self.root.overrideredirect(1)
        self.root.withdraw()
        self.background_colour = "#F0F0F0"
        self.default_font = "Helvetica"

    def _init_Shell(self):
        self.toplevelShell = Toplevel(self.root)
        Frame.__init__(self, self.toplevelShell)
        self.configShell()

    def configShell(self):
        self.width = 800
        self.height = 800

        self.toplevelShell.wm_title("ERL IDE")
        self.toplevelShell.wm_iconbitmap("icon.ico")
        self.toplevelShell.geometry(f"{self.width}x{self.height}+100+100")
        self.toplevelShell.resizable(True, True)
        self.toplevelShell.configure(background=self.background_colour)

        self.toplevelShell.bind("<F5>", self.runButton)
        self.toplevelShell.protocol("WM_DELETE_WINDOW",  self.exitButton)

    def create_sizegripShell(self):
        self.toplevelShell.columnconfigure(0, weight=1)
        # self.toplevelShell.rowconfigure(0, weight=1)
        self.toplevelShell.rowconfigure(1, weight=1)
        self.toplevelShell.rowconfigure(2, weight=1)

        my_sizegrip = ttk.Sizegrip(self.toplevelShell)
        my_sizegrip.grid(row=2, sticky="SE")
        # my_sizegrip.pack(side="right", anchor="se")

    def runButton(self, event):
        print("ran")

    def exitButton(self):
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit\nAny unsaved changes will be lost')
        if response:
            self.toplevelShell.destroy()
            if get_number_of_toplevel_windows(self.root) == 0:
                self.root.destroy()

    def drawShell(self):
        self.create_sizegripShell()
        menu = Menu(self.toplevelShell)
        self.toplevelShell.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(
            label="New File"
        )
        fileMenu.add_command(
            label="Open File"
        )
        fileMenu.add_command(
            label="Open Recent"
        )
        fileMenu.add_command(
            label="Save"
        )
        fileMenu.add_command(
            label="Save As..."
        )
        fileMenu.add_command(
            label="Exit",
            command=self.exitButton
        )
        menu.add_cascade(label="File", menu=fileMenu)

        # editMenu = Menu(menu)
        # editMenu.add_command(
        #   label="Undo"
        # )
        # editMenu.add_command(
        #   label="Redo"
        # )
        # menu.add_cascade(label="File", menu=editMenu)

        runMenu = Menu(menu)
        runMenu.add_command(
            label="Run Program",
            command=self.runButton
        )
        runMenu.add_command(
            label="Open Shell"
        )
        menu.add_cascade(label="Run", menu=runMenu)

        self.create_sizegripShell()
        code_label = LabelFrame(self.toplevelShell, font=(self.default_font, 10), text="Shell")
        code_label.grid(row = 1, column = 0, sticky="nsew", padx=10, pady=10)

        code_label.columnconfigure(0, weight=1)
        code_label.rowconfigure(0, weight=1)

        # self.code_widget = Text(code_label, bg="white", font=(self.default_font, 10))
        # self.code_widget.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

        console = Console(code_label)
        console.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

    def run(self):
        self._init_Shell()
        self.drawShell()
        self.root.mainloop()
        return

ide = IDE()
ide.run()
active = active_children()
for child in active: 
    child.terminate()
for child in active:
    child.join()