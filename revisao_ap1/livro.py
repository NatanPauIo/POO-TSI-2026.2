class LivroIndisponivelError(Exception):
    """Erro de livro indisponivel"""
class LivroNaoEncontradoError(Exception):
    """Erro de livro não encontrado"""
class Livro:
    def __init__(self,titulo:str,ano:int) -> None:
        self.titulo = titulo
        self.ano = ano
        self.disponivel = True

    def __eq__(self, value:object) -> bool:
        if not isinstance(value, Livro):
            return NotImplemented   

        return (self.titulo == value.titulo and self.ano == value.ano)

    def __str__(self) -> str:
        return f"Titulo do livro: {self.titulo}| Ano do livro: {self.ano}"
    
class Biblioteca:
    def __init__(self) -> None:
        self.acervo = []

    def cadastrar(self,l:Livro) -> None:
        self.acervo.append(l)

    def emprestar(self,t:str) -> None:
        for i in self.acervo:
            if i.titulo == t and i.disponivel:
                print(f"Livro emprestado com sucesso!")
                i.disponivel = False
                return

            raise LivroIndisponivelError("O livro não está disponivel")
        
    def devolver(self,t:str) -> None:
        for i in self.acervo:
                    if i.titulo == t and i.disponivel == False:
                        print(f"Livro devolvido com sucesso!")
                        i.disponivel = True
                        return

        raise LivroNaoEncontradoError("Erro ao devolver o livro.")

    def disponiveis(self):
        print("Livros disponiveis:")
        for i in self.acervo:
            if i.disponivel:
                print(i)

if __name__ == "__main__":
    l1 = Livro("a",2000)
    l2 = Livro("b",2000)

    b = Biblioteca()
    b.cadastrar(l2)
    b.cadastrar(l1)

    #Emprestimo
    try:
        b.emprestar("b")
        b.emprestar("b")
    except LivroIndisponivelError as e:
        print(e)

    print("\n")
    #Devolver
    try:
        b.devolver("b")
        b.devolver("b")
    except LivroNaoEncontradoError as e:
        print(e)

    print(l1 == l2)