from collections.abc import Callable
from typing import Any

from mvvm.Bases.base_view_model import BaseViewModel


class reactive_property(property):
    name:str
    def __set_name__(self,owner: BaseViewModel,name):
        self.name = name
        if not hasattr(owner, '__ui_reactive_properties'):
            owner.__ui_reactive_properties = []
        owner.__ui_reactive_properties.append(name)
    def __init__(self, fget: Callable[[BaseViewModel], Any] | None = ..., fset: Callable[[BaseViewModel, Any], None] | None = ..., fdel: Callable[[BaseViewModel], None] | None = ..., doc: str | None = ...) -> None:
        super().__init__(fget, fset, fdel, doc)
    
    def __set__(self, __instance: BaseViewModel, __value: Any) -> None:
        super().__set__(__instance, __value)
        __instance._notify_update(self.name,value=__value)
