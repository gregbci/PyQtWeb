from PyQt6.QtCore import QUrl, pyqtSlot
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QLineEdit, QMainWindow, QPushButton, QToolBar)
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        initialUrl = "https://instagram.com"

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon(":/qt-project.org/styles/commonstyle/images/left-32.png"))
        self.backButton.clicked.connect(self.backPressed)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon(":/qt-project.org/styles/commonstyle/images/right-32.png"))
        self.forwardButton.clicked.connect(self.forwardPressed)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.returnPressed.connect(self.addressChanged)
        self.addressLineEdit.setText(initialUrl)

        self.scrollButton = QPushButton()
        self.scrollButton.setText("Scroll Test")
        self.scrollButton.clicked.connect(self.scrollPressed)

        self.toolBar = QToolBar()
        self.toolBar.addWidget(self.backButton)
        self.toolBar.addWidget(self.forwardButton)
        self.toolBar.addWidget(self.addressLineEdit)
        self.toolBar.addWidget(self.scrollButton)

        self.webEngineView = QWebEngineView()
        self.webEngineView.load(QUrl(initialUrl))
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)

        self.addToolBar(self.toolBar)
        self.setCentralWidget(self.webEngineView)
        self.setWindowTitle("PyQtWebEngine example application")

    @pyqtSlot()
    def addressChanged(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    @pyqtSlot()
    def backPressed(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Back)

    @pyqtSlot()
    def forwardPressed(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Forward)

    @pyqtSlot(QUrl)
    def urlChanged(self, url):
        self.addressLineEdit.setText(url.toString())

    @pyqtSlot()
    def scrollPressed(self):
        self.webEngineView.page().runJavaScript("window.scrollTo(0, 1000);")
