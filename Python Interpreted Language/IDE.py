# TODO config file to edit default keybinds
# On finish change to .pyw to hide console

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from console import Console

class IDEShell:
    def __init__(self, root):
        self.master = root
        self.background_colour = "#F0F0F0"
        self.default_font = "Helvetica"
        self.draw()

    def draw(self):
        code_label = LabelFrame(self.master, font=(self.default_font, 10), text="Shell")
        code_label.grid(row = 1, column = 0, sticky="nsew", padx=10, pady=10)

        code_label.columnconfigure(0, weight=1)
        code_label.rowconfigure(0, weight=1)

        # self.code_widget = Text(code_label, bg="white", font=(self.default_font, 10))
        # self.code_widget.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

        console = Console(code_label)
        console.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

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
            label="Open Shell",
            command=lambda: IDEShell(self.master)
        )
        menu.add_cascade(label="Run", menu=runMenu)

    def runButton(self, event):
        print("ran")

    def exitButton(self):
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit\nAny unsaved changes will be lost')
        if response:
            self.master.destroy()
            exit()

class IDEEditor:
    def __init__(self, root):
        self.root = root
        self.background_colour = "#F0F0F0"
        self.default_font = "Helvetica"
        self.draw()
        
    def draw(self):
        self.code_draw()
        self.output_draw()

    def code_draw(self):
        code_label = LabelFrame(self.root, font=(self.default_font, 10), text="Code")
        code_label.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

        code_label.columnconfigure(0, weight=1)
        code_label.rowconfigure(0, weight=1)

        code_widget = Text(code_label, bg="white", font=(self.default_font, 10))
        code_widget.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)
        
    def output_draw(self):
        output_label = LabelFrame(self.root, font=(self.default_font, 10), text="Output")
        output_label.grid(row = 1, column = 0, sticky="nsew", padx=10, pady=10)

        output_label.columnconfigure(0, weight=1)
        output_label.rowconfigure(0, weight=1)

        output_widget = Text(output_label, bg="white", font=(self.default_font, 10))
        output_widget.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

class IDEMain:
    def __init__(self):
        self.root = Tk()
        self.app = Window(self.root)
        self.window_config()

    def window_config(self):
        self.width = 800
        self.height = 800
        self.background_colour = "#F0F0F0"
        self.default_font = "Helvetica"

        self.root.wm_title("ERL IDE")
        self.root.wm_iconbitmap("icon.ico")
        self.root.geometry(f"{self.width}x{self.height}+100+100")
        self.root.resizable(True, True)
        self.root.configure(background=self.background_colour)

        self.root.bind("<F5>", self.app.runButton)
        self.root.bind("<Escape>", lambda x: self.on_close())
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.create_sizegrip()

    def create_sizegrip(self):
        self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        my_sizegrip = ttk.Sizegrip(self.root)
        my_sizegrip.grid(row=2, sticky="SE")
        # my_sizegrip.pack(side="right", anchor="se")

    def on_close(self):
        response = messagebox.askyesno('Exit', 'Are you sure you want to exit\nAny unsaved changes will be lost')
        if response:
            self.root.destroy()
            exit()

    def draw(self):
        tabControl = ttk.Notebook(self.root)
        self.tabEDIT = ttk.Frame(tabControl)
        self.tabSHELL = ttk.Frame(tabControl)
        self.editor = IDEEditor(self.tabEDIT)
        self.shell = IDEShell(self.tabSHELL)
        tabControl.add(self.tabEDIT, text='Editor')
        tabControl.add(self.tabSHELL, text='Shell')
        tabControl.grid(row = 0, column = 0)

    def run(self):
        self.draw()
        self.root.mainloop()
        self.root.destroy()

ide = IDEMain()
ide.run()