from delivery import *
r1 = Restaurante("Baboon",15)
p1 = Prato("Risoto", 50)
p2 = Prato("Macarrao", 40)
r1.cardapio.adicionar_prato(p1)
r1.cardapio.adicionar_prato(p2)

c1 = Cliente("Alex","3333")
c2 = Cliente("Alex","4444")

e1 = DeBike("João","1111",30)
e2 = DeMoto("Pedro","2222",50)

Pedido()