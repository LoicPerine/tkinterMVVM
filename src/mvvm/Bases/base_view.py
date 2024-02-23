from abc import ABC, abstractmethod
from tkinter import Frame
from typing import TYPE_CHECKING, Generic, TypeVar

from mvvm.Bases.base_view_model import BaseViewModel

if TYPE_CHECKING:  # let's avoid cyclic dependencies lol
    from mvvm.Bases.base_window import BaseWindow

T = TypeVar("T", bound=BaseViewModel)


class BaseView(Frame, ABC, Generic[T]):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def create_widgets(self, window: "BaseWindow", **kwargs):
        raise NotImplementedError("this should be implemented by child classes")

    @abstractmethod
    def reset(self):
        raise NotImplementedError("this should be implemented by child classes")
