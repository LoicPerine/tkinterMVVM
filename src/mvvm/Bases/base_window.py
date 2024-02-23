from tkinter import Tk
from typing import Optional
from abc import ABC
from mvvm.Bases.base_view import BaseView

from mvvm.Bases.base_view_model import BaseViewModel

class BaseWindow(Tk,ABC):

    __current_view: Optional[BaseViewModel]

    @property
    def current_view(self)-> BaseView:
        return self.__current_view
    
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        self.__current_view = None
        super().__init__(screenName, baseName, className, useTk, sync, use)

    

    def show(self,view: 'BaseView', **viewParams):
        childs = self.winfo_children()
        for child in childs:
            child.pack_forget()

        if self.__current_view is not None:
            self.__current_view
        view.create_widgets(window=self,kwargs=viewParams)
        self.__current_view = view

    
    def reset(self):
        """
        clears the window of all it's widgets (calling pack on them will be needed again)
        """
        for child in super(Tk).winfo_children():
            child.pack_forget()

    