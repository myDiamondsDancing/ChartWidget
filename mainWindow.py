import sys

from PyQt5.Qt import *

from chartWidget import ChartWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()
        self.connectUi()
        self.setLightTheme()

    def initUi(self):
        self.darkB = QPushButton('Dark')
        self.grayB = QPushButton('Gray')
        self.lightB = QPushButton('Light')
        self.setTT = QPushButton('On Tool tips')
        self.delTT = QPushButton('Delete tool tips')

        self.themeL = QHBoxLayout()
        self.themeL.addWidget(self.darkB)
        self.themeL.addWidget(self.grayB)
        self.themeL.addWidget(self.lightB)
        self.themeL.addWidget(self.setTT)
        self.themeL.addWidget(self.delTT)
        
        self.w = QWidget()        
        
        self.main = ChartWidget()
        self.mainL = QVBoxLayout(self.w)
        self.mainL.addLayout(self.themeL)
        self.mainL.addWidget(self.main)

        self.setCentralWidget(self.w)
        
    def connectUi(self):
        self.darkB.clicked.connect(self.setDarkTheme)
        self.grayB.clicked.connect(self.setGrayTheme)
        self.lightB.clicked.connect(self.setLightTheme)
        self.setTT.clicked.connect(self.setToolTips)
        self.delTT.clicked.connect(self.deleteToolTips)

    def setDarkTheme(self):
        self.setStyleSheet("background : rgb(103, 103, 103);")
        self.main.setTheme(2)
        self.darkB.setEnabled(False)
        self.grayB.setEnabled(True)
        self.lightB.setEnabled(True)

    def setGrayTheme(self):
        self.setStyleSheet("background : rgb(176, 176, 176);")
        self.main.setTheme(1)
        self.darkB.setEnabled(True)
        self.grayB.setEnabled(False)
        self.lightB.setEnabled(True)  

    def setLightTheme(self):
        self.setStyleSheet("background : rgb(238, 238, 238);")
        self.main.setTheme(0)
        self.darkB.setEnabled(True)
        self.grayB.setEnabled(True)
        self.lightB.setEnabled(False)  

    def setToolTips(self):
        for widget in self.main.area.listOfWidgets:
            widget.setToolTips(True)

    def deleteToolTips(self):
        for widget in self.main.area.listOfWidgets:
            widget.deleteToolTips(False)               

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()  
