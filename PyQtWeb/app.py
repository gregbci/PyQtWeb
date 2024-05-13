import sys
from PyQt6.QtWidgets import QApplication

from .MainView import MainView
#from .TrainingController import TrainingController


def start():
    app = QApplication(sys.argv)

    # inject view into controller
    view = MainView()
    #controller = TrainingController(view)

    # show view and begin Qt event loop
    view.show()
    app.exec()
