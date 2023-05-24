import sys
from PySide6.QtCore import QObject, Slot, Property, Signal, QProcess
from PySide6.QtQuick import QQuickItem, QQuickWindow
from PySide6.QtQml import QQmlApplicationEngine
import subprocess
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
          
          engine = QQmlApplicationEngine()
          engine.quit.connect(app.quit)
          engine.load('Flasher/GUI/mainUI.qml')
          devices = self._controller.getBoardList()
          engine.rootContext().setContextProperty("devices", devices) # Nel contest (file qml) va a trovare una variabile che si chiama values e associa il valore della variabile devices
          
          application_window = engine.rootObjects()[0]

          self.rectangle = application_window.findChild(QQuickItem, "rectangle") #type: ignore
          figli = self.rectangle.children() #type: ignore
          
          for figlio in figli:
               print(figlio.objectName())
          self.text_area = self.rectangle.findChild(QQuickItem, "outputTextArea") #type: ignore
          
          
          combo_box_handler = ComboBoxHandler(self._controller)
          engine.rootContext().setContextProperty("comboBoxHandler", combo_box_handler)
          
          commandRunner = CommandRunner(self.text_area)
          engine.rootContext().setProperty("commandRunner", commandRunner)
          
          flashButtonHandler = FlashButton(self._controller, self._model, commandRunner)
          engine.rootContext().setContextProperty("flashButtonHandler", flashButtonHandler)
          
          
          app.exec()

     
     # def getViewPanel(self):
     #      return self.viewPanel
          

# class ViewPanel():
     
#      def __init__(self, root, controller):
#           self.controller = controller
          
#           root.grid_rowconfigure(3, weight=1)
#           root.grid_columnconfigure(2, weight=1)
          
#           self.framePanel = customtkinter.CTkFrame(root) # dichiara il frame panel
#           self.first_flash = firstBlockFrame.Flash_Board(self.framePanel, self.controller) # set del frame panel
#           self.framePanel.grid(column=0,row=0, columnspan = 3) # posiziona il frame panel
#           # self.terminalFrame = customtkinter.CTkFrame(root)
#           # wid = self.terminalFrame.winfo_id()
#           # os.system('xterm -into %d -geometry 400x100 -sb &' % wid)
#           # self.framePanel.grid(column=0, row=1, columnspan = 3)
          
#      def updateLabel(self, data):
#           label = self.first_flash.getLabel()
#           label.configure(text = data)