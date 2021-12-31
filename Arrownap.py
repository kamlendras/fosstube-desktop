import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
 def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://arrownap.github.io'))
        self.setCentralWidget(self.browser)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Arrow Nap')
        self.setWindowIcon(QIcon('nap.png')) 
        self.showMaximized()

app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
