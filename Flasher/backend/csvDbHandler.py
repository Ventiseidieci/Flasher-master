from . import dataStorage
import csv
from datetime import datetime
import os
import sys
class csvDbHandler(dataStorage.dataStorage):
     
     def __init__(self):
          super().__init__()
          self.dictionary = {}
          if getattr(sys, 'frozen', False):
              # we are running in a |PyInstaller| bundle
              base_path = sys._MEIPASS  #type: ignore
              extDataDir = os.getcwd() #get current working directory

          else:
              # we are running in a normal Python environment
              base_path = os.getcwd()
          
          self.csvPath = os.path.join(base_path, 'Flasher', 'configuration', 'skuList.csv')
          with open( self.csvPath, newline='') as csvfile:
               spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
               for row in spamreader:
                    self.dictionary.update({row[0] : row[1]})
               #print(self.dictionary)
          
     def isAvailable(self, sku):
          if ( sku not in self.dictionary):
               return True

     def registerSku(self, sku): #E' un append sul csv 'a'
          
          row = [str(sku) , str(datetime.today())]
          with open(self.csvPath, 'a',newline='') as csvfile:
               writer = csv.writer(csvfile)
               writer.writerow(row)