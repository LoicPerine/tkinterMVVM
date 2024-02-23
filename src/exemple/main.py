# import tkinter as tk
from Views.MainWindow import MainWindow
from Views.MainView import MainView

window = MainWindow()
mainView = MainView()
window.show(mainView)
window.mainloop()
