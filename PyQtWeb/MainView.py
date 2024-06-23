from PySide6.QtCore import QUrl, QEvent, Qt, QCoreApplication, Slot
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtWidgets import QWidget, QLineEdit, QMainWindow, QPushButton, QToolBar, QHBoxLayout
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        initialUrl = "https://www.youtube.com/shorts/"

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

        self.box = QWidget()
        layout_box = QHBoxLayout(self.box)
        layout_box.setContentsMargins(20, 20, 20, 20)
        layout_box.addWidget(self.webEngineView)
        self.box.setLayout(layout_box)

        self.addToolBar(self.toolBar)
        self.setCentralWidget(self.box)
        self.setWindowTitle("PyQtWebEngine example application")

    @Slot()
    def addressChanged(self):
        url = QUrl.fromUserInput(self.addressLineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    @Slot()
    def backPressed(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Back)

    @Slot()
    def forwardPressed(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Forward)

    @Slot(QUrl)
    def urlChanged(self, url):
        self.addressLineEdit.setText(url.toString())

    @Slot()
    def scrollPressed(self):
        event = QKeyEvent(QEvent.Type.KeyPress, Qt.Key.Key_Down, Qt.KeyboardModifier.NoModifier)
        QCoreApplication.sendEvent(self.webEngineView.focusProxy(), event)
        QCoreApplication.processEvents()
