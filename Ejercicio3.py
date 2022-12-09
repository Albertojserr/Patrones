from zope.interface import Interface
from zope.interface import implementer
import time
import random

class ISensor(Interface):

    def comprobar(self):
        """Devuelve el valor de peligro"""
    def setValor(self):
        """Establece un nuevo valor de peligro"""

@implementer(ISensor)
class Sensor(object):
    def __init__(self, nombre):
        self.nombre=nombre
        self.umbral=0
        self._valor=0
    def comprobar(self):
        self.diferencia=self._valor/self.umbral
        return self.diferencia
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self,valor :int):
        self._valor=valor

class SensorHumo(Sensor):
    def __init__(self):
        Sensor.__init__(self,"Sensor humo")
        self.umbral=20

class SensorTemperatura(Sensor):
    def __init__(self):
        Sensor.__init__(self,"Sensor temperatura")
        self.umbral=47

class SensorPresion(Sensor):
    def __init__(self):
        Sensor.__init__(self,"Sensor presion")
        self.umbral=40

class Alarma(object):
    def __init__(self):
        self.sensores=[]
    def addSensor(self,sensor):
        self.sensores.append(sensor)
    def comprobar(self):
        peligro=0
        for sensor in self.sensores:
            peligro+=float(sensor.comprobar())
        if float(peligro/len(self.sensores))>1:
            print("ALARMA!!!")
        else:
            print("Todo OK")

if __name__=="__main__":
    Humo=SensorHumo()
    Temperatura=SensorTemperatura()
    Presion=SensorPresion()
    alarma=Alarma()
    alarma.addSensor(Humo)
    alarma.addSensor(Temperatura)
    alarma.addSensor(Presion)
    seguir='si'
    while seguir=='si':
        for i in range(random.randint(1,10)):
            for sensor in alarma.sensores:
                max=int(sensor.umbral*1.2)
                min=int(sensor.umbral*0.8)
                sensor.valor=random.randint(min,max)
            alarma.comprobar()
            time.sleep(2)
        seguir=input("Desea seguir? Si/No ").lower()
