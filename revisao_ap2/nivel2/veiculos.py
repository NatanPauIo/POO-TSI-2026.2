from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self,placa:str,diaria:int) -> None:
        self.placa = placa
        self.diaria = diaria

    @abstractmethod
    def calcular_aluguel(self,dias:int)-> None:
        pass

    def descricao(self) -> None:
        return f"Veiculo de placa {self.placa} , valor da diaria R${self.diaria}"

class Carro(Veiculo):
    def __init__(self, placa, diaria):
        super().__init__(placa, diaria)

    def calcular_aluguel(self,dias:int)-> float:
        return self.diaria * dias


class Moto(Veiculo):
    def __init__(self, placa, diaria):
        super().__init__(placa, diaria)

    def calcular_aluguel(self,dias:int)-> float:
        return (self.diaria * dias) - (self.diaria * dias*0.2)

class Caminhao(Veiculo) :
    def __init__(self, placa:str,diaria) -> None:
        super().__init__(diaria, placa=placa)

    def calcular_aluguel(self,dias:int)-> None:
            return self.diaria * dias + 100


class Locadora():
    def __init__(self) -> None:
        self.veiculos:list[Veiculo] = []

    def faturamento_previsto(self,dias:int) -> str:
        soma = 0
        for i in self.veiculos:
            soma += i.calcular_aluguel(dias)

        return f"O faturamento com os veiculos foi de {soma} em {dias} dias."

    def cadastrar(self,veiculo:Veiculo) -> None:
        if not isinstance(veiculo, Veiculo):
            raise TypeError("Informe um veiculo válido")

        self.veiculos.append(veiculo)
        return


c1 = Carro("111aaa", 10)
print(c1.descricao())
m1 = Moto("222bbb", 10)
c2 = Caminhao("333ccc")

print(c1.calcular_aluguel(10))
print(m1.calcular_aluguel(10))
print(c2.calcular_aluguel(10))

l1 = Locadora()
l1.cadastrar(c1)
l1.cadastrar(m1)
l1.cadastrar(c2)
print("Faturamento")
print(l1.faturamento_previsto(5))

#tentando instanciar classe abstrata
try:
    meu_veiculo = Veiculo()
except TypeError as e:
    print("PROVA: Não é possível instanciar a classe abstrata.")
    print(f"Mensagem do Python: {e}")
