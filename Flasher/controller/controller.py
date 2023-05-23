from PySide6 import QtCore, QtWidgets, QtGui


class Controller(QtCore.QObject):
     
     def __init__(self, model):
          super().__init__()
          self.model = model
          self.myBackend = self.model.getBackend()
          
#           self.root = customtkinter.CTk()
#           if getattr(sys, 'frozen', False):
#               # we are running in a |PyInstaller| bundle
#               base_path = sys._MEIPASS  #type: ignore
#               extDataDir = os.getcwd() #get current working directory

#           else:
#               # we are running in a normal Python environment
#               base_path = os.getcwd()
#           pathJson = os.path.join(base_path, 'Flasher', 'custom_color.json')
          
#           customtkinter.set_default_color_theme(pathJson)
          
#           self.model = model.Model()
#           self.myBackend = backend.Backend()
                    
#           self.view = view.View(self.root, self)
     

          
#           self.root.geometry("400x200")
#           self.root.title("Vbite Flasher")
#           self.root.minsize(400,200)
          
# #          self.thread = self._createThread()
#           self.q = queue.Queue()
          
#           while True:
               
#                self.root.update_idletasks()
#                self.root.update()
#                self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
#                if self.q.empty():
#                     pass
#                else:
#                     self.view.getViewPanel().updateLabel(self.q.get())
#                     #self.q.task_done()
     
#     def _createThread(self):
#          return threading.Thread(target=self.startSerialRead)

     # def on_closing(self):
     #      self.root.destroy()

     
     def flash(self, choice):

          sku = self.myBackend.flashSku()
          self.model.setSku(sku)
          
          return self.myBackend.flashProgram(choice)
     
     def getBoardList(self):
          return self.myBackend.getPorts()
          
     # def updateList(self, event, container):
     #      #container.configure(values=serialRead.mySerial.get_serial_ports())
     #      container.configure(values=self.myBackend.getPorts())
     
     # def printRoba(self, event, choice):
     #      print("optionmenu dropdown clicked:", event, " ", choice)
          
     def setBoard(self, board):
          self.model.setBoardName(board)
          self.myBackend.setBoard(board)
     #      #print("hai scelto questa board:", board)
     #      #if not self.thread.is_alive():
     #      #      self.thread = self._createThread()
     #      #      self.thread.start()
          
     # def getBoard(self):
     #      return self.model.getBoardName()
     
#     def startSerialRead(self):
#          while True and self.myserial.getBoard().isOpen():
#               self.myserial.printLine(self)
