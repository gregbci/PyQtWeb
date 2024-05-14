from PyQt6.QtCore import QUrl, pyqtSlot
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QLineEdit,
    QMainWindow,
    QPushButton,
    QToolBar,
)
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtWebEngine example application")

        self.toolBar = QToolBar()
        self.addToolBar(self.toolBar)
        self.backButton = QPushButton()
        self.backButton.setIcon(
            QIcon(":/qt-project.org/styles/commonstyle/images/left-32.png")
        )
        self.backButton.clicked.connect(self.back)
        self.toolBar.addWidget(self.backButton)
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(
            QIcon(":/qt-project.org/styles/commonstyle/images/right-32.png")
        )
        self.forwardButton.clicked.connect(self.forward)
        self.toolBar.addWidget(self.forwardButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.returnPressed.connect(self.load)
        self.toolBar.addWidget(self.addressLineEdit)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = "https://possneuro.com"
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)

    @pyqtSlot()
    def load(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    @pyqtSlot()
    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    @pyqtSlot()
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    @pyqtSlot(QUrl)
    def urlChanged(self, url):
        self.addressLineEdit.setText(url.toString())
