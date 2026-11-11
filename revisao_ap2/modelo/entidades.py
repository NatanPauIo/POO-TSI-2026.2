class Prato():
    def __init__(self, nome:str,valor:float) -> None:
        self.nome = nome
        self.valor = valor

class Cliente():
    def __init__(self,nome:str,cpf:str) -> None:
        self.nome = nome 
        self.cpf = cpf

class Item():
    def __init__(self,quantidade:int,prato:Prato) -> None:
        self.quantidade = quantidade
        self.prato = prato

    @property
    def total(self):
        return self.prato.valor * self.quantidade

class Cardapio():
    def __init__(self) -> None:
        self.pratos:list[Prato] = []

    def adicionar_prato(self,prato:Prato) -> None:
        if not isinstance(prato, Prato):
            raise TypeError("Informe um prato válido")

        self.pratos.append(prato)