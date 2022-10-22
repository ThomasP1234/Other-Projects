# TODO config file to edit default keybinds
# On finish change to .pyw to hide console

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from console import Console

class IDEShell:
    def __init__(self, root):
        self.master = Toplevel(root)
        self.window_config()

    def window_config(self):
        self.width = 800
        self.height = 800
        self.background_colour = "#F0F0F0"
        self.default_font = "Helvetica"

        self.master.wm_title("ERL IDE")
        self.master.wm_iconbitmap("icon.ico")
        self.master.geometry(f"{self.width}x{self.height}+100+100")
        self.master.resizable(True, True)
        self.master.configure(background=self.background_colour)

        self.create_sizegrip()
        self.draw()

    def create_sizegrip(self):
        self.master.columnconfigure(0, weight=1)
        # self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)

        my_sizegrip = ttk.Sizegrip(self.master)
        my_sizegrip.grid(row=2, sticky="SE")
        # my_sizegrip.pack(side="right", anchor="se")

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
    def __init__(self):
        self.root = Tk()
        self.app = Window(self.root)
        self.window_config()
        self.output = False
        self.output_items = []

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
        self.app.exitButton()

    def draw(self):
        title = Label(self.root, font=(self.default_font, 25), text="ERL IDE")
        title.grid(row = 0, column = 0, sticky="nsew")

        self.code_draw()
        self.output_draw()

    def code_draw(self):
        code_label = LabelFrame(self.root, font=(self.default_font, 10), text="Code")
        code_label.grid(row = 1, column = 0, sticky="nsew", padx=10, pady=10)

        code_label.columnconfigure(0, weight=1)
        code_label.rowconfigure(0, weight=1)

        code_widget = Text(code_label, bg="white", font=(self.default_font, 10))
        code_widget.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)
        
    def output_draw(self):
        output_label = LabelFrame(self.root, font=(self.default_font, 10), text="Output")
        output_label.grid(row = 2, column = 0, sticky="nsew", padx=10, pady=10)

        output_label.columnconfigure(0, weight=1)
        output_label.rowconfigure(0, weight=1)

        output_widget = Text(output_label, bg="white", font=(self.default_font, 10))
        output_widget.grid(row = 0, column = 0, sticky="nsew", padx=10, pady=10)

        self.output_items.extend([output_label, output_widget])

    def run(self):
        self.draw()
        self.root.mainloop()

    def quit(self):
        self.root.quit()

ide = IDEEditor()
ide.run()
ide.quit()