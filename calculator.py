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
        'text': '.',
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

        self.label = ttk.Label(self, text="0", anchor=E, background='black', foreground='white', font='Helvetica 36')
        self.label.pack(side=TOP, fill=BOTH, expand=True)

    def refresh(self, texto):
        self.label.config(text=texto)

class CalcButton(ttk.Frame):
    def __init__(self, parent, text, command=None, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=WIDTH*width, height=HEIGHT*height)
        self.pack_propagate(0)
        self.value = text
        self.command = command

        ttk.Button(self, text=text, command=self.send).pack(side=TOP, fill=BOTH, expand=True)

        #ttk.Button(self, text=text, command=lambda : command(text)).pack(side=TOP, fill=BOTH, expand=True)

    def send(self):
        self.command(self.value)


class Keyboard(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*5)
        self.pack_propagate(0)

        for boton in dbotones:
            w = boton.get('w', 1)
            h = boton.get('h', 1)

            btn = CalcButton(self, boton['text'],width=w, height=h, command=command)
            btn.grid(row=boton['r'], column=boton['c'], columnspan=w, rowspan=h)


class Calculator(ttk.Frame):
    valor1 = None
    valor2 = None
    r = None
    operador = ""
    cadena = ""

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=WIDTH*4, height=HEIGHT*6)
        self.pack_propagate(0)
        s = ttk.Style()
        s.theme_use('alt')

        self.display = Display(self)
        self.display.pack(side=TOP, fill=BOTH, expand=True)

        self.teclado = Keyboard(self, self.gestiona_calculos)
        self.teclado.pack(side=TOP)

    def gestiona_calculos(self, tecla):
        print(tecla)

        if tecla.isdigit() != 0: # si la tecla es diferente a 0
            if len(self.cadena) > 9:#si la longitud del número es mayor que 9, no dejes seguir añadiendo números
                return
            if not (self.cadena == "" and tecla == "0"): # si cadena no está vacía y tecla no he pulsado 0
                self.cadena += tecla # cadena coge el valor de la tecla pulsada
                self.display.refresh(self.cadena) # refrescamos el display con el nuevo valor de la cadena
        elif tecla in ("+-x÷"): # si la tecla es un simbolo de operación
            if self.valor1 == None and not self.cadena: #si el valor1 esta vacio y la cadena está vacia
                return #volver (evita el casque de meter simbolos de inicio sin información)
            if self.valor1 == None: # si el valor1 está vacio
                self.valor1 = float(self.cadena) # el valor1 pasa a ser el valor de la cadena
                self.cadena = "" #se vacia la cadena
                self.operador = tecla # el operador coge el simbolo de la tecla pulsada
            elif self.valor1 != None and not self.cadena:
                self.operador = tecla # el operador coge el simbolo de la tecla pulsada
            else:
                if not self.cadena: #si no hay cadena vuelve
                    return
                self.valor2 = float(self.cadena) #si hay cadena el valor2 pasa a ser el valor de la cadena
                self.r = self.calculate() #el resultado ejecuta la función calculate en función de su simbolo
                self.display.refresh(self.r) #refrescamos el display con el resultado de la operación
                self.valor1 = self.r #el valor1 pasa a ser el valor del resultado
                self.operador = tecla # el operador coge el simbolo de la tecla pulsada
                self.cadena = "" #se vacia la cadena
        elif tecla == '=': #si la tecla pulsada es =
            self.valor2 = float(self.cadena) #si hay cadena el valor2 pasa a ser el valor de la cadena
            self.r = self.calculate() #el resultado ejecuta la función calculate en función de su simbolo
            self.display.refresh(self.r) #refrescamos el display con el resultado de la operación
            self.valor1 = self.r #el valor1 pasa a ser el valor del resultado
            self.cadena = "" #se vacia la cadena
            self.operador = "" #se reinicia el operador
        elif tecla == "C": #si la tecla pulsada es borrar
            self.valor1 = None #reiniciamos valor1
            self.valor2 = None #reiniciamos valor2
            self.r = None #reiniciamos resultado
            self.operador = "" #reiniciamos operador
            self.cadena = "" #reiniciamos cadena
            self.display.refresh("0") #refrescamos el display a 0
        elif tecla == "." and "." not in self.cadena: #si la tecla es , y no está dentro de la cadena ya
            self.cadena += tecla # añadir , a la cadena
            self.display.refresh(self.cadena) # refrescamos el display con el nuevo valor de la cadena
        elif tecla == "+/-":
            
            

    def calculate(self):
        
        if self.operador == '+':
            return self.valor1 + self.valor2
        elif self.operador == '-':
            return self.valor1 - self.valor2
        elif self.operador == 'x':
            return self.valor1 * self.valor2
        else:
            return self.valor1 / self.valor2
