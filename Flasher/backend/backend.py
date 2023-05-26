from . import csvDbHandler
from . import skuGenerator
from . import serialMACOS
from . import serialLINUX
from . import serialWINDOWS
import sys
from . import csvMaker

class Backend():
   
     def __init__(self):
          
          # scelta del dataStorage
          self.skuGenerator = skuGenerator.skuGenerator(csvDbHandler.csvDbHandler())
          self.csvMaker = csvMaker.CsvMaker()
          
          if sys.platform.startswith('win'):
               self.myserial = serialWINDOWS.serialWINDOWS()
          elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
               # this excludes your current terminal "/dev/tty"
               self.myserial = serialLINUX.serialLINUX()
               # ports = glob.glob('/dev/tty[A-Za-z]*')
          elif sys.platform.startswith('darwin'):
               self.myserial = serialMACOS.serialMACOS()
          else:
               raise EnvironmentError('Unsupported platform')
     
     def getPorts(self):
          return self.myserial.get_serial_port()
     
     def setBoard(self, board):
          self.myserial.setBoard(board)
     
     def getSKU(self):
          pass
     
     def assignSKU(self, sku):
          pass
     
     def flashProgram(self, choice):
          commandList = []
          commandList.append(self.myserial.flashProgramNVS(choice))
          commandList.append(self.myserial.flashProgramBootloader(choice))
          commandList.append(self.myserial.flashProgramPartition(choice))
          commandList.append(self.myserial.flashProgramFirmware(choice))
          
          return commandList
          
     def flashSku(self):
          sku = self.skuGenerator.getSku()
          self.csvMaker.makeNVS(sku)
          self.myserial.flashNVS()
          full = self.skuGenerator.getFullSkuData()
          return sku, full[1]