from abc import ABC, abstractmethod
from tkinter import Misc
from typing import TYPE_CHECKING
if TYPE_CHECKING: #let's avoid cyclic dependencies lol
    from mvvm.Bases.base_window import BaseWindow





class BaseView(ABC, Misc ):
    def __init__(self) -> None:
        super().__init__()
    @abstractmethod
    def display(self,window: 'BaseWindow',**kwargs):
        raise NotImplementedError("this should be implemented by child classes")
    
    @abstractmethod
    def reset(self):
        raise NotImplementedError("this should be implemented by child classes")