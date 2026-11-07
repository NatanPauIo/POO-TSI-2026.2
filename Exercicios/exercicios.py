# ==============================================================================
# QUESTÃO 01: Leitura de 4 notas, exibição das notas e cálculo da média aritmética
# ==============================================================================
class BoletimNotas:
    def __init__(self, nota1: float, nota2: float, nota3: float, nota4: float) -> None:
        self._nota1 = nota1
        self._nota2 = nota2
        self._nota3 = nota3
        self._nota4 = nota4

    @property
    def notas(self) -> list:
        return [self._nota1, self._nota2, self._nota3, self._nota4]

    def calcular_media(self) -> float:
        return (self._nota1 + self._nota2 + self._nota3 + self._nota4) / 4

    def exibir_resultado(self) -> None:
        print(
            f"Notas digitadas: {self._nota1:.1f}, {self._nota2:.1f}, "
            f"{self._nota3:.1f}, {self._nota4:.1f}"
        )
        print(f"Média aritmética: {self.calcular_media():.2f}")

    def __str__(self) -> str:
        return f"BoletimNotas(notas={self.notas}, media={self.calcular_media():.2f})"


print(">>> QUESTÃO 01: Média Aritmética de 4 Notas")
boletim_q1 = BoletimNotas(8.5, 7.0, 9.0, 7.5)
boletim_q1.exibir_resultado()
print(f"Estado do objeto: {boletim_q1}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 02: Conversão de idade (anos, meses e dias) para total apenas em dias
# ==============================================================================
class IdadePessoa:
    def __init__(self, anos: int, meses: int, dias: int) -> None:
        self._anos = anos
        self._meses = meses
        self._dias = dias

    @property
    def anos(self) -> int:
        return self._anos

    @property
    def meses(self) -> int:
        return self._meses

    @property
    def dias(self) -> int:
        return self._dias

    def calcular_total_dias(self) -> int:
        return (self._anos * 365) + (self._meses * 30) + self._dias

    def exibir_idade_em_dias(self) -> None:
        total = self.calcular_total_dias()
        print(f"Idade informada: {self._anos} anos, {self._meses} meses e {self._dias} dias")
        print(f"Idade expressa apenas em dias: {total} dias")

    def __str__(self) -> str:
        return (
            f"IdadePessoa(anos={self._anos}, meses={self._meses}, "
            f"dias={self._dias}, total_dias={self.calcular_total_dias()})"
        )


print(">>> QUESTÃO 02: Idade Expressa em Dias")
idade_q2 = IdadePessoa(32, 5, 17)
idade_q2.exibir_idade_em_dias()
print(f"Estado do objeto: {idade_q2}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 03: Cálculo de minutos decorridos desde o início do dia
# ==============================================================================
class RelogioDia:
    def __init__(self, hora: int, minuto: int) -> None:
        self._hora = hora
        self._minuto = minuto

    @property
    def hora(self) -> int:
        return self._hora

    @property
    def minuto(self) -> int:
        return self._minuto

    def calcular_minutos_decorridos(self) -> int:
        return (self._hora * 60) + self._minuto

    def exibir_minutos(self) -> None:
        print(f"Horário informado: {self._hora:02d}:{self._minuto:02d}")
        print(
            f"Minutos decorridos desde o início do dia: "
            f"{self.calcular_minutos_decorridos()} minutos"
        )

    def __str__(self) -> str:
        return f"RelogioDia({self._hora:02d}:{self._minuto:02d})"


print(">>> QUESTÃO 03: Minutos desde o Início do Dia")
relogio_q3 = RelogioDia(14, 35)
relogio_q3.exibir_minutos()
print(f"Estado do objeto: {relogio_q3}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 04: Cálculo de salário de funcionário com acréscimo de 3% por filho
# ==============================================================================
class Funcionario:
    def __init__(
        self,
        nome_completo: str,
        horas_trabalhadas: float,
        valor_hora: float,
        numero_filhos: int,
    ) -> None:
        self._nome_completo = nome_completo
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora
        self._numero_filhos = numero_filhos

    def calcular_salario_bruto(self) -> float:
        return self._horas_trabalhadas * self._valor_hora

    def calcular_acrescimo_filhos(self) -> float:
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (0.03 * self._numero_filhos)

    def calcular_salario_final(self) -> float:
        return self.calcular_salario_bruto() + self.calcular_acrescimo_filhos()

    def exibir_contracheque(self) -> None:
        print(f"Funcionário: {self._nome_completo}")
        print(f"Horas trabalhadas/mês: {self._horas_trabalhadas}")
        print(f"Valor da hora: R$ {self._valor_hora:.2f}")
        print(f"Número de filhos: {self._numero_filhos}")
        print(f"Salário bruto: R$ {self.calcular_salario_bruto():.2f}")
        print(f"Acréscimo por filhos ({self._numero_filhos * 3}%): R$ {self.calcular_acrescimo_filhos():.2f}")
        print(f"Salário total a receber: R$ {self.calcular_salario_final():.2f}")

    def __str__(self) -> str:
        return (
            f"Funcionario(nome='{self._nome_completo}', "
            f"salario_final={self.calcular_salario_final():.2f})"
        )


print(">>> QUESTÃO 04: Cálculo de Salário de Funcionário")
funcionario_q4 = Funcionario("Carlos Eduardo Silva", 160, 25.0, 2)
funcionario_q4.exibir_contracheque()
print(f"Estado do objeto: {funcionario_q4}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 05: Quantidade de lâmpadas de 60W necessárias para iluminar uma sala
# ==============================================================================
class SalaIluminacao:
    def __init__(self, largura: float, profundidade: float) -> None:
        self._largura = largura
        self._profundidade = profundidade
        self._potencia_por_m2 = 18.0
        self._potencia_lampada = 60.0

    def calcular_area(self) -> float:
        return self._largura * self._profundidade

    def calcular_potencia_total(self) -> float:
        return self.calcular_area() * self._potencia_por_m2

    def calcular_quantidade_exata(self) -> float:
        return self.calcular_potencia_total() / self._potencia_lampada

    def calcular_quantidade_inteira(self) -> int:
        potencia_total = self.calcular_potencia_total()
        inteiro = int(potencia_total // self._potencia_lampada)
        if potencia_total % self._potencia_lampada > 0:
            inteiro += 1
        return inteiro

    def exibir_dimensionamento(self) -> None:
        print(f"Dimensões da sala: {self._largura}m x {self._profundidade}m")
        print(f"Área total: {self.calcular_area():.2f} m²")
        print(f"Potência necessária (18W/m²): {self.calcular_potencia_total():.2f} W")
        print(
            f"Quantidade de lâmpadas de 60W: {self.calcular_quantidade_exata():.2f} "
            f"({self.calcular_quantidade_inteira()} lâmpadas inteiras)"
        )

    def __str__(self) -> str:
        return (
            f"SalaIluminacao(area={self.calcular_area():.2f}m², "
            f"lampadas={self.calcular_quantidade_inteira()})"
        )


print(">>> QUESTÃO 05: Dimensionamento de Lâmpadas para uma Sala")
sala_q5 = SalaIluminacao(4.0, 5.0)
sala_q5.exibir_dimensionamento()
print(f"Estado do objeto: {sala_q5}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 06: Percentual de votos brancos, nulos e válidos de um município
# ==============================================================================
class ApuracaoEleitoral:
    def __init__(self, votos_brancos: int, votos_nulos: int, votos_validos: int) -> None:
        self._votos_brancos = votos_brancos
        self._votos_nulos = votos_nulos
        self._votos_validos = votos_validos

    def calcular_total_eleitores(self) -> int:
        return self._votos_brancos + self._votos_nulos + self._votos_validos

    def calcular_percentual_brancos(self) -> float:
        total = self.calcular_total_eleitores()
        return (self._votos_brancos / total) * 100 if total > 0 else 0.0

    def calcular_percentual_nulos(self) -> float:
        total = self.calcular_total_eleitores()
        return (self._votos_nulos / total) * 100 if total > 0 else 0.0

    def calcular_percentual_validos(self) -> float:
        total = self.calcular_total_eleitores()
        return (self._votos_validos / total) * 100 if total > 0 else 0.0

    def exibir_apuracao(self) -> None:
        total = self.calcular_total_eleitores()
        print(f"Total de eleitores: {total}")
        print(
            f"Votos brancos: {self._votos_brancos} "
            f"({self.calcular_percentual_brancos():.2f}%)"
        )
        print(
            f"Votos nulos:   {self._votos_nulos} "
            f"({self.calcular_percentual_nulos():.2f}%)"
        )
        print(
            f"Votos válidos: {self._votos_validos} "
            f"({self.calcular_percentual_validos():.2f}%)"
        )

    def __str__(self) -> str:
        return f"ApuracaoEleitoral(total={self.calcular_total_eleitores()})"


print(">>> QUESTÃO 06: Percentual de Votos Brancos, Nulos e Válidos")
apuracao_q6 = ApuracaoEleitoral(150, 250, 1600)
apuracao_q6.exibir_apuracao()
print(f"Estado do objeto: {apuracao_q6}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 07: Conversão de temperatura de Fahrenheit para Celsius
# ==============================================================================
class ConversorTemperatura:
    def __init__(self, fahrenheit: float) -> None:
        self._fahrenheit = fahrenheit

    @property
    def fahrenheit(self) -> float:
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, valor: float) -> None:
        self._fahrenheit = valor

    def converter_para_celsius(self) -> float:
        return 5 * (self._fahrenheit - 32) / 9

    def exibir_conversao(self) -> None:
        celsius = self.converter_para_celsius()
        print(f"Temperatura em Fahrenheit: {self._fahrenheit:.2f} °F")
        print(f"Temperatura em Celsius:    {celsius:.2f} °C")

    def __str__(self) -> str:
        return f"ConversorTemperatura({self._fahrenheit:.2f}°F -> {self.converter_para_celsius():.2f}°C)"


print(">>> QUESTÃO 07: Conversão de Fahrenheit para Celsius")
temp_q7 = ConversorTemperatura(212.0)
temp_q7.exibir_conversao()
print(f"Estado do objeto: {temp_q7}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 08: Cálculo do custo final de um carro novo ao consumidor
# ==============================================================================
class CustoCarroNovo:
    def __init__(self, custo_fabrica: float) -> None:
        self._custo_fabrica = custo_fabrica
        self._percentual_distribuidor = 0.28
        self._percentual_impostos = 0.45

    def calcular_valor_distribuidor(self) -> float:
        return self._custo_fabrica * self._percentual_distribuidor

    def calcular_valor_impostos(self) -> float:
        return self._custo_fabrica * self._percentual_impostos

    def calcular_custo_final(self) -> float:
        return (
            self._custo_fabrica
            + self.calcular_valor_distribuidor()
            + self.calcular_valor_impostos()
        )

    def exibir_custo(self) -> None:
        print(f"Custo de fábrica:           R$ {self._custo_fabrica:.2f}")
        print(f"Parcela do distribuidor (28%): R$ {self.calcular_valor_distribuidor():.2f}")
        print(f"Valor dos impostos (45%):      R$ {self.calcular_valor_impostos():.2f}")
        print(f"Custo final ao consumidor:  R$ {self.calcular_custo_final():.2f}")

    def __str__(self) -> str:
        return (
            f"CustoCarroNovo(fabrica={self._custo_fabrica:.2f}, "
            f"final={self.calcular_custo_final():.2f})"
        )


print(">>> QUESTÃO 08: Custo Final de um Carro Novo")
carro_q8 = CustoCarroNovo(50000.0)
carro_q8.exibir_custo()
print(f"Estado do objeto: {carro_q8}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 09: Verificação se número digitado está dentro ou fora da faixa de 1 a 10
# ==============================================================================
class VerificadorFaixa:
    def __init__(self, numero: int) -> None:
        self._numero = numero

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, valor: int) -> None:
        self._numero = valor

    def verificar_faixa(self) -> str:
        if 1 <= self._numero <= 10:
            return "O número digitado está DENTRO da faixa solicitada."
        else:
            return "O número digitado está FORA da faixa solicitada."

    def exibir_verificacao(self) -> None:
        print(f"Número informado: {self._numero}")
        print(self.verificar_faixa())

    def __str__(self) -> str:
        return f"VerificadorFaixa(numero={self._numero})"


print(">>> QUESTÃO 09: Verificação de Faixa (1 a 10)")
verif_dentro = VerificadorFaixa(7)
verif_dentro.exibir_verificacao()
verif_fora = VerificadorFaixa(15)
verif_fora.exibir_verificacao()
print(f"Estado dos objetos: {verif_dentro} | {verif_fora}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 10: Dados dois valores, informar qual deles é o maior
# ==============================================================================
class ComparadorMaiorValor:
    def __init__(self, valor1: float, valor2: float) -> None:
        self._valor1 = valor1
        self._valor2 = valor2

    def obter_maior(self) -> float:
        if self._valor1 >= self._valor2:
            return self._valor1
        else:
            return self._valor2

    def exibir_resultado(self) -> None:
        print(f"Valores comparados: {self._valor1} e {self._valor2}")
        if self._valor1 > self._valor2:
            print(f"O maior valor é: {self._valor1}")
        elif self._valor2 > self._valor1:
            print(f"O maior valor é: {self._valor2}")
        else:
            print(f"Os dois valores são iguais: {self._valor1}")

    def __str__(self) -> str:
        return f"ComparadorMaiorValor(v1={self._valor1}, v2={self._valor2}, maior={self.obter_maior()})"


print(">>> QUESTÃO 10: Maior entre Dois Valores")
comp_q10 = ComparadorMaiorValor(42, 19)
comp_q10.exibir_resultado()
print(f"Estado do objeto: {comp_q10}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 11: Diferença entre o maior valor e o menor valor entre dois inteiros
# ==============================================================================
class DiferencaValores:
    def __init__(self, valor1: int, valor2: int) -> None:
        self._valor1 = valor1
        self._valor2 = valor2

    def calcular_diferenca(self) -> int:
        if self._valor1 >= self._valor2:
            return self._valor1 - self._valor2
        else:
            return self._valor2 - self._valor1

    def exibir_diferenca(self) -> None:
        print(f"Valores inteiros informados: {self._valor1} e {self._valor2}")
        print(f"Diferença entre o maior e o menor valor: {self.calcular_diferenca()}")

    def __str__(self) -> str:
        return f"DiferencaValores(v1={self._valor1}, v2={self._valor2}, diferenca={self.calcular_diferenca()})"


print(">>> QUESTÃO 11: Diferença entre o Maior e o Menor Valor")
dif_q11 = DiferencaValores(18, 45)
dif_q11.exibir_diferenca()
print(f"Estado do objeto: {dif_q11}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 12: Leitura de 3 valores inteiros e exibição em ordem crescente
# ==============================================================================
class OrdenadorTresValores:
    def __init__(self, v1: int, v2: int, v3: int) -> None:
        self._v1 = v1
        self._v2 = v2
        self._v3 = v3

    def obter_ordem_crescente(self) -> list:
        a = self._v1
        b = self._v2
        c = self._v3
        if a <= b and a <= c:
            if b <= c:
                return [a, b, c]
            else:
                return [a, c, b]
        elif b <= a and b <= c:
            if a <= c:
                return [b, a, c]
            else:
                return [b, c, a]
        else:
            if a <= b:
                return [c, a, b]
            else:
                return [c, b, a]

    def exibir_ordem_crescente(self) -> None:
        ordenados = self.obter_ordem_crescente()
        print(f"Valores digitados: {self._v1}, {self._v2}, {self._v3}")
        print(f"Ordem crescente: {ordenados[0]}, {ordenados[1]}, {ordenados[2]}")

    def __str__(self) -> str:
        return f"OrdenadorTresValores(crescente={self.obter_ordem_crescente()})"


print(">>> QUESTÃO 12: Três Valores Inteiros em Ordem Crescente")
ord_q12 = OrdenadorTresValores(25, 7, 14)
ord_q12.exibir_ordem_crescente()
print(f"Estado do objeto: {ord_q12}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 13: Três valores inteiros ordenados em ordem crescente ou decrescente
# ==============================================================================
class OrdenadorEscolhido:
    def __init__(self, v1: int, v2: int, v3: int, opcao_ordem: str = "crescente") -> None:
        self._v1 = v1
        self._v2 = v2
        self._v3 = v3
        self._opcao_ordem = opcao_ordem

    def ordenar(self) -> list:
        base = OrdenadorTresValores(self._v1, self._v2, self._v3).obter_ordem_crescente()
        if self._opcao_ordem == "decrescente" or self._opcao_ordem == "D":
            return base[::-1]
        else:
            return base

    def exibir_resultado(self) -> None:
        ordenados = self.ordenar()
        print(f"Valores digitados: {self._v1}, {self._v2}, {self._v3}")
        print(f"Ordem escolhida ({self._opcao_ordem}): {ordenados[0]}, {ordenados[1]}, {ordenados[2]}")

    def __str__(self) -> str:
        return f"OrdenadorEscolhido(ordem='{self._opcao_ordem}', valores={self.ordenar()})"


print(">>> QUESTÃO 13: Ordenação Crescente ou Decrescente Conforme Escolha")
ord_cresc_q13 = OrdenadorEscolhido(12, 3, 29, "crescente")
ord_cresc_q13.exibir_resultado()
ord_decresc_q13 = OrdenadorEscolhido(12, 3, 29, "decrescente")
ord_decresc_q13.exibir_resultado()
print(f"Estado dos objetos: {ord_cresc_q13} | {ord_decresc_q13}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 14: Impressão dos números inteiros de 1 até 100 em ordem crescente
# ==============================================================================
class SequenciaCrescenteCem:
    def __init__(self, inicio: int = 1, fim: int = 100) -> None:
        self._inicio = inicio
        self._fim = fim

    def exibir_sequencia(self) -> None:
        print(f"Números inteiros de {self._inicio} até {self._fim} (ordem crescente):")
        for i in range(self._inicio, self._fim + 1):
            if i < self._fim:
                print(i, end=" ")
            else:
                print(i)

    def __str__(self) -> str:
        return f"SequenciaCrescenteCem(inicio={self._inicio}, fim={self._fim})"


print(">>> QUESTÃO 14: Números de 1 até 100 em Ordem Crescente")
seq_q14 = SequenciaCrescenteCem()
seq_q14.exibir_sequencia()
print(f"Estado do objeto: {seq_q14}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 15: Impressão dos números inteiros de 1 até 100 em ordem decrescente
# ==============================================================================
class SequenciaDecrescenteCem:
    def __init__(self, inicio: int = 1, fim: int = 100) -> None:
        self._inicio = inicio
        self._fim = fim

    def exibir_sequencia(self) -> None:
        print(f"Números inteiros de {self._inicio} até {self._fim} (ordem decrescente):")
        for i in range(self._fim, self._inicio - 1, -1):
            if i > self._inicio:
                print(i, end=" ")
            else:
                print(i)

    def __str__(self) -> str:
        return f"SequenciaDecrescenteCem(fim={self._fim}, inicio={self._inicio})"


print(">>> QUESTÃO 15: Números de 1 até 100 em Ordem Decrescente")
seq_q15 = SequenciaDecrescenteCem()
seq_q15.exibir_sequencia()
print(f"Estado do objeto: {seq_q15}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 16: Impressão de todos os números de um intervalo e seu somatório
# ==============================================================================
class IntervaloNumerico:
    def __init__(self, v_ini: int, v_fim: int) -> None:
        self._v_ini = v_ini
        self._v_fim = v_fim

    def obter_numeros_intervalo(self) -> list:
        numeros = []
        if self._v_ini <= self._v_fim:
            for i in range(self._v_ini, self._v_fim + 1):
                numeros += [i]
        else:
            for i in range(self._v_ini, self._v_fim - 1, -1):
                numeros += [i]
        return numeros

    def calcular_somatorio(self) -> int:
        soma = 0
        for num in self.obter_numeros_intervalo():
            soma += num
        return soma

    def exibir_intervalo_e_soma(self) -> None:
        numeros = self.obter_numeros_intervalo()
        print(f"Intervalo de {self._v_ini} até {self._v_fim}:")
        for num in numeros:
            print(num, end=" ")
        print()
        print(f"Somatório dos números do intervalo: {self.calcular_somatorio()}")

    def __str__(self) -> str:
        return (
            f"IntervaloNumerico(v_ini={self._v_ini}, v_fim={self._v_fim}, "
            f"somatorio={self.calcular_somatorio()})"
        )


print(">>> QUESTÃO 16: Números de um Intervalo e seu Somatório")
intervalo_q16 = IntervaloNumerico(5, 15)
intervalo_q16.exibir_intervalo_e_soma()
print(f"Estado do objeto: {intervalo_q16}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 17: Leitura de 10 números e impressão do somatório
# ==============================================================================
class SomatorioDezNumeros:
    def __init__(self, numeros: list) -> None:
        self._numeros = numeros[:]

    def calcular_somatorio(self) -> float:
        soma = 0
        for num in self._numeros:
            soma += num
        return soma

    def exibir_resultado(self) -> None:
        print(f"10 números fornecidos: {self._numeros}")
        print(f"Somatório dos 10 números: {self.calcular_somatorio()}")

    def __str__(self) -> str:
        return f"SomatorioDezNumeros(somatorio={self.calcular_somatorio()})"


print(">>> QUESTÃO 17: Somatório de 10 Números")
soma10_q17 = SomatorioDezNumeros([4, 8, 15, 16, 23, 42, 7, 11, 9, 5])
soma10_q17.exibir_resultado()
print(f"Estado do objeto: {soma10_q17}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 18: Leitura de 5 valores e somatório dos valores menores que 10
# ==============================================================================
class SomatorioMenoresQueDez:
    def __init__(self, valores: list) -> None:
        self._valores = valores[:]

    def calcular_somatorio(self) -> float:
        soma = 0
        for valor in self._valores:
            if valor < 10:
                soma += valor
        return soma

    def exibir_resultado(self) -> None:
        print(f"5 valores informados: {self._valores}")
        print(f"Somatório dos valores menores que 10: {self.calcular_somatorio()}")

    def __str__(self) -> str:
        return f"SomatorioMenoresQueDez(somatorio={self.calcular_somatorio()})"


print(">>> QUESTÃO 18: Somatório dos Valores Menores que 10 (dentre 5 valores)")
soma_menor10_q18 = SomatorioMenoresQueDez([3, 12, 7, 10, 8])
soma_menor10_q18.exibir_resultado()
print(f"Estado do objeto: {soma_menor10_q18}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 19: Leitura de 5 valores e somatório dos valores >= 10 e < 20
# ==============================================================================
class SomatorioFaixaDezAVinte:
    def __init__(self, valores: list) -> None:
        self._valores = valores[:]

    def calcular_somatorio(self) -> float:
        soma = 0
        for valor in self._valores:
            if valor >= 10 and valor < 20:
                soma += valor
        return soma

    def exibir_resultado(self) -> None:
        print(f"5 valores informados: {self._valores}")
        print(f"Somatório dos valores >= 10 e < 20: {self.calcular_somatorio()}")

    def __str__(self) -> str:
        return f"SomatorioFaixaDezAVinte(somatorio={self.calcular_somatorio()})"


print(">>> QUESTÃO 19: Somatório dos Valores >= 10 e < 20 (dentre 5 valores)")
soma_faixa_q19 = SomatorioFaixaDezAVinte([8, 10, 15, 20, 19])
soma_faixa_q19.exibir_resultado()
print(f"Estado do objeto: {soma_faixa_q19}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 20: Leitura de 5 valores e somatório dos valores pares digitados
# ==============================================================================
class SomatorioParesCincoValores:
    def __init__(self, valores: list) -> None:
        self._valores = valores[:]

    def calcular_somatorio_pares(self) -> int:
        soma = 0
        for valor in self._valores:
            if valor % 2 == 0:
                soma += valor
        return soma

    def exibir_resultado(self) -> None:
        print(f"5 valores informados: {self._valores}")
        print(f"Somatório dos valores pares: {self.calcular_somatorio_pares()}")

    def __str__(self) -> str:
        return f"SomatorioParesCincoValores(soma_pares={self.calcular_somatorio_pares()})"


print(">>> QUESTÃO 20: Somatório dos Valores Pares (dentre 5 valores)")
soma_pares_q20 = SomatorioParesCincoValores([6, 11, 4, 9, 12])
soma_pares_q20.exibir_resultado()
print(f"Estado do objeto: {soma_pares_q20}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 21: Quantidade definida pelo usuário e contagem de números pares
# ==============================================================================
class ContadorParesQuantidade:
    def __init__(self, quantidade: int, valores: list) -> None:
        self._quantidade = quantidade
        self._valores = valores[:quantidade]

    def contar_pares(self) -> int:
        qtd_pares = 0
        for i in range(self._quantidade):
            if self._valores[i] % 2 == 0:
                qtd_pares += 1
        return qtd_pares

    def exibir_resultado(self) -> None:
        print(f"Quantidade de valores informada: {self._quantidade}")
        print(f"Valores fornecidos: {self._valores}")
        print(f"Quantidade de números pares digitados: {self.contar_pares()}")

    def __str__(self) -> str:
        return f"ContadorParesQuantidade(qtd={self._quantidade}, pares={self.contar_pares()})"


print(">>> QUESTÃO 21: Contagem de Pares em N Valores Fornecidos")
cont_pares_q21 = ContadorParesQuantidade(6, [10, 3, 8, 7, 14, 22])
cont_pares_q21.exibir_resultado()
print(f"Estado do objeto: {cont_pares_q21}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 22: Soma das posições ímpares (1º,3º,5º,7º,9º) vs pares (2º,4º,6º,8º,10º)
# ==============================================================================
class SomatorioSequenciaPosicoes:
    def __init__(self, valores: list) -> None:
        self._valores = valores[:]

    def calcular_soma_posicoes_impares(self) -> float:
        # 1º, 3º, 5º, 7º e 9º elementos correspondem aos índices 0, 2, 4, 6 e 8
        soma = 0
        for i in range(0, len(self._valores), 2):
            soma += self._valores[i]
        return soma

    def calcular_soma_posicoes_pares(self) -> float:
        # 2º, 4º, 6º, 8º e 10º elementos correspondem aos índices 1, 3, 5, 7 e 9
        soma = 0
        for i in range(1, len(self._valores), 2):
            soma += self._valores[i]
        return soma

    def comparar_somatorios(self) -> str:
        soma_imp = self.calcular_soma_posicoes_impares()
        soma_par = self.calcular_soma_posicoes_pares()
        if soma_imp > soma_par:
            return "O somatório da sequência ímpar é MAIOR do que o da sequência par."
        elif soma_imp < soma_par:
            return "O somatório da sequência ímpar é MENOR do que o da sequência par."
        else:
            return "O somatório da sequência ímpar é IGUAL ao da sequência par."

    def exibir_resultado(self) -> None:
        print(f"10 valores digitados: {self._valores}")
        print(
            f"Soma da sequência ímpar (1º, 3º, 5º, 7º, 9º): "
            f"{self.calcular_soma_posicoes_impares()}"
        )
        print(
            f"Soma da sequência par   (2º, 4º, 6º, 8º, 10º): "
            f"{self.calcular_soma_posicoes_pares()}"
        )
        print(self.comparar_somatorios())

    def __str__(self) -> str:
        return (
            f"SomatorioSequenciaPosicoes(seq_impar={self.calcular_soma_posicoes_impares()}, "
            f"seq_par={self.calcular_soma_posicoes_pares()})"
        )


print(">>> QUESTÃO 22: Soma das Posições Ímpares (1º,3º,5º,7º,9º) vs Pares (2º,4º,6º,8º,10º)")
seq_pos_q22 = SomatorioSequenciaPosicoes([10, 5, 20, 8, 15, 12, 7, 6, 9, 4])
seq_pos_q22.exibir_resultado()
print(f"Estado do objeto: {seq_pos_q22}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 23: Somatório dos números pares e ímpares (entre 10 inteiros) e comparação
# ==============================================================================
class ComparadorSomaParesImpares:
    def __init__(self, valores: list) -> None:
        self._valores = valores[:]

    def calcular_soma_pares(self) -> int:
        soma_par = 0
        for v in self._valores:
            if v % 2 == 0:
                soma_par += v
        return soma_par

    def calcular_soma_impares(self) -> int:
        soma_impar = 0
        for v in self._valores:
            if v % 2 != 0:
                soma_impar += v
        return soma_impar

    def comparar_somatorios(self) -> str:
        soma_impar = self.calcular_soma_impares()
        soma_par = self.calcular_soma_pares()
        if soma_impar > soma_par:
            return "O somatório dos números ímpares é MAIOR do que o dos números pares."
        elif soma_impar < soma_par:
            return "O somatório dos números ímpares é MENOR do que o dos números pares."
        else:
            return "O somatório dos números ímpares é IGUAL ao dos números pares."

    def exibir_resultado(self) -> None:
        print(f"10 valores inteiros digitados: {self._valores}")
        print(f"Somatório dos números pares:   {self.calcular_soma_pares()}")
        print(f"Somatório dos números ímpares: {self.calcular_soma_impares()}")
        print(self.comparar_somatorios())

    def __str__(self) -> str:
        return (
            f"ComparadorSomaParesImpares(soma_pares={self.calcular_soma_pares()}, "
            f"soma_impares={self.calcular_soma_impares()})"
        )


print(">>> QUESTÃO 23: Comparação entre Somatório dos Pares e dos Ímpares")
comp_soma_q23 = ComparadorSomaParesImpares([2, 7, 4, 9, 6, 11, 8, 13, 10, 15])
comp_soma_q23.exibir_resultado()
print(f"Estado do objeto: {comp_soma_q23}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 24: Somatório de sequência exibindo a expressão (ex: 2+7+3+8+6=26)
# ==============================================================================
class SomatorioExpressaoSequencia:
    def __init__(self, total_numeros: int, numeros: list) -> None:
        self._total_numeros = total_numeros
        self._numeros = numeros[:total_numeros]

    def calcular_soma(self) -> int:
        soma = 0
        for num in self._numeros:
            soma += num
        return soma

    def gerar_expressao_saida(self) -> str:
        expressao = ""
        for i in range(len(self._numeros)):
            expressao += str(self._numeros[i])
            if i < len(self._numeros) - 1:
                expressao += "+"
        expressao += "=" + str(self.calcular_soma())
        return expressao

    def exibir_resultado(self) -> None:
        print("Programa para cálculo do somatório de uma sequência de números.")
        print(f"Digite o total de números a serem somados: {self._total_numeros}")
        print("Números digitados pelo usuário:", end=" ")
        for num in self._numeros:
            print(num, end=" ")
        print()
        print(f"Saída no terminal: {self.gerar_expressao_saida()}")

    def __str__(self) -> str:
        return f"SomatorioExpressaoSequencia('{self.gerar_expressao_saida()}')"


print(">>> QUESTÃO 24: Somatório Formatado de uma Sequência")
seq_soma_q24 = SomatorioExpressaoSequencia(5, [2, 7, 3, 8, 6])
seq_soma_q24.exibir_resultado()
print(f"Estado do objeto: {seq_soma_q24}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 25: Números divisíveis por 7 e não múltiplos de 5 entre 1000 e 3000
# ==============================================================================
class FiltroDivisiveisPorSete:
    def __init__(self, inicio: int = 1000, fim: int = 3000) -> None:
        self._inicio = inicio
        self._fim = fim

    def obter_numeros_filtrados(self) -> list:
        filtrados = []
        for num in range(self._inicio, self._fim + 1):
            if num % 7 == 0 and num % 5 != 0:
                filtrados += [num]
        return filtrados

    def exibir_numeros(self) -> None:
        numeros = self.obter_numeros_filtrados()
        print(
            f"Números divisíveis por 7 e não múltiplos de 5 "
            f"no intervalo de {self._inicio} a {self._fim}:"
        )
        for i in range(len(numeros)):
            if i < len(numeros) - 1:
                print(numeros[i], end=";")
            else:
                print(numeros[i])

    def __str__(self) -> str:
        return (
            f"FiltroDivisiveisPorSete(intervalo=[{self._inicio}, {self._fim}], "
            f"total_encontrados={len(self.obter_numeros_filtrados())})"
        )


print(">>> QUESTÃO 25: Divisíveis por 7 e Não Múltiplos de 5 (1000 a 3000)")
filtro_q25 = FiltroDivisiveisPorSete(1000, 3000)
filtro_q25.exibir_numeros()
print(f"Estado do objeto: {filtro_q25}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 26: Contabilização de pares e ímpares até digitar número negativo
# ==============================================================================
class ContabilizadorAteNegativo:
    def __init__(self, sequencia_entrada: list) -> None:
        self._sequencia_entrada = sequencia_entrada[:]
        self._qtd_pares = 0
        self._qtd_impares = 0
        self._processar_com_while()

    def _processar_com_while(self) -> None:
        self._qtd_pares = 0
        self._qtd_impares = 0
        indice = 0
        while indice < len(self._sequencia_entrada):
            valor = self._sequencia_entrada[indice]
            if valor < 0:
                break
            if valor % 2 == 0:
                self._qtd_pares += 1
            else:
                self._qtd_impares += 1
            indice += 1

    @property
    def qtd_pares(self) -> int:
        return self._qtd_pares

    @property
    def qtd_impares(self) -> int:
        return self._qtd_impares

    def exibir_resultado(self) -> None:
        print(f"Sequência de entradas (sentinela negativo): {self._sequencia_entrada}")
        print(f"Quantidade de números pares:   {self._qtd_pares}")
        print(f"Quantidade de números ímpares: {self._qtd_impares}")

    def __str__(self) -> str:
        return (
            f"ContabilizadorAteNegativo(pares={self._qtd_pares}, "
            f"impares={self._qtd_impares})"
        )


print(">>> QUESTÃO 26: Contagem de Pares e Ímpares até Número Negativo")
cont_neg_q26 = ContabilizadorAteNegativo([4, 7, 12, 9, 15, 20, 0, -5, 100])
cont_neg_q26.exibir_resultado()
print(f"Estado do objeto: {cont_neg_q26}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 27: Sequência de 1 até N substituindo múltiplos de 3 (PI), 7 (PA) e ambos (POW)
# ==============================================================================
class SequenciaPiPaPow:
    def __init__(self, limite: int) -> None:
        self._limite = limite

    def gerar_sequencia(self) -> list:
        resultado = []
        for num in range(1, self._limite + 1):
            if num % 3 == 0 and num % 7 == 0:
                resultado += ["POW"]
            elif num % 3 == 0:
                resultado += ["PI"]
            elif num % 7 == 0:
                resultado += ["PA"]
            else:
                resultado += [num]
        return resultado

    def exibir_sequencia(self) -> None:
        sequencia = self.gerar_sequencia()
        print(f"Sequência PI / PA / POW de 1 até {self._limite}:")
        for item in sequencia:
            print(item, end=" ")
        print()

    def __str__(self) -> str:
        return f"SequenciaPiPaPow(limite={self._limite})"


print(">>> QUESTÃO 27: Sequência de 1 até N com PI (múlt. 3), PA (múlt. 7) e POW (múlt. 3 e 7)")
pipapow_q27 = SequenciaPiPaPow(25)
pipapow_q27.exibir_sequencia()
print(f"Estado do objeto: {pipapow_q27}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 28: Vetor de 10 posições inteiras e contagem de pares (zero é neutro)
# ==============================================================================
class VetorDezPosicoesPares:
    def __init__(self, valores: list) -> None:
        self._vetor = valores[:10]

    @property
    def vetor(self) -> list:
        return self._vetor[:]

    def contar_pares_sem_zero(self) -> int:
        qtd_pares = 0
        for num in self._vetor:
            # Conforme enunciado: ZERO é neutro, NÃO É PAR
            if num != 0 and num % 2 == 0:
                qtd_pares += 1
        return qtd_pares

    def exibir_resultado(self) -> None:
        print(f"Vetor de 10 posições: {self._vetor}")
        print(
            f"Quantidade de valores pares (considerando 0 neutro): "
            f"{self.contar_pares_sem_zero()}"
        )

    def __str__(self) -> str:
        return (
            f"VetorDezPosicoesPares(vetor={self._vetor}, "
            f"pares={self.contar_pares_sem_zero()})"
        )


print(">>> QUESTÃO 28: Contagem de Pares em Vetor de 10 Posições (Zero Neutro)")
vetor_q28 = VetorDezPosicoesPares([0, 2, 5, 8, 11, 14, 0, 7, 20, 6])
vetor_q28.exibir_resultado()
print(f"Estado do objeto: {vetor_q28}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 29: Leitura da nota de 10 alunos, maior nota, menor nota e média
# ==============================================================================
class TurmaDezAlunos:
    def __init__(self, notas: list) -> None:
        self._notas = notas[:10]

    def obter_maior_nota(self) -> float:
        maior = self._notas[0]
        for nota in self._notas:
            if nota > maior:
                maior = nota
        return maior

    def obter_menor_nota(self) -> float:
        menor = self._notas[0]
        for nota in self._notas:
            if nota < menor:
                menor = nota
        return menor

    def calcular_media(self) -> float:
        soma = 0.0
        for nota in self._notas:
            soma += nota
        return soma / len(self._notas)

    def exibir_estatisticas(self) -> None:
        print(f"Notas dos 10 alunos: {self._notas}")
        print(f"Maior nota: {self.obter_maior_nota():.2f}")
        print(f"Menor nota: {self.obter_menor_nota():.2f}")
        print(f"Média das notas: {self.calcular_media():.2f}")

    def __str__(self) -> str:
        return (
            f"TurmaDezAlunos(maior={self.obter_maior_nota():.2f}, "
            f"menor={self.obter_menor_nota():.2f}, media={self.calcular_media():.2f})"
        )


print(">>> QUESTÃO 29: Maior, Menor e Média das Notas de 10 Alunos")
turma_q29 = TurmaDezAlunos([7.5, 9.0, 5.5, 8.0, 6.0, 10.0, 4.5, 7.0, 8.5, 6.5])
turma_q29.exibir_estatisticas()
print(f"Estado do objeto: {turma_q29}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 30: Dois vetores de 5 inteiros (vet1 e vet2) com somaPAR e somaIMPAR
# ==============================================================================
class SomadorDoisVetores:
    def __init__(self, valores_dez: list) -> None:
        self.vet1 = valores_dez[:5]
        self.vet2 = valores_dez[5:10]
        self.somaPAR = 0
        self.somaIMPAR = 0
        self.calcular_somas()

    def calcular_somas(self) -> None:
        self.somaPAR = 0
        self.somaIMPAR = 0
        for valor in self.vet1 + self.vet2:
            if valor % 2 == 0:
                self.somaPAR += valor
            else:
                self.somaIMPAR += valor

    def exibir_resultado(self) -> None:
        print(f"Vetor 1 (vet1): {self.vet1}")
        print(f"Vetor 2 (vet2): {self.vet2}")
        print(f"Valor de somaPAR:   {self.somaPAR}")
        print(f"Valor de somaIMPAR: {self.somaIMPAR}")

    def __str__(self) -> str:
        return (
            f"SomadorDoisVetores(vet1={self.vet1}, vet2={self.vet2}, "
            f"somaPAR={self.somaPAR}, somaIMPAR={self.somaIMPAR})"
        )


print(">>> QUESTÃO 30: Soma dos Pares (somaPAR) e Ímpares (somaIMPAR) de vet1 e vet2")
vetores_q30 = SomadorDoisVetores([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vetores_q30.exibir_resultado()
print(f"Estado do objeto: {vetores_q30}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 31: Competição de salto em distância (5 saltos por atleta)
# ==============================================================================
class AtletaSalto:
    def __init__(self, nome: str, saltos: list) -> None:
        self._nome = nome
        self._saltos = saltos[:5]

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def saltos(self) -> list:
        return self._saltos[:]

    def calcular_media(self) -> float:
        soma = 0.0
        for salto in self._saltos:
            soma += salto
        return soma / len(self._saltos)

    def exibir_relatorio(self, numero_atleta: int) -> None:
        ordens = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
        print(f"Atleta {numero_atleta}: {self._nome}\n")
        for i in range(len(self._saltos)):
            print(f"{ordens[i]} Salto: {self._saltos[i]} m")
        print("\nResultado final:")
        print(f"Atleta: {self._nome}")
        texto_saltos = ""
        for i in range(len(self._saltos)):
            texto_saltos += str(self._saltos[i])
            if i < len(self._saltos) - 1:
                texto_saltos += " - "
        print(f"Saltos: {texto_saltos}")
        media = self.calcular_media()
        # Formatação limpa conforme o exemplo do PDF (5.9 m e 6.18 m)
        print(f"Média dos saltos: {round(media, 2)} m")

    def __str__(self) -> str:
        return f"AtletaSalto(nome='{self._nome}', media={round(self.calcular_media(), 2)})"


class CompeticaoSaltoDistancia:
    def __init__(self, registros_entrada: list) -> None:
        self._registros_entrada = registros_entrada[:]
        self._atletas = []
        self._processar_registros()

    def _processar_registros(self) -> None:
        indice = 0
        while indice < len(self._registros_entrada):
            nome, saltos = self._registros_entrada[indice]
            # Encerra quando não for informado o nome do atleta
            if nome == "":
                break
            self._atletas += [AtletaSalto(nome, saltos)]
            indice += 1

    def exibir_resultados(self) -> None:
        for i in range(len(self._atletas)):
            self._atletas[i].exibir_relatorio(i + 1)
            if i < len(self._atletas) - 1:
                print("\n-------------------------------------------\n")

    def __str__(self) -> str:
        return f"CompeticaoSaltoDistancia(total_atletas={len(self._atletas)})"


print(">>> QUESTÃO 31: Competição de Salto em Distância")
dados_competicao_q31 = [
    ("João do Pulo", [6.5, 6.1, 6.2, 5.4, 5.3]),
    ("João do Salto", [6.5, 6.4, 6.6, 5.9, 5.5]),
    ("", []),  # Sentinela de parada: nome vazio encerra a leitura
]
competicao_q31 = CompeticaoSaltoDistancia(dados_competicao_q31)
competicao_q31.exibir_resultados()
print(f"\nEstado do objeto: {competicao_q31}")
print("\n" + "=" * 60 + "\n")


# ==============================================================================
# QUESTÃO 32: Comparativo de Consumo de Combustível entre Modelos de Carros
# ==============================================================================
class ComparativoConsumoCombustivel:
    def __init__(
        self,
        modelos: list,
        consumos: list,
        distancia_km: float = 1000.0,
        preco_gasolina: float = 7.50,
    ) -> None:
        self._modelos = modelos[:]
        self._consumos = consumos[:]
        self._distancia_km = distancia_km
        self._preco_gasolina = preco_gasolina

    def calcular_litros(self, consumo_km_l: float) -> float:
        return self._distancia_km / consumo_km_l

    def calcular_custo(self, consumo_km_l: float) -> float:
        return self.calcular_litros(consumo_km_l) * self._preco_gasolina

    def obter_modelo_mais_economico(self) -> str:
        indice_maior_rendimento = 0
        for i in range(1, len(self._consumos)):
            if self._consumos[i] > self._consumos[indice_maior_rendimento]:
                indice_maior_rendimento = i
        return self._modelos[indice_maior_rendimento]

    def exibir_relatorio(self) -> None:
        print("Comparativo de Consumo de Combustível\n")
        for i in range(len(self._modelos)):
            print(f"Veículo {i + 1}")
            print(f"Nome: {self._modelos[i]}")
            print(f"Km por litro: {self._consumos[i]}")

        print("\nRelatório Final")
        for i in range(len(self._modelos)):
            modelo = self._modelos[i]
            km_l = self._consumos[i]
            litros = self.calcular_litros(km_l)
            custo = self.calcular_custo(km_l)
            print(
                f" {i + 1} - {modelo:<10} - {km_l:>5.1f} - "
                f"{litros:>5.1f} litros - R$ {custo:>6.2f}"
            )
        print(f"O menor consumo é do {self.obter_modelo_mais_economico()}.")

    def __str__(self) -> str:
        return (
            f"ComparativoConsumoCombustivel(veiculos={len(self._modelos)}, "
            f"mais_economico='{self.obter_modelo_mais_economico()}')"
        )


print(">>> QUESTÃO 32: Comparativo de Consumo de Combustível")
modelos_q32 = ["Fusca", "Gol", "Uno", "Vectra", "HB20"]
consumos_q32 = [7, 10, 12.5, 9, 14.5]
comparativo_q32 = ComparativoConsumoCombustivel(modelos_q32, consumos_q32)
comparativo_q32.exibir_relatorio()
print(f"\nEstado do objeto: {comparativo_q32}")
print("\n" + "=" * 60 + "\n")