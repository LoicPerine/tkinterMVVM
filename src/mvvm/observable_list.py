from typing import Generic, Optional,TypeVar
from enum import Enum
from typing import Self, Callable

T = TypeVar('T')

class MODIFICATION_TYPE(Enum):
    APPENDED =1
    REMOVED =2
    MODIFIED =3

class ObservableList(list, Generic[T]):
    listeners : list[Callable[[Self,MODIFICATION_TYPE,Optional[T],T],None]] = []

    def __init__(values: list[T]):
        super(list).__init__()
        for value in values:
            super(list).append(value)

    def append(self, __object: T) -> None:
        super().append()
        self.__raise_event_modified(MODIFICATION_TYPE.APPENDED,None,__object)
    
    def __raise_event_modified(self,type:MODIFICATION_TYPE,old:Optional[T] ,new:T):
        for listener in self.listeners:
            listener(self,type,None,new)

    