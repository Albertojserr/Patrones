from abc import ABC, abstractmethod
class Builder(ABC):
    @abstractmethod
    def numeroAmbulancias(self):
        pass

    @abstractmethod
    def tiempoRespuesta(self):
        pass

class Ambulatorio(Builder):
    def __init__(self,base:str,ambulancias:int,tiempo:int):
        self.base=base
        self.ambulancias=ambulancias
        self.tiempo=tiempo
    def numeroAmbulancias(self):
        return("En "+str(self.base)+" hay "+str(self.ambulancias)+" ambulancias")
    def tiempoRespuesta(self):
        return("En "+str(self.base)+" las ambulancias tardan "+str(self.tiempo)+" minutos")

class AreaSanitaria(Builder):
    def __init__(self,base:int,ambulatorios:list[Ambulatorio]):
        self.base=base
        self.ambulatorios=ambulatorios
    def numeroAmbulancias(self):
        ambulancias=0
        for ambulatorio in self.ambulatorios:
            ambulancias+=ambulatorio.ambulancias
        return("En "+str(self.base)+" hay "+str(ambulancias)+" ambulancias")
    def tiempoRespuesta(self):
        tiempo=0
        for ambulatorio in self.ambulatorios:
            tiempo+=ambulatorio.tiempo
        return("En "+str(self.base)+" las ambulancias tardan una media de "+str(tiempo/len(self.ambulatorios))+" minutos")

if __name__ == "__main__":
    ambulancia1=Ambulatorio("Getafe Norte",5,50)
    ambulancia2=Ambulatorio("Los Molinos",4,40)
    ambulatorio1=AreaSanitaria("Getafe",[ambulancia1,ambulancia2])
    print(ambulancia1.numeroAmbulancias())
    print(ambulancia2.numeroAmbulancias())
    print(ambulatorio1.numeroAmbulancias())
    print(ambulancia1.tiempoRespuesta())
    print(ambulancia2.tiempoRespuesta())
    print(ambulatorio1.tiempoRespuesta())