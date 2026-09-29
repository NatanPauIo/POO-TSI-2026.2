class ErroDeConta(Exception):
    """para indicar um erro na conta bancária."""
class InvalidoValorError(ErroDeConta):
    """para indicar que um valor é inválido."""
class SaldoInsuficienteError(ErroDeConta):
    """para indicar que o saldo é insuficiente para a operação."""
class LimiteExcedidoError(ErroDeConta):
    """para indicar que o limite da conta foi excedido."""


class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise InvalidoValorError("Valor de depósito deve ser um número.")
        
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            raise InvalidoValorError("Valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise InvalidoValorError("Valor de saque deve ser um número.")
        if valor > 0 and valor <= 1000:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
                return
            elif valor > self._saldo:
                raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
            else:
                raise InvalidoValorError("Valor de saque deve ser positivo.")

        raise LimiteExcedidoError("O valor do saque excede o limite permitido de R$1000.")