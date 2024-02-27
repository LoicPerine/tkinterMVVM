from collections.abc import Callable
from typing import Any, Union
from types import EllipsisType
from mvvm.Bases.base_view_model import BaseViewModel


class reactive_property(property):
    name: str


    def __set_name__(self, owner: type[BaseViewModel], name:str):
        super().__set_name__(owner,name)
        self.name = name
        if hasattr(owner, "_ui_reactive_properties"):
            if self.__needs_to_be_added(owner): 
                owner._ui_reactive_properties.append(name)
        else:
            owner._ui_reactive_properties = []
            owner._ui_reactive_properties.append(name)
    
    def __set__(self, __instance: BaseViewModel, __value: Any) -> None:
        super().__set__(__instance, __value)
        __instance._notify_update(self.name, value=__value)

    def __needs_to_be_added(self, owner: type[BaseViewModel]) -> bool:
        """ 
        Function used to avoid duplication of properties 
        """
        fget = self.fget
        fset = self.fset
        fdel = self.fdel

        if fget is not None or fset is not None or fdel is not None:
            if fget is not None and fget.__name__ in owner._ui_reactive_properties:
                return False
            if fset is not None and fset.__name__ in owner._ui_reactive_properties:
                return False
            if fdel is not None and fdel.__name__ in owner._ui_reactive_properties:
                return False
            return True
        raise ValueError("fget, fset or fdel should be defined")  # should NEVER happen