import serial
from . import serialInterface
import os
import sys
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
          if getattr(sys, 'frozen', False):
               
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               # esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'dist', 'esptool.exe')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
               # command = ["python", esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               command = ["python",esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
     
     def flashProgramBootloader(self, choice):
          choice = choice
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'dist', 'esptool.exe')
               # esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x1000", super().getBootloader()]
               # command = ["python", esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getBootloader()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               command = ["python",esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x1000", super().getBootloader()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
     
     
     def flashProgramPartition(self, choice):
          choice = choice
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'dist', 'esptool.exe')
               # esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x8000", super().getPartition()]
               # command = ["python",esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getPartition()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               command = ["python",esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x8000", super().getPartition()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
     
     
     def flashProgramFirmware(self, choice):
          choice = choice
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               extDataDir = os.getcwd() #get current working directory
               # esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'dist', 'esptool.exe')
               command = [esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x10000", super().getFirmware()]
               # command = ["python", esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getFirmware()]
          else:
               # we are running in a normal Python environment
               base_path = os.getcwd()
               esptoolPath = os.path.join(base_path, 'esp_idf_win','components','esptool_py', 'esptool', 'esptool.py')
               command = ["python", esptoolPath, "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x10000", super().getFirmware()]
          # command = ['esptool.py', "-p", choice , "-b", "460800", "--before", "default_reset", "--after", "no_reset", "--chip", "esp32", "write_flash", "--flash_mode", "dio", "--flash_size", "8MB", "--flash_freq", "40m", "0x9000", super().getNvs()]
          return command
          
     def flashNVS(self):
          if getattr(sys, 'frozen', False):
               # we are running in a |PyInstaller| bundle
               base_path = sys._MEIPASS  #type: ignore
               # command = 'python '+ base_path + r'\esp_idf_win\components\nvs_flash\nvs_partition_generator\nvs_partition_gen.py generate ' + base_path + '\\Flasher\\configuration\\nvsPartition.csv ' + base_path + '\\Flasher\\configuration\\nvsPartition.bin 0x5000'
               command =  base_path + r'\esp_idf_win\components\nvs_flash\nvs_partition_generator\dist\nvs_gen.exe generate ' + base_path + '\\Flasher\\configuration\\nvsPartition.csv ' + base_path + '\\Flasher\\configuration\\nvsPartition.bin 0x5000'
               # print(command)
               # subprocess.run(['py', base_path + r'\esp_idf_win\components\nvs_flash\nvs_partition_generator\nvs_partition_gen.py generate ' + base_path + '\\Flasher\\configuration\\nvsPartition.csv ' + base_path + '\\Flasher\\configuration\\nvsPartition.bin 0x5000'], shell=True)
               subprocess.run(command, shell=True)
               # subprocess.run(['python ', base_path + r'\esp_idf_win\components\nvs_flash\nvs_partition_generator\nvs_partition_gen.py generate'  + base_path + '\\Flasher\\configuration\\nvsPartition.csv ' + base_path + '\\Flasher\\configuration\\nvsPartition.bin 0x5000'], shell=True)
          else:
               base_path = super().getBasePath()
               # command = 'python '+ base_path + r'\esp_idf_win\components\nvs_flash\nvs_partition_generator\nvs_partition_gen.py generate ' + base_path + '\\Flasher\\configuration\\nvsPartition.csv ' + base_path + '\\Flasher\\configuration\\nvsPartition.bin 0x5000'
               command = base_path + r'\esp_idf_win\components\nvs_flash\nvs_partition_generator\dist\nvs_gen.exe generate ' + base_path + '\\Flasher\\configuration\\nvsPartition.csv ' + base_path + '\\Flasher\\configuration\\nvsPartition.bin 0x5000'
               # print(command)
               # subprocess.run(['py', base_path + r'\esp_idf_win\components\nvs_flash\nvs_partition_generator\nvs_partition_gen.py generate ' + base_path + '\\Flasher\\configuration\\nvsPartition.csv ' + base_path + '\\Flasher\\configuration\\nvsPartition.bin 0x5000'], shell=True)
               subprocess.run(command, shell=True)