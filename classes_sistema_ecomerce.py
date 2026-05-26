class Produto:
    """Representa um produto físico da loja."""
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (R$ {self.preco:.2f})"


class ItemCarrinho:
    """Classe intermediária que une o Produto à Quantidade escolhida."""
    def __init__(self, produto, quantidade):
        self.produto = produto  # Objeto da classe Produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        # Multiplica o preço do objeto Produto pela quantidade deste item
        return self.produto.preco * self.quantidade


class CarrinhoDeCompras:
    """Gerencia a lista de itens que o cliente quer comprar."""
    def __init__(self):
        self.itens = [] # LISTA: Vai guardar objetos da classe ItemCarrinho

    def adicionar_produto(self, produto, quantidade=1):
        # Lógica com Lista: Verifica se o produto já está no carrinho
        for item in self.itens:
            if item.produto.codigo == produto.codigo:
                item.quantidade += quantidade
                print(f"-> Aumentada a quantidade de '{produto.nome}' para {item.quantidade}.")
                return
        
        # Se for um produto novo, cria o ItemCarrinho e adiciona à lista
        novo_item = ItemCarrinho(produto, quantidade)
        self.itens.append(novo_item)
        print(f"-> '{produto.nome}' adicionado ao carrinho.")

    def remover_produto(self, codigo_produto):
        # Lógica com Lista: Filtra e remove um item pelo código
        for item in self.itens:
            if item.produto.codigo == codigo_produto:
                self.itens.remove(item)
                print(f"-> '{item.produto.nome}' foi removido do carrinho.")
                return
        print("-> Produto não encontrado no carrinho.")

    def calcular_total_carrinho(self):
        # Lógica com Lista: Soma o subtotal de cada objeto da lista
        total = sum(item.calcular_subtotal() for item in self.itens)
        return total

    def exibir_resumo(self):
        print("\n" + "="*35)
        print("        CARRINHO DE COMPRAS        ")
        print("="*35)
        if not self.itens:
            print("Seu carrinho está vazio.")
        else:
            for item in self.itens:
                print(f"{item.produto.nome:<18} | Qtd: {item.quantidade:<2} | Subtotal: R$ {item.calcular_subtotal():.2f}")
            print("-"*35)
            print(f"TOTAL DA COMPRA: R$ {self.calcular_total_carrinho():.2f}")
        print("="*35)


# --- Testando o fluxo do E-commerce ---
if __name__ == "__main__":
    # 1. Criando o catálogo de produtos da loja
    teclado = Produto("A10", "Teclado Mecânico", 250.00)
    mouse = Produto("B20", "Mouse Gamer", 150.00)
    monitor = Produto("C30", "Monitor 144Hz", 1200.00)

    # 2. Inicializando o carrinho do cliente
    meu_carrinho = CarrinhoDeCompras()

    # 3. Adicionando produtos (e testando a repetição do mesmo produto)
    print("--- Adicionando Itens ---")
    meu_carrinho.adicionar_produto(teclado, 1)
    meu_carrinho.adicionar_produto(mouse, 2)
    meu_carrinho.adicionar_produto(teclado, 1) # Deve somar na quantidade do teclado existente

    # 4. Exibindo o carrinho com os valores calculados
    meu_carrinho.exibir_resumo()

    # 5. Removendo um item e adicionando outro mais caro
    print("\n--- Alterando o Carrinho ---")
    meu_carrinho.remover_produto("B20") # Remove o mouse
    meu_carrinho.adicionar_produto(monitor, 1)

    # 6. Resumo final
    meu_carrinho.exibir_resumo()