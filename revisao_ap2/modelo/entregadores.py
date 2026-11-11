from abc import ABC, abstractmethod 
from modelo.erros import EntregaForaDeAreaError

class Entregador(ABC):
    def __init__(self,nome:str,cpf:str,limite:float) -> None:
        self.nome = nome
        self.cpf = cpf
        self.limite = limite

    @abstractmethod
    def taxa_entrega(self,distancia:float) -> float:
        pass


class DeBike(Entregador):
    def taxa_entrega(self,distancia:float) -> float:
        if(distancia > self.limite):
            raise EntregaForaDeAreaError("O entragador não atende até essa região")

        return distancia * 0.8

class DeMoto(Entregador):
    def taxa_entrega(self,distancia:float) -> float:
        if(distancia > self.limite):
            raise EntregaForaDeAreaError("O entragador não atende até essa região")

        return distancia * 1