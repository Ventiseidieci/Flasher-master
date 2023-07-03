
import serial
import os
import sys
class serialInterface():
     
     def __init__(self):
          self.board = None
          if getattr(sys, 'frozen', False):
              # we are running in a |PyInstaller| bundle
              self.base_path = sys._MEIPASS  #type: ignore
              extDataDir = os.getcwd() #get current working directory

          else:
              # we are running in a normal Python environment
              self.base_path = os.getcwd()
          self.nvsPath = os.path.join(self.base_path, 'Flasher', 'configuration', 'nvsPartition.bin')
          self.bootloaderPath = os.path.join(self.base_path, 'Flasher', 'configuration', 'bootloader.bin')
          self.partitionPath = os.path.join(self.base_path, 'Flasher', 'configuration', 'partition-table.bin')
          self.firmwarePath = os.path.join(self.base_path, 'Flasher', 'configuration', 'sketch_nov21_OTA_EEPROM_read.ino.bin')
     
     def get_serial_ports(self):
          pass

     def setBoard(self, board):
          if self.board == None:
               self.board = serial.Serial(board, 115200, timeout=5)
          else:
               self.board.close()
               self.board = serial.Serial(board, 115200, timeout=5)
               self.board.close()
               
     def getBoard(self):
          return self.board
     
     def closeBoard(self, board):
          board.close()
     
     def flashProgram(self, container):
          pass
     
     def flashNVS(self):
          pass
     
     def getNvs(self):
          return self.nvsPath
     
     def getBootloader(self):
          return self.bootloaderPath
     
     def getPartition(self):
          return self.partitionPath
     
     def getFirmware(self):
          return self.firmwarePath
     
     def getBasePath(self):
          return self.base_path