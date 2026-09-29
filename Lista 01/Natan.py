#Aplicação de Aluno
class Aluno:
    

    def __init__(self, nome:str,matricula:str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def lancar_nota(self,valor:float):
        self.notas.append(valor)

    def media(self) -> float:
        soma = 0
        for i in self.notas:
            soma += i

        
        return soma/len(self.notas)

    def aprovado(self) -> bool:
        if(self.media() >= 6):
            return True

        return False
    def __str__(self):
        return f"{self.nome} ({self.matricula}) - Média {self.media()}"

alunos = [ Aluno("a1","123"),Aluno("a2","321"),Aluno("a3","231")]

nota = 4

for i in alunos:
    i.lancar_nota(nota)
    nota += 1
    i.lancar_nota(nota)
    nota += 1

for i in alunos:
    if(i.aprovado()):
        print(f"{i} - Aprovado")
    else:
        print(f"{i} - Reprovado")

#Aplicação Retangulo
class Retangulo:

    def __init__(self, base:float,altura:float):
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 + (self.base+self.altura)

    def __eq__(self, obj:object):
        if not isinstance(obj, Retangulo):
            return NotImplemented

        return self.base == obj.base and self.altura == obj.altura

r1 = Retangulo(10,21)
r2 = Retangulo(10,20)

print(r1 == r2)

#Aplicação Data

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @staticmethod
    def bissexto(ano:int) -> bool:
        if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True

        return False

    @classmethod
    def de_texto(cls, data:str):
        dia, mes, ano = data.split('/')
        return cls(int(dia),int(mes),int(ano))
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"


