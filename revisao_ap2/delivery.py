from abc import ABC, abstractmethod

class EntregaForaDeAreaError(Exception):
    """Exececao para distancia > limite do entregador"""
class PedidoError(Exception):
    """Exececao para erro no pedido"""

class Prato():
    def __init__(self, nome:str,valor:float) -> None:
        self.nome = nome
        self.valor = valor

class Cardapio():
    def __init__(self) -> None:
        self.pratos:list[Prato] = []

    def adicionar_prato(self,prato:Prato) -> None:
        if not isinstance(prato, Prato):
            raise TypeError("Informe um prato válido")

        self.pratos.append(prato)


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

class Pedido():
    def __init__(self,entregador:Entregador,cliente:Cliente, distancia:float) -> None:
        self.itens:list[Item] = []
        self.entregador = entregador
        self.cliente = cliente
        self.distancia = distancia

    def adicionar_item(self,item:Item):
        if not isinstance(item, Item):
            raise Exception("Houve algum erro ao lançar seu pedido")

        
    @property
    def total(self):
        soma = 0
        for i in self.itens:
            soma += i.total

        return soma + self.entregador.taxa_entrega(self.distancia)

class Restaurante():
    def __init__(self,nome:str,mesas:int) -> None:
        self.nome = nome
        self.mesas = mesas
        self.cardapio = Cardapio()
        self.pedidos:list[Pedido] = []

    def lancar_pedido(self, entregador:Entregador, cliente:Cliente, distancia:float,itens:list[Item]) -> None:
        try:
            taxa = entregador.taxa_entrega(distancia)
        except EntregaForaDeAreaError as e:
            print(e)
            return
        
        p1 = Pedido(entregador,cliente,distancia)
        if not isinstance(p1, Pedido):
            raise PedidoError("Houve algum erro ao lançar seu pedido")

        for i in itens:
            p1.itens.append(i)

        self.pedidos.append(p1)
        print(f"Seu pedido foi lançado com sucesso! O total do seu pedido foi {p1.total}, taxa de entrega {taxa}")
        return

    











