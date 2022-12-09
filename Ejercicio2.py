from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observador):
        pass

    @abstractmethod
    def detach(self, observer: Observador):
        pass

    @abstractmethod
    def notify(self):
        pass

class Bateria:
    def __init__(self,conectado:bool,cargando:bool,carga:int,tiempo:int):
        self.conectado=conectado
        self.cargando=cargando
        self.carga=carga#de 0 a 100
        self.tiempo=tiempo #en minutos
    @staticmethod
    def cambios():
        pass

class Bateria2(Subject):
    def __init__(self,conectado:bool,cargando:bool,carga:int,tiempomaximo:int):
        self.conectado=conectado
        self.cargando=cargando
        self.carga=carga#de 0 a 100
        self.tiempomax=tiempomaximo
        self.tiempo=int((tiempomaximo/100)*self.carga) #en minutos
    _observadores: List[Observador]=[]

    def attach(self, observer: Observador):
        print("Bateria: Se ha adjuntado un observador.")
        self._observadores.append(observer)

    def detach(self, observer: Observador):
        self._observadores.remove(observer)

    def notify(self):
        print("Bateria: Notificando a los observadores...")
        for observer in self._observadores:
            observer.update(self)


    def actualizar(self):
        self.cambiarBateria()
        print(f"Bateria: ¿Ahora estoy conectado?: {self.conectado}")
        self.notify()

    def cambiarBateria(self):
        if self.carga==100:
            self.cargando=False
        elif self.carga<=10:
            self.cargando=True
        if self.cargando==True:
            self.carga=100
            self.tiempo=self.tiempomax
            print("\nBateria:  Me estoy cargando.")
        else:
            self.carga=self.carga-10
            self.tiempo=int((self.tiempomax/100)*self.carga)
            print("\nBateria: Me estoy descargando.")

class Observador(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass

class ObservadorTiempo(Observador):
    def update(self, bateria: Subject):
        print(f"Tiempo: {bateria.tiempo}")

class ObservadorCarga(Observador):
    def update(self, bateria: Subject):
        print(f"Carga: {bateria.carga}")

if __name__ == "__main__":

    bateria = Bateria2(True,False,80,70)

    observador_tiempo = ObservadorTiempo()
    observador_carga = ObservadorCarga()
    bateria.attach(observador_tiempo)
    bateria.attach(observador_carga)
    for i in range (10):
        bateria.actualizar()
    
'''
    bateria.detach(observer_a)

    subject.some_business_logic()'''