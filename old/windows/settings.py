import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from ads import disableFirstRun, load_settings_values, write_settings_values, automation

class Settings(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Daily Screener")
        self.setWindowIcon(QIcon("gui/daily_screener.ico"))

        loadUi("gui/settings.ui", self)
        self.pushButton.clicked.connect(self.run_once) #run once button - QTLineEdito5
        self.pushButton_2.clicked.connect(self.save) #save
        #self.checkBox.clicked.connect(self.run_daily)
        #self.checkBox_2.clicked.connect(self.headless)

        loadedSettings = load_settings_values()
        firstRun = loadedSettings[5]

        if (firstRun):
            self.checkBox.setChecked(True)
            self.checkBox_2.setChecked(True)
            disableFirstRun()
        else:            
            self.lineEdit.setText(loadedSettings[0])
            self.lineEdit_2.setText(loadedSettings[1])
            self.lineEdit_3.setText(loadedSettings[2])
            self.checkBox.setChecked(loadedSettings[3])
            self.checkBox_2.setChecked(loadedSettings[4])
  
    def save(self):
        netID = self.lineEdit.text()
        password = self.lineEdit_2.text()
        deviceURL = self.lineEdit_3.text();
        
        if (netID == "" or password == "" or deviceURL == ""):
            print("You must fill out all the information")
            return False

        runDaily = self.checkBox.isChecked()
        headless = self.checkBox_2.isChecked()

        write_settings_values(netID, password, deviceURL, runDaily, headless)
        print("saved")

    def run_once(self):
        netID = self.lineEdit.text()
        password = self.lineEdit_2.text()
        deviceURL = self.lineEdit_3.text()

        if (netID == "" or password == "" or deviceURL == ""):
            print("You must fill out all the information")
            return False

        self.save()
        print("Automatically saved the current credentials")
        print("Starting running process...")
        automation()

    def run_daily(self):
        #TODO: Implement daily running
        print("run daily")
        
app = QApplication(sys.argv)
mainWindow = Settings()
mainWindow.show()
app.exec()