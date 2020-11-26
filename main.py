from tkinter import *
from tkinter import ttk

import calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        
        self.calculator = calculator.Calculator(self)
        self.calculator.pack(side=TOP)
        

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()