import sys

import PyQt5.QtCore as QCore
from PyQt5.Qt import *

class ChartSettingsWidget(QWidget):
    def __init__(self, parent=None):
        super(ChartSettingsWidget, self).__init__(parent)
        self.loadFields()        
        self.initUi()
        self.connectUi()
        self.setTheme(0)
        self.setToolTips(True)
     
    def initUi(self):
    '''|initUi(self)
       |private method : loads interface of widget'''
        self.xLabel = QLabel('X:')
        
        self.xMinBox = QSpinBox(self)
        self.xMinBox.setRange(-1000, 999)
        self.xMinBox.setValue(-10)
        
        self.xMaxBox = QSpinBox(self)
        self.xMaxBox.setRange(-999, 1000)
        self.xMaxBox.setValue(10)
        
        self.deleteButton = QPushButton('Delete')
        self.deleteButton.setStyleSheet('background : red;')        
        
        self.xRangeLayout = QHBoxLayout()
        self.xRangeLayout.addWidget(self.xLabel)
        self.xRangeLayout.addWidget(self.xMinBox)
        self.xRangeLayout.addWidget(self.xMaxBox)
        self.xRangeLayout.addWidget(self.deleteButton)

        self.colorButton = QPushButton('Choose color')
        self.colorButton.setStyleSheet('background : blue;')
        
        self.fmtBox = QComboBox()
        self.fmtBox.addItem('...')
        self.fmtBox.addItem(',,,')
        self.fmtBox.addItem('ooo')
        self.fmtBox.addItem('vvv')
        self.fmtBox.addItem('^^^')
        self.fmtBox.addItem('<<<')
        self.fmtBox.addItem('>>>')
        self.fmtBox.addItem('111')
        self.fmtBox.addItem('222')
        self.fmtBox.addItem('333')
        self.fmtBox.addItem('444')
        self.fmtBox.addItem('888')
        self.fmtBox.addItem('sss')
        self.fmtBox.addItem('ppp')        
        self.fmtBox.addItem('PPP')
        self.fmtBox.addItem('***')        
        self.fmtBox.addItem('hhh')
        self.fmtBox.addItem('HHH')
        self.fmtBox.addItem('+++')
        self.fmtBox.addItem('xxx')
        self.fmtBox.addItem('XXX')
        self.fmtBox.addItem('ddd')
        self.fmtBox.addItem('DDD')
        self.fmtBox.addItem('|||')
        self.fmtBox.addItem('___')
        
        self.settingLayout = QHBoxLayout()
        self.settingLayout.addWidget(self.colorButton)
        self.settingLayout.addWidget(self.fmtBox)
        
        self.chartLegendLabel = QLabel('Chart legend :')
        
        self.chartLegendEdit = QLineEdit()
        
        self.legendLayout = QHBoxLayout()
        self.legendLayout.addWidget(self.chartLegendLabel)
        self.legendLayout.addWidget(self.chartLegendEdit)
        
        self.funcLabel = QLabel('y =  ')
        self.funcEdit = QLineEdit()
        
        self.functionLayout = QHBoxLayout()
        self.functionLayout.addWidget(self.funcLabel)
        self.functionLayout.addWidget(self.funcEdit)
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.xRangeLayout)
        self.mainLayout.addLayout(self.settingLayout)
        self.mainLayout.addLayout(self.legendLayout)
        self.mainLayout.addLayout(self.functionLayout)
        self.setLayout(self.mainLayout)
            
    def connectUi(self):
    '''|connectUi(self)
       |private method : connects all signals with private methods'''
        self.colorButton.clicked.connect(self.chooseColor)
        self.xMaxBox.valueChanged.connect(self.changedValueInMaxBox)
        self.xMinBox.valueChanged.connect(self.changedValueInMinBox)
        
    def loadFields(self):
    '''|loadFields(self)
       |private method : loads local fields(color, theme)''' 
        self.color = 'blue'
        self.theme = 0
        
    def chooseColor(self): 
    '''|chooseColor(self)
       |private method : chooses chart's color(connected with colorButton's click)'''
        dialog = QColorDialog(self)
        dialog.setCurrentColor(QColor(self.color))  

        if dialog.exec_():
            self.colorButton.setStyleSheet("background : {};".format(dialog.currentColor().name())) 
            self.color =  dialog.currentColor().name()

    def changedValueInMinBox(self):
    ''' If minimum of x is greater than maximum of x(connected with xMinBox.valueChanged)'''
        if self.xMinBox.value() > self.xMaxBox.value():
            self.xMaxBox.setValue(self.xMinBox.value() + 1)

    def changedValueInMaxBox(self): 
    '''If maximum ofx is smaller than minimum of x(connected with xMaxBox.valueChanged)'''
        if self.xMinBox.value() > self.xMaxBox.value():
            self.xMinBox.setValue(self.xMaxBox.value() - 1)       

    def setLightTheme(self):          
    '''|setLightTheme(self)
       |private method : sets light theme for widget'''
        _translate = QCore.QCoreApplication.translate
        self.setStyleSheet("background : rgb(238, 238, 238);")
        self.xMaxBox.setStyleSheet("background : rgb(252, 252, 252)")
        self.xMinBox.setStyleSheet("background : rgb(252, 252, 252)")
        self.chartLegendEdit.setStyleSheet("background : rgb(252, 252, 252)")
        self.xLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">X :</span></p></body></html>"))  
        self.funcLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">y(x) = </span></p></body></html>"))
        self.funcEdit.setStyleSheet("background : rgb(252, 252, 252)")
        self.chartLegendLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Chart legend</span></p></body></html>"))           
        self.fmtBox.setStyleSheet("background : rgb(252, 252, 252)")
            
    def setGrayTheme(self):    
    '''|setGrayTheme(self)
       |private method : sets gray theme for widget'''
        _translate = QCore.QCoreApplication.translate    
        self.setStyleSheet("background : rgb(176, 176, 176);")
        self.xMaxBox.setStyleSheet("background : rgb(232, 232, 232);")
        self.xMinBox.setStyleSheet("background : rgb(232, 232, 232);")
        self.chartLegendEdit.setStyleSheet("background : rgb(232, 232, 232);")
        self.fmtBox.setStyleSheet("background : rgb(232, 232, 232);") 
        self.xLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">X :</span></p></body></html>"))  
        self.funcLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">y(x) = </span></p></body></html>"))
        self.funcEdit.setStyleSheet("background : rgb(232, 232, 232)")        
        self.chartLegendLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Chart legend</span></p></body></html>"))         

    def setDarkTheme(self): 
    '''|setDarkTheme(self)
       |private method : sets dark theme for widget'''
        _translate = QCore.QCoreApplication.translate    
        self.setStyleSheet("background : rgb(103, 103, 103);")
        self.xMaxBox.setStyleSheet("background : rgb(182, 182, 182);")
        self.xMinBox.setStyleSheet("background : rgb(182, 182, 182);")
        self.chartLegendEdit.setStyleSheet("background : rgb(182, 182, 182);")
        self.fmtBox.setStyleSheet("background : rgb(182, 182, 182);")
        self.xLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ececec;\">X :</span></p></body></html>")) 
        self.funcLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ececec;\">y(x) = </span></p></body></html>"))
        self.funcEdit.setStyleSheet("background : rgb(182, 182, 182)")                
        self.chartLegendLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ececec;\">Chart legend</span></p></body></html>"))   
        
    def setToolTips(self, flag):
    '''|setToolTips(self, flag)
       |flag : True, False 
       |public method : on or off tooltips
       |setToolTips(flag) >>> None'''
        if flag is True:
              self.onToolTips()
        else:
              self.deleteToolTips()        
        
    def onToolTips(self):
    '''|onToolTips(self)
       |private method : set tooltips for all widgets'''
        _translate = QCore.QCoreApplication.translate
        self.colorButton.setToolTip(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Color of chart</span></p></body></html>"))
        self.xMinBox.setToolTip(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Minimum of X</span></p></body></html>"))
        self.xMaxBox.setToolTip(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Maximum of x</span></p></body></html>"))
        self.chartLegendEdit.setToolTip(_translate("self", "<html><head/><body><p align=\"center\">Enter legend</p></body></html>"))
        self.funcEdit.setToolTip(_translate("self", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Enter your function</span></p></body></html>"))    
        
    def deleteToolTips(self):        
    '''|deleteToolTips(self)
       |private method : deletes tooltips for all widgets'''
        self.colorButton.setToolTip("")
        self.xMinBox.setToolTip("")
        self.xMaxBox.setToolTip("")
        self.chartLegendEdit.setToolTip("")
        self.funcEdit.setToolTip("")
        
    def setTheme(self, flag):        
    '''|setTheme(self, flag)
       |flag : (0, 1, 2) 
       |public method : sets theme for widget
       |setTheme(theme) >>> None '''
        if flag == 0:
            self.setLightTheme()
            self.theme = 0
        elif flag == 1:
            self.setGrayTheme()
            self.theme = 1
        else:
            self.setDarkTheme()
            self.theme = 2        
      
    def results(self):
    '''|results(self)
       |public method : returns all chart's settings for parent widget
       |results() >>> (xMin, xMax, func, legend, fmt, color) '''
        xMin = self.xMinBox.value()
        xMax = self.xMaxBox.value()
        
        legend = self.chartLegendEdit.text()
        
        fmt = self.fmtBox.currentText()[0]
        
        color = self.color
        
        func = self.funcEdit.text()

        return (xMin, xMax, func, legend, fmt, color)   
