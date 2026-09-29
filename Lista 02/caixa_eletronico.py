import ContaBancaria

if __name__ == "__main__":
    c1 = ContaBancaria.ContaBancaria()
    opção = ""

    while True:
        print("Bem-vindo ao Caixa Eletrônico!")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Saldo")
        print("4. sair")
        opção = input("Escolha uma opção: ")

        if opção == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            try:
                c1.depositar(valor)
            except ContaBancaria.InvalidoValorError as e:
                print(f"Erro: {e}")
        elif opção == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            try:
                c1.sacar(valor)
            except ContaBancaria.InvalidoValorError as e:
                print(f"Erro: {e}")
            except ContaBancaria.SaldoInsuficienteError as e:
                print(f"Erro: {e}")
            except ContaBancaria.LimiteExcedidoError as e:
                print(f"Erro: {e}")
        elif opção == "3":
            print(f"Saldo atual: R${c1.saldo:.2f}")
        elif opção == "4":
            print("Saindo do Caixa Eletrônico. Até logo!")
            break


