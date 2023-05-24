from PySide6 import QtCore, QtWidgets, QtGui


class Controller(QtCore.QObject):
     
     def __init__(self, model):
          super().__init__()
          self.model = model
          self.myBackend = self.model.getBackend()

     def flash(self, choice):

          sku, data = self.myBackend.flashSku()
          self.model.setSku(sku)
          self.model.setData(data)
          
          return self.myBackend.flashProgram(choice)
     
     def getBoardList(self):
          return self.myBackend.getPorts()

     def setBoard(self, board):
          self.model.setBoardName(board)
          self.myBackend.setBoard(board)
