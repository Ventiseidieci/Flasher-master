import sys
import glob
import serial
import subprocess
from backend import *
from abc import ABC, abstractclassmethod

class serialCreatorFactoryMethod(ABC): # TODO in realtà serve factory method pattern

    def __init__(self):
        self.board = None

    def getSerial(self):
        return self.factory_method()

    @abstractclassmethod
    def factory_method():
        pass
    
    def setBoard(self, board):
        pass
    
    def getBoard(self):
        return self.board
