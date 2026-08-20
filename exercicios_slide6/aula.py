t1 = (1,2,3,4,5,6,7,8,9,10)


def retorna_pares(tupla):
    pares = ()
    for i in tupla:
        if i % 2 == 0:
           # adicionar valores a uma tupla já criada
           pares  += (i,) 
    return pares

print(retorna_pares(t1))