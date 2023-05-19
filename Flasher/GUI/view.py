from PySide6.QtCore import QObject
from PySide6.QtQml import QQmlApplicationEngine
class View(QObject):
     
     def __init__(self, app, model, controller):
          super().__init__()
          self.model = model
          self.controller = controller
          
          engine = QQmlApplicationEngine()
          engine.quit.connect(app.quit)
          engine.load('Flasher/GUI/mainUI.qml')
          devices = self.controller.getBoardList()
          engine.rootContext().setContextProperty("devices", devices) # Nel contest (file qml) va a trovare una variabile che si chiama values e associa il valore della variabile devices
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