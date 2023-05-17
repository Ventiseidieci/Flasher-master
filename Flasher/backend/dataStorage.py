import abc

class dataStorage(abc.ABC):
     
     def __init__(self):
          pass
     
     @abc.abstractmethod
     def isAvailable(sku):
          raise NotImplemented