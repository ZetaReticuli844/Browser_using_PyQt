import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import re
import os

class WebBrowser(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(WebBrowser,self).__init__(*args,**kwargs)
        self.window=QWidget()
        self.setWindowTitle("Web Browser")
        self.layout=QVBoxLayout()
        self.horizontal=QHBoxLayout()
    

        
        self.url_bar=QLineEdit()
        self.url_bar.setMaximumHeight(30)
     
        
        self.go_button=QPushButton("Go")
        self.go_button.setMinimumHeight(30)
        
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
        self.browser.setUrl(QUrl("file:///" + os.path.join(os.getcwd(), "home.html")))
        self.go_button.clicked.connect(lambda:self.navigate(self.url_bar.text()))
        self.url_bar.returnPressed.connect(lambda:self.navigate(self.url_bar.text()))
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)
        
        self.window.setLayout(self.layout)
        self.window.show()
        
    def navigate(self,url):
        if re.match('^(http|https)://', url):
            self.url_bar.setText(url)
        else:
            url = "https://www.google.com/search?q=" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
        
app=QApplication([])
window=WebBrowser()
app.exec_()