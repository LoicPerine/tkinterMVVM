from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING: #let's avoid cyclic dependencies lol
    from mvvm.Bases.BaseWindow import BaseWindow





class BaseView(ABC):
    
    @abstractmethod
    def display(self,window: 'BaseWindow',**kwargs):
        raise NotImplementedError("this should be implemented by child classes")
    
    @abstractmethod
    def reset(self):
        raise NotImplementedError("this should be implemented by child classes")