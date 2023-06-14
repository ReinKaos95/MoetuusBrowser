#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 14:43:49 2022

@author: desarrollo04
"""
#PyQt5 packages
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


#Browser window
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
#Browser title
        self.setWindowTitle("Moetuus")
        self.setWindowIcon(QIcon("icons/internet-browsing.png"))
        self.setGeometry(800,600, 900,600)
        
#Browser toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
#Browser esssential buttons
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("icons/backward.png"))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("icons/reload.png"))
        self.reloadButton.setIconSize(QSize(36,36))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)
                
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/forward.png"))
        self.forwardButton.setIconSize(QSize(36,36))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)
        
        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/home.png"))
        self.homeButton.setIconSize(QSize(36,36))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)
        
        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif", 18))
        toolbar.addWidget(self.addressLineEdit)
        
        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("icons/search.png"))
        self.searchButton.setIconSize(QSize(36,36))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)
        
#Browser engine
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://google.com'
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

#Browser search engine

    def searchBtn(self):
        myurl=self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()
        
    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.webEngineView.load(QUrl('https://google.com'))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())