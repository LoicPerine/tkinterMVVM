from context import BaseViewModel, reactive_property

class FileViewModel(BaseViewModel):
    
    __demo: str =""
    def __init__(self) -> None:
        super().__init__()
    
        
    @reactive_property
    def demo(self):
        return self.__demo
    
    @demo.setter
    def set_demo(self,value:str):
        self.__demo = value
    
    def create_widgets(self):
        pass