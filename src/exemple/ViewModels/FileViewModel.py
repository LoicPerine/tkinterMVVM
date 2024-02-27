from context import BaseViewModel, reactive_property

class FileViewModel(BaseViewModel):
    _demo:str

    def __init__(self) -> None:
        self._demo = "&"
        super().__init__()
    
        
    @reactive_property
    def demo(self):
        return self.__demo

    @demo.setter
    def demo(self, value):
        self.__demo = value
    
    def create_widgets(self):
        pass