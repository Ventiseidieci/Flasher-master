import csv
import sys
import os

class CsvMaker():
     
     def __init__(self):
          self.header = ['key', 'type', 'encoding', 'value']
          self.namespace = ['tech', 'namespace', '','']
          
          pass
     
     def makeNVS(self, sku):
          if getattr(sys, 'frozen', False):
              # we are running in a |PyInstaller| bundle
              base_path = sys._MEIPASS  #type: ignore
              extDataDir = os.getcwd() #get current working directory

          else:
              # we are running in a normal Python environment
              base_path = os.getcwd()
          csvPath = os.path.join(base_path, 'Flasher', 'configuration', 'nvsPartition.csv')
          with open(csvPath, 'w', newline='') as csvfile:
               writer = csv.writer(csvfile)
               writer.writerow(self.header)
               writer.writerow(self.namespace)
               word = str(sku)
               writer.writerow(['SKU', 'data', 'string', word])