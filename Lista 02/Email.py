class EmailInvalidoError(Exception):
    """Exceção personalizada para indicar que um email é inválido."""


class Email:
    def __init__(self, endereco):
        self.endereco = endereco
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor):
        if "@" not in valor or "." not in valor:
            raise EmailInvalidoError("Email inválido: deve conter '@' e '.'")
        self._endereco = valor


if __name__ == "__main__":
    try:
        email = Email("usuariodominio.com")
        print(f"Email válido: {email.endereco}")
    except EmailInvalidoError as e:
        print(f"Erro: {e}")

    try:
        email = Email("usuario@dominiocom")
        print(f"Email válido: {email.endereco}")
    except EmailInvalidoError as e:
        print(f"Erro: {e}")