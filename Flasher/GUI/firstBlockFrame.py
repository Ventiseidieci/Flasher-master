# import customtkinter
# from ..backend import *

# class Flash_Board(customtkinter.CTkFrame):
     
#      def __init__(self, root, controller, *args, header_name="firstBlockFrame", **kwargs):
#           super().__init__(root,*args, **kwargs)
#           self.controller = controller
#           self.header_name = header_name
          
#           root.columnconfigure(1, weight=1)
#           root.rowconfigure(3, weight=1)
          
#           self.label = customtkinter.CTkLabel(root, text="Seleziona la Board per la programamzione", height=20)
#           self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
          
#           self.combobox = customtkinter.CTkOptionMenu(root,
#                                                  values=self.controller.getBoardList(),
#                                                  command= self.controller.setBoard)
#           self.combobox.grid(row=1, column=0, padx=10, pady=10)
#           self.combobox.set("Seleziona una board")  # set initial value
#           #self.combobox.bind("<Button-1>", lambda event, arg=self.combobox: self.controller.updateList(event, arg))
          
#           #create Flash button
#           self.flash_button = customtkinter.CTkButton(root, text="Flash")
#           #posizionamento bottone Flash
#           self.flash_button.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
#           self.flash_button.bind("<Button-1>", lambda event, arg= self.combobox: self.controller.flash(event, arg))
          
#           #self.label = customtkinter.CTkLabel(root)
#           #self.label.grid(row=2, column = 0, padx=10, columnspan = 2)
     

#      def getLabel(self):
#           return self.label


