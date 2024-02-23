from context import BaseViewModel, reactive_property
from Models.FileModel import FileModel

class FileViewModel(BaseViewModel.BaseViewModel[FileModel]):
    
    __demo: str =""
    def __init__(self) -> None:
        super().__init__()
    
        
    @reactive_property
    def demo(self):
        return self.__demo
    
    @demo.setter
    def set_demo(self,value:str):
        self.__demo = value
    
    def display(self):
        pass