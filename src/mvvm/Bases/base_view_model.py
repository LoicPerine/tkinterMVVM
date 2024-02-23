from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseViewModel(ABC,Generic[T]):
    data: T

    def __init__(self) -> None:
        pass
    
    def _notify_update(self,name:str,value:any):
        print(f"{name} has been updated with value {value}")
    
    @abstractmethod
    def display(self):
        raise NotImplementedError("this should be implemented by subclasses")