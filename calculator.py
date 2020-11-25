from tkinter import *
from tkinter import ttk

WIDTH = 68
HEIGHT = 50

dbotones = [
    {
        'text': 'C',
        'r': 0,
        'c': 1,
    },
    {
        'text': '+/-',
        'r': 0,
        'c': 2,
    },
    {
        'text': '÷',
        'r': 0,
        'c': 3,
    },
    {
        'text': '7',
        'r': 1,
        'c': 0,
    },
    {
        'text': '8',
        'r': 1,
        'c': 1,
    },
    {
        'text': '9',
        'r': 1,
        'c': 2,
    },
    {
        'text': 'x',
        'r': 1,
        'c': 3,
    },
    {
        'text': '4',
        'r': 2,
        'c': 0,
    },
    {
        'text': '5',
        'r': 2,
        'c': 1,
    },
    {
        'text': '6',
        'r': 2,
        'c': 2,
    },
    {
        'text': '-',
        'r': 2,
        'c': 3,
    },
    {
        'text': '1',
        'r': 3,
        'c': 0,
    },
    {
        'text': '2',
        'r': 3,
        'c': 1,
    },
    {
        'text': '3',
        'r': 3,
        'c': 2,
    },
    {
        'text': '+',
        'r': 3,
        'c': 3,
    },
    {
        'text':'0',
        'r':4,
        'c':0,
        'w': 2
    },
    {
        'text': ',',
        'r': 4,
        'c': 2,
    },
    {
        'text': '=',
        'r': 4,
        'c': 3,
    },
]

def retornaCaracter(tecla):
    print('han pulsado', tecla)

class Display(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        self.label = ttk.Label(self, text="0", anchor=E, background='black', foreground='white', font='Helvetica 36')
        self.label.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self, texto):
        self.label.config(text=texto)

class CalcButton(ttk.Frame):
    def __init__(self, parent, text, command=None, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        ttk.Button(self, text=text, command=lambda: command(text) ).pack(side=TOP, fill=BOTH, expand=True)


class Keyboard(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        for boton in dbotones:
            w = boton.get('w', 1)
            h = boton.get('h', 1)

            btn = CalcButton(self, boton['text'],width=w, height=h, command=command)
            btn.grid(row=boton['r'], column=boton['c'], columnspan=w, rowspan=h)


class Calculator(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*6)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        self.display = calculator.Display(self)
        self.display.pack(side=TOP, fill=BOTH, expand=True)

        self.teclado = calculator.Keyboard(self, self.gestiona_calculos)
        self.teclado.pack(side=TOP)

    def gestiona_calculos(self, tecla):
        '''
        Establecer toda la lógica de calculos posible en función de lo tecleado
        variables
            op1
            op2
            operacion
            resultado
        '''
        pass