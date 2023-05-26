import serial
from . import serialInterface
import glob
import subprocess
import os
import sys

class serialMACOS(serialInterface.serialInterface):
     
     def __init__(self):
          super().__init__()
          
     def get_serial_port(self):
          ports = glob.glob('/dev/tty.*')
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
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               esptoolPath = os.path.join(base_path, 'esp_idf','components','esptool_py', 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
     
     def flashProgramBootloader(self, choice):
          choice = choice
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               esptoolPath = os.path.join(base_path, 'esp_idf','components','esptool_py', 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getBootloader()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getBootloader()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
     
     
     def flashProgramPartition(self, choice):
          choice = choice
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               esptoolPath = os.path.join(base_path, 'esp_idf','components','esptool_py', 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getPartition()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getPartition()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
     
     
     def flashProgramFirmware(self, choice):
          choice = choice
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               esptoolPath = os.path.join(base_path, 'esp_idf','components','esptool_py', 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getFirmware()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getFirmware()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command

     def flashNVS(self):
          base_path = super().getBasePath()
          # idf_path = os.path.join(base_path, 'esp', 'esp-idf')
          #subprocess.run(["/Users/ale2610/esp/esp-idf/components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py", "generate", "configuration/nvsPartition.csv", "configuration/nvsPartition.bin", '0x5000'])
          subprocess.run([ "$IDF_PATH/components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py generate " + base_path + "/Flasher/configuration/nvsPartition.csv " + base_path + "/Flasher/configuration/nvsPartition.bin 0x5000"], shell=True)
          #subprocess.run([ '' + idf_path + "/components/nvs_flash/nvs_partition_generator/nvs_partition_gen.py generate", base_path + '/Flasher/configuration/nvsPartition.csv', base_path + '/Flasher/configuration/nvsPartition.bin 0x5000'], shell=True)