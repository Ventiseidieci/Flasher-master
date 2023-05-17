import string
import random

class skuGenerator():
     
     def __init__(self,  dataStorage, stringSize = 6, charlist = string.ascii_letters + string.digits, unwantedCharacters = 'lIO0QD1ij5SsWw'):
          
          self.stringSize = stringSize
          self.characters = charlist
          self.unwantedCharacters = unwantedCharacters
          self.dataStorage = dataStorage
          
     def getSku(self):
          
          mylist = self.getCharachters()
          mylist = mylist.translate( {ord(i): None for i in self.getUnwantedCharacters()})
          sku = "".join(random.choices(mylist, k = self.getStringSize()))
          print(sku)
          if self.dataStorage.isAvailable(sku) == True:
               self.dataStorage.registerSku(sku)
               return sku
          else:
               self.getSku()
     
     def getStringSize(self):
          return self.stringSize
     
     def getCharachters(self):
          return self.characters
     
     def getUnwantedCharacters(self):
          return self.unwantedCharacters
     
     def setStringSize(self, size):
          self.stringSize = size
     
     def setCharachters(self, chars):
          self.characters = chars
     
