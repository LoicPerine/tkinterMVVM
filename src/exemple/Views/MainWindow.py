from context import BaseWindow


class MainWindow(BaseWindow):
    def __init__(self) -> None:
        super().__init__("Main Window")
        self.geometry("1280x720")