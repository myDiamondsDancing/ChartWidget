import sys
import sip

from PyQt5.Qt import *

from chartSettingsWidget import ChartSettingsWidget

class ScrollWidget(QWidget):      
    def __init__(self, parent=None):
        super(ScrollWidget, self).__init__(parent)
        self.initUi()
        self.connectUi()
        self.loadFields()

    def initUi(self):
        '''|initUi(self)
         |private method : inits user interface in widget'''
        self.layoutV = QVBoxLayout(self)

        self.area = QScrollArea(self)
        self.area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()

        self.layoutH = QHBoxLayout(self.scrollAreaWidgetContents)
        self.gridLayout = QGridLayout()
        self.layoutH.addLayout(self.gridLayout)

        self.area.setWidget(self.scrollAreaWidgetContents)
        self.layoutV.addWidget(self.area)
      
    def connectUi(self):
        pass
        
    def loadFields(self):
        '''|loadFields(self)
         |private method : loads local fields(listOfWidgets, theme, toolTips)'''
        self.listOfWidgets = list()
        self.theme = 0      
        self.toolTips = True

    def setTheme(self, theme):    
        '''|setTheme(self, flag)
         |flag : (0, 1, 2) 
         |public method : sets theme for widgets in scrollArea
         |setTheme(theme) >>> None '''       
        if theme == 0:
            self.setLightTheme()
            self.theme = 0
        elif theme == 1:
            self.setGrayTheme()
            self.theme = 1
        else:
            self.setDarkTheme()
            self.theme = 2
            
    def setLightTheme(self):
        '''|setLightTheme(self)
         |private method : sets light theme for widgets in scrollArea'''        
        self.setStyleSheet("background : rgb(238, 238, 238)")
        for widget in self.listOfWidgets:
            widget.setTheme(0)

    def setGrayTheme(self):
        '''|setGrayTheme(self)
          private method : sets gray theme for widgets in scrollArea'''        
        self.setStyleSheet("background : rgb(176, 176, 176)")
        for widget in self.listOfWidgets:
            widget.setTheme(1)

    def setDarkTheme(self):
        '''|setDarkTheme(self)
         |private method : sets dark theme for widgets in scrollArea'''    
        self.setStyleSheet("background : rgb(103, 103, 103)")
        for widget in self.listOfWidgets:
            widget.setTheme(2)            
            
    def addWidget(self):
        '''|addWidget(self)
         |public method : adds chartSettingsWidget to scrollArea
         |addWidget >>> None'''       
        widget = ChartSettingsWidget()                           # Adding new widget
        self.gridLayout.addWidget(widget)
        self.listOfWidgets.append(widget)         # For getting results and changing theme
        widget.deleteButton.clicked.connect(lambda : self.deleteWidget(widget))
        widget.setTheme(self.theme)                    # Changing theme for new widget
              

    def deleteWidget(self, widget):
        '''|deleteWidget(self, widget)
         |widget : chartSettingsWidget
         |private method : deletes widget from scrollArea(connected with deleteButton on each chartSettingsWidget)'''
        self.listOfWidgets.remove(widget)
        self.gridLayout.removeWidget(widget)
        sip.delete(widget)
        del widget
