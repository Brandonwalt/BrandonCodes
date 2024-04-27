# Org from https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# adapted by Phil J - for Simple Gui creation example (Video)
# Minimal python code to start PyQt5 GUI
# Requires python 2.7
# THIS IS INCOMPLETE . . . .

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *


# This is our window from QtCreator
import mainwindow

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
     # access variables inside of the UI's file

     def pressedOnButton(self):
         print "Pressed On !"

     def changeValue(self):
        print(self.sldPwm.value())
     
     def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

            ### hooks for buttons
        self.btnPress.clicked.connect(lambda: self.pressedOnButton())
        self.sldPwm.valueChanged[int].connect(lambda: self.changeValue())

def main():
     app = QApplication(sys.argv)
     form = MainWindow()
     form.show()
     sys.exit(app.exec_())


# python bit to figure how to started this
if __name__ == "__main__":
 main()
