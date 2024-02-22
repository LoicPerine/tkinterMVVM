from abc import ABC, abstractmethod

from exemple.Views.MainWindow import MainWindow


class BaseView(ABC):
    
    @abstractmethod
    def display(self,window: MainWindow,**kwargs):
        raise NotImplementedError("this should be implemented by child classes")
    
    @abstractmethod
    def reset(self):
        raise NotImplementedError("this should be implemented by child classes")