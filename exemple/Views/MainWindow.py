from tkinter import Tk, Label, Button
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from Bases.BaseView import BaseView #band-aid to avoid cyclic imports, so are are 'ClassName'


class MainWindow(Tk):

    __currentView: Optional['BaseView']

    def __init__(self):
        super().__init__("main window")
        self.geometry("1366x768")

    def show(self,view: 'BaseView', **viewParams):
        childs = self.winfo_children()
        for child in childs:
            child.destroy()
            if self.__currentView is not None:
                self.__currentView.reset()
        view.display(window=self,kwargs=viewParams)
        self.__currentView = view
    