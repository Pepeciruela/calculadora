from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("272x300")
        self.title("Calculadora")
        
        s = ttk.Style()
        s.theme_use("alt")
        #s.configure("my.TLabel", font = "Helvetica 36", background = "black", foreground = "white")
        
        self.display = ttk.Label(self, text = "0", anchor = E, background = "black", foreground = "white", font = "Helvetica 36", padding = (5,0,5,0))
        self.display.pack(side = TOP, fill = BOTH)
        
        self.calcButtonC = ttk.Frame(self, width = 68, height = 50)
        btn = ttk.Button (self.calcButtonC, text= "C")
        self.calcButtonC.pack_propagate(False)
        btn.pack(side = TOP, fill = BOTH, expand = True)
        
        self.calcButtonC.pack(side=TOP)
        
        
        

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
    