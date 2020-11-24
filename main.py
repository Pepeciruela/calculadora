from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        
        self.display = calculator.Display(self)
        self.display.pack(side = TOP, fill= BOTH, expand = True)
        
        self.teclado = ttk.Frame(self, width = calculator.WIDTH * 4, height = calculator.HEIGHT * 5)
        self.teclado.grid_propagate(0)
        self.teclado.pack(side = TOP, fill = BOTH, expand = True)
        
        botonC = calculator.CalcButton(self.teclado, "C")
        botonC.grid (row = 0, column = 0)
        
        botonC = calculator.CalcButton(self.teclado, "+/-")
        botonC.grid (row = 0, column = 1)
        
        botonC = calculator.CalcButton(self.teclado, "%")
        botonC.grid (row = 0, column = 2)
        
        botonC = calculator.CalcButton(self.teclado, "÷")
        botonC.grid (row = 0, column = 3)
        
        
        
        """self.calcButtonC = ttk.Frame(self, width = 136, height = 50)
        btn = ttk.Button(self.calcButtonC, text= "C")
        self.calcButtonC.pack_propagate(False)
        btn.pack(side = TOP, fill = BOTH, expand = True)
        self.calcButtonC.grid(column=0, row=1, columnspan=2)
        
        self.calcButtonCs = ttk.Frame(self, width = 68, height = 50)
        btn = ttk.Button(self.calcButtonCs, text= "+/-")
        self.calcButtonCs.pack_propagate(False)
        btn.pack(side = TOP, fill = BOTH, expand = True)
        self.calcButtonCs.grid(column=2, row=1)
        
        self.calcButtondiv = ttk.Frame(self, width = 68, height = 50)
        btn = ttk.Button(self.calcButtondiv, text= "÷")
        self.calcButtondiv.pack_propagate(False)
        btn.pack(side = TOP, fill = BOTH, expand = True)
        self.calcButtondiv.grid(column=3, row=1)"""
        
        
        
        

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
    