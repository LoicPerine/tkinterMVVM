from collections.abc import Callable
from typing import Any

from mvvm.Bases.base_view_model import BaseViewModel


class reactive_property(property):
    name: str

    def __needs_to_be_added(self, owner: BaseViewModel) -> bool:
        fget = self.fget
        fset = self.fset
        fdel = self.fdel
        if fget is not Ellipsis or fset is not Ellipsis or fdel is not Ellipsis:
            return (
                (
                    fget is not Ellipsis
                    and fget.__name__ not in owner._ui_reactive_properties
                )
                and (
                    fset is not Ellipsis
                    and fset.__name__ not in owner._ui_reactive_properties
                )
                and (
                    fdel is not Ellipsis
                    and fdel.__name__ not in owner._ui_reactive_properties
                )
            )
        raise ValueError("fget, fset or fdel should be defined")  # should NEVER happen

    def __set_name__(self, owner: BaseViewModel, name):
        self.name = name
        if hasattr(owner, "_ui_reactive_properties"):
            if self.__needs_to_be_added(owner):
                owner._ui_reactive_properties.append(name)
        else:
            owner._ui_reactive_properties = []
        print(owner._ui_reactive_properties)

    def __init__(
        self,
        fget: Callable[[BaseViewModel], Any] | None = ...,
        fset: Callable[[BaseViewModel, Any], None] | None = ...,
        fdel: Callable[[BaseViewModel], None] | None = ...,
        doc: str | None = ...,
    ) -> None:
        super().__init__(fget, fset, fdel, doc)

    def __set__(self, __instance: BaseViewModel, __value: Any) -> None:
        super().__set__(__instance, __value)
        __instance._notify_update(self.name, value=__value)
