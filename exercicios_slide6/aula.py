#Questão 1
t1 = (1,2,3,4,5,6,7,8,9,10)

def retorna_pares(tupla):
    pares = ()
    for i in tupla:
        if i % 2 == 0:
           # adicionar valores a uma tupla já criada
           pares  += (i,) 
    return pares

print(retorna_pares(t1))

print("\n")
#Questão 2
frutas = ("uva", "abacate", "pessego","laranja", "amora")

lista_frutas = list(frutas)
tamanho_lista = len(lista_frutas)
#print(tamanho_lista)
for i in range(tamanho_lista):
   for j in range(0,tamanho_lista - i - 1):
      if lista_frutas[j] > lista_frutas[j+1]:
         lista_frutas[j] = lista_frutas[j+1]
         lista_frutas[j+1] = lista_frutas[j]

frutas_ordenadas = tuple(lista_frutas)
print(frutas_ordenadas) 
