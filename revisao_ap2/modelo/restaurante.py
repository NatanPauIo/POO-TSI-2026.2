from modelo.entidades import *
from modelo.entregadores import *
from modelo.erros import *

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
    
        taxa = entregador.taxa_entrega(distancia)
       
        p1 = Pedido(entregador,cliente,distancia)
        if not isinstance(p1, Pedido):
            raise PedidoError("Houve algum erro ao lançar seu pedido")

        for i in itens:
            p1.itens.append(i)

        self.pedidos.append(p1)
        print(f"Seu pedido foi lançado com sucesso! O total do seu pedido foi {p1.total}, taxa de entrega {taxa}")
        return

    

