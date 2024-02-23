import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mvvm.Bases import BaseView,BaseViewModel, BaseModel, reactive_property, BaseWindow
