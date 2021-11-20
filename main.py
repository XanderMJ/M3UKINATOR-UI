import tkinter as tk
from tkinter import Menu, StringVar, ttk
from ttkbootstrap import Style

from src.backend import Client
import os

class App(tk.Tk):

    def __init__(self):
        super(App, self).__init__()
        self.minsize(1200,720)
        self.title("M3UKINATOR v0.3.3")
        self.wm_iconbitmap('data/spotify.ico')
        self.sytle = Style(theme='darkly')
        self.create_tabs()

        # self.Backend = Client()
        self.code = None
        self.token = None

    def create_tabs(self):
        tabControl = ttk.Notebook(self)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        # tab3 = ttk.Frame(tabControl)
 
        tabControl.add(tab1, text='Spotify Search')
        tabControl.add(tab2, text='Settings')
        # tabControl.add(tab3, text='Login')
        tabControl.pack(expand=1, fill='both')

        self.search_page(tab1)
        self.settings_page(tab2)
        # self.login_page(tab3)



    def create_menu(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        settings_menu = Menu(menubar, tearoff = 0)
 
        menubar.add_cascade(label="Settings", menu=settings_menu)
        settings_menu.add_command(label='Login to Spotify')
        settings_menu.add_separator()
        settings_menu.add_command(label='Artist Search Settings')
        settings_menu.add_command(label='Song Search Settings')


    def settings_page(self, page):
        pass

    def search_page(self, page):
        pass


    def callBack(self):
        pass




def login():
    from data.client_info import CLIENT_ID,CLIENT_SECRET,REDIRECT_URI
    import tekore as spotify
    scope = spotify.scope.every
    file = 'tekore.cfg'

    if os.path.isfile(file):
        conf = spotify.config_from_file(file, return_refresh=True)
        token = spotify.refresh_user_token(*conf[:2], conf[3])
    else:
        print(f"{file} not found, log-in to spotify and paste URL in commandline",)
        conf = (CLIENT_ID,CLIENT_SECRET,REDIRECT_URI)
        token = spotify.prompt_for_user_token(*conf, scope=scope)
        spotify.config_to_file(file, conf + (token.refresh_token,))
    return token

def main():
    token = login()
    app = App()    
    app.mainloop()



if __name__ == "__main__":
    main()