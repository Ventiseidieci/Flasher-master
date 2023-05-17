class Model():
     
     def __init__(self):
          self.boardName = None
          self.board = None
          self.sku = None
          self.productionDate = None
          
     def setBoardName(self, name):
          self.boardName = name
     
     def getBoardName(self):
          return self.boardName

     def setSku(self, sku):
          self.sku = sku