import tkinter as tk
from ViewModels.FileViewModel import FileViewModel
from Views.MainWindow import MainWindow
from Views.MainView import MainView
def listener(source:FileViewModel, value:str):
    print("let's goooo")
test = FileViewModel()
test.bind_property("demo",listener)
test.demo = 10
