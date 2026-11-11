#from delivery import *
from revisao_ap2.nivel3.modelo import *

#restaurante
r1 = Restaurante("Baboon",15)
p1 = Prato("Risoto", 50)
p2 = Prato("Macarrao", 40)
r1.cardapio.adicionar_prato(p1)
r1.cardapio.adicionar_prato(p2)

#cliente
c1 = Cliente("Alex","3333")
c2 = Cliente("Alex","4444")

#entregador
e1 = DeBike("João","1111",30)
e2 = DeMoto("Pedro","2222",50)

itens_pedido1 = [Item(2, r1.cardapio.pratos[0])]
itens_pedido2 = [Item(2, r1.cardapio.pratos[0]), Item(1, r1.cardapio.pratos[1])]

try:
   r1.lancar_pedido(e1,c1,25,itens_pedido1) 
except EntregaForaDeAreaError as e:
   print(e)
except PedidoError as e:
   print(e)

try: 
   r1.lancar_pedido(e2,c1,60,itens_pedido2)
except EntregaForaDeAreaError as e:
   print(e)
except PedidoError as e:
   print(e)





