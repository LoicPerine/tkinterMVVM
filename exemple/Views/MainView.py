from tkinter import Button, Label
from typing import Optional
from Bases.BaseView import BaseView
from Views.MainWindow import MainWindow


class MainView(BaseView):
    theme:bool # true -> Light, False -> dark
    ### Tkinter components, these need to be reset on reset() call
    __label: Optional[Label]  # privated (can still be accessed via name mangling)
    __display_file_button: Optional[Button]
    __theme_swap_button: Optional[Button]

    def __init__(self) -> None:
        super().__init__()
        self.theme = True # light theme by default 

    def display(self,window: MainWindow,**kwargs):
        window.rowconfigure(7)
        window.columnconfigure(21)
        self.__label = Label(window, text="henlo friendo, what should we do?")
        self.__label.grid(column=11, row=0)
        self.__theme_swap_button = Button(window,text="change theme",command=self.change_theme)
        self.__theme_swap_button.grid(column=6,row=6)
        self.__display_file_button =Button(window,text="display a raw file",command=self.open_raw)
        self.__display_file_button.grid(column=15,row=6)

    def reset(self):
        self.__label = None

    def change_theme(self):
        self.theme = not self.theme
    
    def open_raw(self):
        pass