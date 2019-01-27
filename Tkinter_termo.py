from tkinter import *
from tkinter import ttk

class mainApp (Tk):


    def __init__(self):
        Tk.__init__(self)
        self.title('Termometro')
        self.geometry('210x150')
        self.configure(bg='#ECECEC')
        self.resizable(0,0)
        self.__temperaturaAnt=StringVar(value='')
        self.temperatura=StringVar()
        self.temperatura.trace('w',self.validateTemperature)
        self.tipoUnidad=StringVar()
        
        self.createLayout()
    
    def createLayout(self):
        self.entrada=ttk.Entry(self, textvariable=self.temperatura,width=25)
        self.entrada.place(x=20,y=25)
        self.LabelUni=ttk.Label(self,text='Grados')
        self.LabelUni.place(x=20,y=55)
        
        self.rb1=ttk.Radiobutton(self, text='Farenheit',variable=self.tipoUnidad,value='F', command=self.selected).place(x=50,y=85)
        self.rb2=ttk.Radiobutton(self, text='Celsius',variable=self.tipoUnidad,value='C', command=self.selected).place(x=50,y=105)
    
    def start (self):
        self.mainloop()
    
    def validateTemperature(self, *args):
        nuevoValor= self.temperatura.get()
        print('nuevoValor', nuevoValor, 'vs valorAnterior', self.__temperaturaAnt)
        try:
            float(nuevoValor)
            self.__temperaturaAnt=nuevoValor
            print("fija valor anterior a", self.__temperaturaAnt)
        except:
            self.temperatura.set(self.__temperaturaAnt)
            print("recupera valor anterior", self.__temperaturaAnt)

    def selected(self):
        resultado=0
        toUnidad=self.tipoUnidad.get()
        grados=float(self.temperatura.get())
        
        if toUnidad=='F':
            resutado=grados*9/5+32
        elif toUnidad=='C':
            resulltado=(grados - 32)*5/9
        else:
            resultado=grados
        
        self.temepratura.set(resultado)
        
        
        
        
if __name__=='__main__':
    app= mainApp()
    app.start()
            