from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout


# Subclass QMainWindow to customize your application's main window
class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtFun")

        self.button = QPushButton("Train")

        self.label = QLabel("Press Train!")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        main = QWidget()
        main.setLayout(layout)
        self.setCentralWidget(main)

    @QtCore.pyqtSlot()
    def display_training_start(self):
        self.label.setText("training...")

    @QtCore.pyqtSlot(int)
    def display_training_count(self, count):
        self.label.setText("training count is " + str(count))
