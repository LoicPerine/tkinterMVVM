from collections.abc import Callable
from typing import Any

from Bases.BaseViewModel import BaseViewModel


class reactive_property(property):
    name:str
    def __set_name__(self,owner,name):
        self.name = name

    def __init__(self, fget: Callable[[BaseViewModel], Any] | None = ..., fset: Callable[[BaseViewModel, Any], None] | None = ..., fdel: Callable[[BaseViewModel], None] | None = ..., doc: str | None = ...) -> None:
        super().__init__(fget, fset, fdel, doc)
    
    def __set__(self, __instance: BaseViewModel, __value: Any) -> None:
        super().__set__(__instance, __value)
        try:
            __instance._notify_update(self.name,value=__value)
        except Exception:
            pass
