import sys
from PySide6.QtCore import QObject, Slot, Property, Signal, QProcess
from PySide6.QtQuick import QQuickItem, QQuickWindow
from PySide6.QtQml import QQmlApplicationEngine
import os
class FlashButton(QObject):
     
     def __init__(self, controller, model, commandRunner):
          super().__init__()
          self._controller = controller
          self._model = model
          self._commandRunner = commandRunner
          
     @Slot()
     def handleButtonClicked(self):
          commands = self._controller.flash(self._model.getBoardName())
          self._commandRunner.setCommands(commands)
class ComboBoxHandler(QObject):
     
     selectedItemChanged = Signal()
     
     def __init__(self, controller):
          super().__init__()
          self._selectedItem = ""
          self._controller = controller
          
     @Property(str, notify=selectedItemChanged) # type: ignore
     def selectedItem(self): # type: ignore
          return self._selectedItem
     
     @selectedItem.setter
     def selectedItem(self, value):
          if self._selectedItem != value:
               self._selectedItem = value
               self.selectedItemChanged.emit()
               self._controller.setBoard(self._selectedItem)
               print("Device seleizonato", self._selectedItem)
               
class CommandRunner(QObject):
     
     def __init__(self, textArea):
          
          self.outputChanged = Signal(str)
          self.outputs = []
          self.output = 0
          self.textArea = textArea
          self.process = QProcess()
          self.process.readyReadStandardOutput.connect(self.readOutput)
          self.process.setProcessChannelMode(self.process.ProcessChannelMode(0x1)) # type: ignore
          self.process.finished.connect(self.handleFinished)
          self.commands = []
          self.currentIndex = 0
          
     @Slot(str)
     def setCommands(self, commands):
          
          for commandList in commands:
               command = ' '.join(commandList)
               self.commands.append(command)

          self.startNextCommand()
               
               
     def startNextCommand(self):
          if self.currentIndex < len(self.commands):
               command = self.commands[self.currentIndex]
               if sys.platform.startswith('win'):
                    self.process.start("cmd.exe", ["-c", command])
               else:
                    self.process.start("bash", ["-c", command])
               self.currentIndex += 1

     def readOutput(self):
          self.output = self.process.readAllStandardOutput().data().decode().strip()
          self.textArea.append(self.output)

     
     def handleFinished(self):
          #  SU RASPBERRY FARE UN SEGNALE DI OUTPUT
          self.textArea.append("processo terminato. ")
          self.startNextCommand()
class View(QObject):
     
     def __init__(self, app, model, controller):
          super().__init__()
          self._model = model
          self._controller = controller
          self.text_area = None
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory

          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
          
          qmlPath = os.path.join(base_path, 'Flasher', 'GUI', 'mainUI.qml')
          engine = QQmlApplicationEngine()
          engine.quit.connect(app.quit)
          engine.load(qmlPath)
          devices = self._controller.getBoardList()
          engine.rootContext().setContextProperty("devices", devices) # Nel contest (file qml) va a trovare una variabile che si chiama values e associa il valore della variabile devices
          
          application_window = engine.rootObjects()[0]

          self.rectangle = application_window.findChild(QQuickItem, "rectangle") #type: ignore
          # figli = self.rectangle.children() #type: ignore
          
          # for figlio in figli:
          #      print(figlio.objectName())
          self.text_area = self.rectangle.findChild(QQuickItem, "outputTextArea") #type: ignore
          
          
          combo_box_handler = ComboBoxHandler(self._controller)
          engine.rootContext().setContextProperty("comboBoxHandler", combo_box_handler)
          
          commandRunner = CommandRunner(self.text_area)
          engine.rootContext().setProperty("commandRunner", commandRunner)
          
          flashButtonHandler = FlashButton(self._controller, self._model, commandRunner)
          engine.rootContext().setContextProperty("flashButtonHandler", flashButtonHandler)
          
          
          app.exec()
