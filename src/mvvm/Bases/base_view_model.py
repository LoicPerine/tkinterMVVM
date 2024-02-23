from abc import ABC, abstractmethod
from typing import Any, Callable, Self
from mvvm.observable_list import ObservableList



class BaseViewModel(ABC):
    __ui_reactive_properties: list[str] =[]
    __prop_bindings:dict[str,list[Callable[[Self,Any],None]]]

    def __init__(self) -> None:
        self.__prop_bindings  = {}
    
    def _notify_update(self,name:str,value:Any):
        for listener in self.__prop_bindings.get(name):
            listener(self,value)
    
    
    def create_observable_list(values: list):
        return ObservableList(values)
    
    def bind_property(self,property_name:str, command: Callable[[Self,Any],None])-> None:
        if property_name not in self.__class__.__ui_reactive_properties:
            raise ValueError(f"object of type :{self.__class__} has no reactive property named: {property_name}")
        if property_name not in self.__prop_bindings.keys():
            self.__prop_bindings[property_name] = []
        self.__prop_bindings[property_name].append(command)