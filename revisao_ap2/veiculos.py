from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self,placa:str,diaria:int) -> None:
        self.placa = placa
        self.diaria = diaria

    @abstractmethod
    def calcular_aluguel(self,dias:int)-> None:
        pass

    def descricao():
        pass

class Carro(Veiculo):
    def __init__(self, placa, diaria)-> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self,dias:int)-> None:
            pass


class Moto(Veiculo):
    def __init__(self, placa, diaria)-> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self,dias:int)-> None:
            pass

class Caminhao(Veiculo) :
    def __init__(self, placa, diaria) -> None:
        super().__init__(placa, diaria)

    def calcular_aluguel(self,dias:int)-> None:
            pass


class Locadora():
    def __init__(self) -> None:
        self.veiculos:list[Veiculo] = []

    def faturamento_previsto(dias:int) -> float:
        pass



#tentando instanciar classe abstrata
try:
    meu_veiculo = Veiculo()
except TypeError as erro:
    print("PROVA: Não é possível instanciar a classe abstrata.")
    print(f"Mensagem do Python: {erro}")
