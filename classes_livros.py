class Livro:
    """Classe que representa um livro individual."""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"


class Membro:
    """Classe que representa um usuário da biblioteca."""
    def __init__(self, nome, id_membro):
        self.nome = nome
        self.id_membro = id_membro
        # LISTA: Guarda os objetos da classe Livro que este membro pegou
        self.historico_emprestimos = [] 

    def pegar_livro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.historico_emprestimos.append(livro) # Adiciona à lista
            print(f"-> {self.nome} pegou o livro '{livro.titulo}' emprestado.")
        else:
            print(f"-> Desculpe {self.nome}, o livro '{livro.titulo}' já está ocupado!")

    def listar_meus_livros(self):
        print(f"\nLivros com {self.nome}:")
        if not self.historico_emprestimos:
            print("Nenhum livro emprestado no momento.")
        for livro in self.historico_emprestimos:
            print(f"- {livro.titulo}")


class Biblioteca:
    """Classe principal que gerencia o fluxo usando listas."""
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []  # LISTA: Armazenará objetos da classe Livro
        self.membros = []   # LISTA: Armazenará objetos da classe Membro

    def cadastrar_livro(self, livro):
        self.catalogo.append(livro) # Adiciona o objeto Livro à lista

    def registrar_membro(self, membro):
        self.membros.append(membro) # Adiciona o objeto Membro à lista

    def mostrar_catalogo(self):
        print(f"\n--- Catálogo da Biblioteca {self.nome} ---")
        # Iterando pela lista de objetos
        for livro in self.catalogo:
            print(livro) 


# --- Executando e Testando o Sistema ---
if __name__ == "__main__":
    # 1. Instanciando a Biblioteca
    minha_biblioteca = Biblioteca("Central de Python")

    # 2. Criando objetos da classe Livro e adicionando na lista da Biblioteca
    livro1 = Livro("O Hobbit", "J.R.R. Tolkien")
    livro2 = Livro("1984", "George Orwell")
    livro3 = Livro("Python Fluente", "Luciano Ramalho")

    minha_biblioteca.cadastrar_livro(livro1)
    minha_biblioteca.cadastrar_livro(livro2)
    minha_biblioteca.cadastrar_livro(livro3)

    # 3. Criando objetos da classe Membro e registrando na lista da Biblioteca
    usuario_joao = Membro("João Silva", 101)
    usuario_maria = Membro("Maria Souza", 102)

    minha_biblioteca.registrar_membro(usuario_joao)
    minha_biblioteca.registrar_membro(usuario_maria)

    # 4. Mostrando o catálogo inicial
    minha_biblioteca.mostrar_catalogo()

    # 5. Movimentando os livros (Interação entre Classes e Listas)
    print("\n--- Movimentações ---")
    usuario_joao.pegar_livro(livro3) # João pega Python Fluente
    usuario_maria.pegar_livro(livro3) # Maria tenta pegar o mesmo livro

    # 6. Ver