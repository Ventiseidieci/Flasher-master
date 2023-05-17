import customtkinter
from ..GUI import firstBlockFrame
import os
class View():
     
     def __init__(self, master, controller):
          self.controller = controller
          #self.frame = customtkinter.CTkFrame(master)
          #self.frame.grid()
          self.viewPanel = ViewPanel(master, controller)
     
     def getViewPanel(self):
          return self.viewPanel
          

class ViewPanel():
     
     def __init__(self, root, controller):
          self.controller = controller
          
          root.grid_rowconfigure(3, weight=1)
          root.grid_columnconfigure(2, weight=1)
          
          self.framePanel = customtkinter.CTkFrame(root) # dichiara il frame panel
          self.first_flash = firstBlockFrame.Flash_Board(self.framePanel, self.controller) # set del frame panel
          self.framePanel.grid(column=0,row=0, columnspan = 3) # posiziona il frame panel
          # self.terminalFrame = customtkinter.CTkFrame(root)
          # wid = self.terminalFrame.winfo_id()
          # os.system('xterm -into %d -geometry 400x100 -sb &' % wid)
          # self.framePanel.grid(column=0, row=1, columnspan = 3)
          
     def updateLabel(self, data):
          label = self.first_flash.getLabel()
          label.configure(text = data)