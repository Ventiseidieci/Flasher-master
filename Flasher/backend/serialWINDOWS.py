import serial
from . import serialInterface
import os
import esptool
import subprocess
class serialWINDOWS(serialInterface.serialInterface):
     
     def __init__(self):
          super().__init__()
          
          
     def get_serial_port(self):
          ports = ['COM%s' % (i + 1) for i in range(256)]
          results = []
          for port in ports:
               try:
                    s = serial.Serial(port)
                    s.close()
                    results.append(port)
               except (OSError, serial.SerialException):
                    pass
          return results
     
     def setBoard(self, board):
          super().setBoard(board)
          
     def getBoard(self):
          return super().getBoard()
     
     def closeBoard(self, board):
          return super().closeBoard(board)
     
     def flashProgramNVS(self, choice):
          choice = choice
          command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
     
     def flashProgramBootloader(self, choice):
          choice = choice
          command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "keep", "--flash_size", "8MB", "--flash_freq", "40m", "0x1000", super().getBootloader()]
          return command
     
     
     def flashProgramPartition(self, choice):
          choice = choice
          command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x8000", super().getPartition()]
          return command
     
     
     def flashProgramFirmware(self, choice):
          choice = choice
          command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "hard_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x10000", super().getFirmware()]
          return command
          
     def flashNVS(self):
          base_path = super().getBasePath()
          path = os.path.join( '%IDF_TOOLS_PATH%', 'frameworks', 'esp-idf-v5.0.1', 'components', 'nvs_flash', 'nvs_partition_generator', 'nvs_partition_gen.py' )
          os.system("python " + path + " generate " + base_path + r"\Flasher\configuration\nvsPartition.csv " + base_path + r"\Flasher\configuration\nvsPartition.bin " + '0x5000')