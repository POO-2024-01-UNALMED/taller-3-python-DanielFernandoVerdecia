class TV:

    
    numTV = 0

    def __init__(self, marca, estado = False , canal = 1, precio = 500, volumen = 1, control = None):

        self._marca = marca
        self._canal = canal
        self._precio = precio
        self._estado = estado
        self._volumen = volumen
        self._control = control
        TV.numTV += 1
        
    
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca


    def getCanal(self):
        return self._canal
    
    def setCanal(self, canal):

        if (canal >= 1 and canal <= 120) and self._estado:
            self._canal = canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, precio):
        self._precio = precio


    def getVolumen(self):
        
        return self._volumen
    
    def setVolumen(self, volumen):

        if (volumen >=0 and volumen <= 7) and self._estado:
        
            self._volumen = volumen

    def getControl(self):
        return self._control
        
    def setControl(self, control):
        self._control = control

    def turnOn(self):
        self._estado = True


    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    
    def canalUp(self):

        if (self._estado) and (self._canal < 120):
            self._canal += 1

    def canalDown(self):

        if (self._estado) and (self._canal > 1):
           
            self._canal -= 1

    def volumenUp(self):

        if (self._estado) and (self._volumen < 7):
            self._volumen += 1

    def volumenDown(self):
        if (self._estado) and (self._volumen >= 1):
            self._volumen -= 1

    @classmethod
    def getNumTV(self):
        return TV.numTV
    
    @classmethod
    def setNumTV(self, value):
        TV.numTV = value
    
    


