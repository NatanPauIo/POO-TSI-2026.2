class Funcionario:

    def __init__(self,nome:str, salario:float):
        self.nome = nome
        self._salario = salario


    @property
    def salario(self):
        return self._salario

    def aumentar(self, percentual:float):
        if percentual < 1 or percentual > 30:
            raise ValueError("O percentual de aumento deve estar entre 1 e 30")

        self._salario += self._salario * percentual / 100

    @salario.setter
    def salario(self, valor:float):
        if valor < 1621:
            raise ValueError("O salário não pode ser menor que 1621")
        
        self._salario = valor

if __name__ == "__main__":
    f1 = Funcionario("João", 2000)
    f2 = Funcionario("Maria", 2500)

    try:
        f1.aumentar(35)
    except ValueError as e:
        print(f"Erro: {e}")

    try:
        f2.salario = 1500
    except ValueError as e:
        print(f"Erro: {e}")
