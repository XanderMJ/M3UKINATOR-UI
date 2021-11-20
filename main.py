import tkinter as tk
from tkinter import Menu, ttk
from ttkbootstrap import Style

class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.minsize(1200,720)
        self.title("M3UKINATOR v0.3.3")
        self.wm_iconbitmap('data/spotify.ico')
        self.sytle = Style(theme='darkly')

        self.create_tabs()
        # self.create_menu()

    def create_tabs(self):
        tabControl = ttk.Notebook(self)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
 
        tabControl.add(tab1, text='Spotify Search')
        tabControl.add(tab2, text='Settings')
        tabControl.add(tab3, text='Login')
        tabControl.pack(expand=1, fill='both')

    def create_menu(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        settings_menu = Menu(menubar, tearoff = 0)
 
        menubar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label='Login to Spotify')
        settings_menu.add_separator()
        settings_menu.add_command(label='Artist Search Settings')
        settings_menu.add_command(label='Song Search Settings')


    def callBack(self):
        pass

def main():
    # root = tk.Tk()
    app = App()#Inherit
    
    app.mainloop()
    print(app.tab1)

if __name__ == "__main__":
    main()