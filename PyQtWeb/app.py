import sys
from PyQt6.QtWidgets import QApplication

from .MainView import MainView

# from .TrainingController import TrainingController


def start():
    app = QApplication(sys.argv)

    # create main view and make it large enough to show "desktop" sized screen
    view = MainView()
    screenRect = view.screen().availableGeometry()
    width = int(screenRect.width() * 0.75)
    height = int(screenRect.height() * 0.75)
    view.resize(width, height)

    # inject view into controller
    # controller = TrainingController(view)

    # show view and begin Qt event loop
    view.show()
    app.exec()
