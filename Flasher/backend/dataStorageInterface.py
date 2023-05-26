import abc

class dataStorageInterface(abc.ABC):
     
     def __init__(self):
          pass
     
     @abc.abstractmethod
     def isAvailable(sku):
          raise NotImplemented
     
     @abc.abstractmethod
     def getRow(self):
          raise NotImplemented