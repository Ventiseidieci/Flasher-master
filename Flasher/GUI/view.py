import sys
from PySide6.QtCore import QObject, Slot, Property, Signal, QProcess
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
          self._commandRunner.runCommands(commands)
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
    
     outputChanged = Signal(str)
     outputs = []
     @Slot(str)
     def runCommands(self, commands):

          process = QProcess()
          process.setProcessChannelMode(QProcess.MergedChannels) # type: ignore
          process.readyReadStandardOutput.connect(self.readOutput)
          
          for commandList in commands:
               command = ' '.join(commandList)
               # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=None, universal_newlines=True, bufsize=1)
               # output, _ = process.communicate()
               process.start(command)
               process.waitForFinished(-1)
               # self.outputs.append(output)
               # print(output)
               # sys.stdout.flush()
               # self.outputChanged.emit(str("cazzo"))
               
          # self.outputChanged.emit('\n'.join(self.outputs))
     def readOutput(self):
          output = self.sender().readAllStandardOutput().data().decode() # type: ignore
          # self.outputChanged.emit(output)
          print(output)
class View(QObject):
     
     def __init__(self, app, model, controller):
          super().__init__()
          self._model = model
          self._controller = controller
          
          engine = QQmlApplicationEngine()
          engine.quit.connect(app.quit)
          engine.load('Flasher/GUI/mainUI.qml')
          devices = self._controller.getBoardList()
          engine.rootContext().setContextProperty("devices", devices) # Nel contest (file qml) va a trovare una variabile che si chiama values e associa il valore della variabile devices
          
          combo_box_handler = ComboBoxHandler(self._controller)
          engine.rootContext().setContextProperty("comboBoxHandler", combo_box_handler)
          
          commandRunner = CommandRunner()
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