from abc import ABC
from typing import TypeVar, Generic

T = TypeVar('T')

class BaseViewModel(ABC,Generic[T]):
    data: T

    def __init__(self) -> None:
        super().__init__()
    
    def _notify_update(self,name:str,value:any):
        print(f"{name} has been updated with value {value}")