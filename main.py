import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl

class WebBrowser(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(WebBrowser,self).__init__(*args,**kwargs)
        self.window=QWidget()
        self.setWindowTitle("Web Browser")
        self.layout=QVBoxLayout()
        self.horizontal=QHBoxLayout()
        
        self.url_bar=QTextEdit()
        self.url_bar.setMaximumHeight(30)
        
        self.go_button=QPushButton("Go")
        self.go_button.setMinimumhHeight(30)
        
        self.back_button=QPushButton("<")
        self.back_button.setMinimumHeight(30)
        
        self.forward_button=QPushButton(">")
        self.forward_button.setMinimumHeight(30)
        
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_button)
        self.horizontal.addWidget(self.back_button)
        self.horizontal.addWidget(self.forward_button)
        
        self.browser=QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        self.window.setLayout(self.layout)
        self.window.show()
        
app=QApplication([])
window=WebBrowser()
app.exec_()        
        
        
        
        
        
        