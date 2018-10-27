import sys
import sip

import numpy as np

from PyQt5.Qt import *
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from scrollWidget import ScrollWidget

class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super(ChartWidget, self).__init__(parent)
        self.initUi()
        self.connectUi()
        self.loadFields()
        self.setTheme(self.theme)
        
    def initUi(self):
        '''private method : inits user interface'''
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure) 
        self.toolBar = NavigationToolbar(self.canvas, self)
        
        self.drawAreaLayout = QVBoxLayout()
        self.drawAreaLayout.addWidget(self.canvas)
        self.drawAreaLayout.addWidget(self.toolBar)
        
        self.addButton = QPushButton('Add chart')
        self.saveButton = QPushButton('Save img')
        self.plotButton = QPushButton('Plot')
        
        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.addWidget(self.addButton)
        self.buttonsLayout.addWidget(self.saveButton)
        
        self.area = ScrollWidget()
        
        self.areaLayout = QVBoxLayout()
        self.areaLayout.addLayout(self.buttonsLayout)
        self.areaLayout.addWidget(self.area)
        self.areaLayout.addWidget(self.plotButton)
        
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.areaLayout)
        self.mainLayout.addLayout(self.drawAreaLayout)
        
        self.setLayout(self.mainLayout)
        
    def loadFields(self):
        '''|loadFields(self)
       |private method : loads local field(theme)'''
        self.theme = 0     
        
    def connectUi(self):
        '''private method : connects all needed signals with class methods'''
        self.addButton.clicked.connect(self.area.addWidget)
        self.plotButton.clicked.connect(self.plot)
        
    def plot(self):
        '''|plot(self)
       |public method : plots chart is canvas using chartSettingsWidget.results
       |plot >>> True if plotting is success else False '''
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        i = 1
        for widget in self.area.listOfWidgets:
            xMin, xMax, func, label, format, color = widget.results()
            x = np.linspace(xMin, xMax, (xMax - xMin * 1000))
            try:
                y = eval(func)
            except Exception as ex:
                self.showDialog('Error of function(widget {0})'.format(i))
                return False
            try:
                ax.plot(x, y, label=label, color=color, linestyle=format)
                ax.legend(loc='best')               
                self.canvas.draw()
            except Exception as ex:
                self.showDialog('Error of ploting (widget{0})\n{1}'.format(i, ex))
                return False 
            i += 1  
        return True            
        
    def setTheme(self, flag):
        '''|setTheme(self, flag)
       |flag : (0: Light, 1: Gray, 2: Dark) 
       |public method : sets theme for widgets
       |setTheme >>> None'''
        self.theme = flag
        if flag == 0:
            self.setLigthTheme()
        elif flag == 1:
            self.setGrayTheme()
        else:
            self.setDarkTheme()        

    def setLigthTheme(self):
        '''|setLigthTheme(self)
       |private method : sets light theme for widgets'''
       
        self.setStyleSheet("background : rgb(238, 238, 238);")
        self.area.setTheme(0)    

    def setGrayTheme(self):
        '''|setGrayTheme(self)
       |private method : sets gray theme for widgets''' 
        self.setStyleSheet("background : rgb(176, 176, 176);") 
        self.area.setTheme(1)

    def setDarkTheme(self):
        '''|setGrayTheme(self)
       |private method : sets dark theme for widget''' 
        self.setStyleSheet("background : rgb(103, 103, 103);")
        self.area.setTheme(2)  
        
    def showDialog(self, text):
        '''|showDialog(self, text)
       |text : String
       |private method : shows error dialog with input text'''         
        dlg = QMessageBox(self)
        dlg.setText(text)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()                 
            
       
