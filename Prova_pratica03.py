# Prova pratica de python 03 - POO
# Aluno : Rafael Augusto      RA : 22508717

#01 Pense numa entidade para desenvolver uma classe
# -> Entidade escolhida: Livro

class Livro:
    #02 Crie o método construtor com pelo menos quatro atributos (string, float e int)
    def __init__(self, titulo: str, preco: float, ano: int, estoque: int):
        self.__titulo = titulo     # atributo string
        self.__preco = preco       # atributo float
        self.__ano = ano           # atributo int
        self.__estoque = estoque   # atributo int

    #03 Crie os métodos GETs (consultar) de todos os atributos
    def get_titulo(self):
        return self.__titulo

    def get_preco(self):
        return self.__preco

    def get_ano(self):
        return self.__ano

    def get_estoque(self):
        return self.__estoque

    #04 Crie os métodos SETs (alterar) de todos os atributos
    def set_titulo(self, novo_titulo: str):
        self.__titulo = novo_titulo

    def set_preco(self, novo_preco: float):
        self.__preco = novo_preco

    def set_ano(self, novo_ano: int):
        self.__ano = novo_ano

    def set_estoque(self, novo_estoque: int):
        self.__estoque = novo_estoque

    #05 Crie o método mostra_dados1 usando os atributos da classe
    def mostra_dados1(self):
        print("📘 Dados do Livro (modo 1 - atributos diretos):")
        print(f"Título: {self.__titulo}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Ano: {self.__ano}")
        print(f"Estoque: {self.__estoque} unidades")
        print("-" * 40)

    #06 Crie o método mostra_dados2 usando os métodos GET
    def mostra_dados2(self):
        print("📗 Dados do Livro (modo 2 - via GETs):")
        print(f"Título: {self.get_titulo()}")
        print(f"Preço: R$ {self.get_preco():.2f}")
        print(f"Ano: {self.get_ano()}")
        print(f"Estoque: {self.get_estoque()} unidades")
        print("-" * 40)

    #07 Crie o método retorna_dados para retornar todos os atributos
    def retorna_dados(self):
        return (self.__titulo, self.__preco, self.__ano, self.__estoque)

    #08 Crie um método para aumentar o valor numérico de um atributo
    def aumentar_preco(self, valor: float):
        self.__preco += valor
        print(f"💰 O preço do livro '{self.__titulo}' foi aumentado em R$ {valor:.2f}.")
        print(f"Novo preço: R$ {self.__preco:.2f}")
        print("-" * 40)

    #10 Elabore mais um método funcional
    # -> Método extra: aplicar desconto percentual no preço
    def aplicar_desconto(self, percentual: float):
        desconto = (percentual / 100) * self.__preco
        self.__preco -= desconto
        print(f"📉 Desconto de {percentual}% aplicado ao livro '{self.__titulo}'.")
        print(f"Novo preço: R$ {self.__preco:.2f}")
        print("-" * 40)


#11 No método main, crie (instancie) pelo menos quatro objetos e use todos os métodos
def main():
    # Criando objetos da classe Livro
    livro1 = Livro("O Senhor dos Anéis", 120.00, 1954, 10)
    livro2 = Livro("1984", 60.00, 1949, 5)
    livro3 = Livro("Python para Iniciantes", 80.00, 2020, 20)
    livro4 = Livro("Dom Casmurro", 45.00, 1899, 15)

    # Usando os métodos mostra_dados
    livro1.mostra_dados1()
    livro2.mostra_dados2()

    # Retornando dados
    print("🔄 Retorno de dados (livro3):", livro3.retorna_dados())
    print("-" * 40)

    # Alterando atributos com SET
    livro4.set_preco(50.00)
    livro4.mostra_dados1()

    #09 Peça para o usuário fornecer o valor do aumento
    valor_aumento = float(input("Digite o valor de aumento para o livro 1: R$ "))
    livro1.aumentar_preco(valor_aumento)

    # Usando o método funcional extra (desconto)
    livro2.aplicar_desconto(10)  # desconto de 10%


#12 Execução do programa
if __name__ == "__main__":
    main()
