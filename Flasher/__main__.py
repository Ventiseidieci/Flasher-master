import sys
from PySide6 import QtWidgets
from PySide6 import QtGui
from Flasher.backend.model import Model
from Flasher.controller.controller import Controller
from Flasher.GUI.view import View

# class App(QtWidgets.QApplication):
class App(QtGui.QGuiApplication):
     def __init__(self, sys_argv):
          super(App, self).__init__(sys_argv)
          self.model = Model()
          self.main_controller = Controller(self.model)
          self.main_view = View(self, self.model, self.main_controller)

     def quit(self):
          super().quit()
          
def main():
     
     app = App(sys.argv)
     
     sys.exit(app.exec_())