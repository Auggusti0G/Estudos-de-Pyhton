# --- GRUPO DE ITENS ---

class Item:
    """Classe base para qualquer item do jogo."""
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def obter_detalhes(self):
        return f"{self.nome} (Peso: {self.peso}kg)"


class Arma(Item):
    """Classe que herda de Item e adiciona dano."""
    def __init__(self, nome, peso, dano):
        super().__init__(nome, peso)
        self.dano = dano

    def atacar(self):
        return f"Causou {self.dano} de dano com {self.nome}!"


class Pocao(Item):
    """Classe que herda de Item e adiciona efeito de cura."""
    def __init__(self, nome, peso, cura):
        super().__init__(nome, peso)
        self.cura = cura

    def usar(self):
        return f"Usou {self.nome} e recuperou {self.cura} de vida!"


# --- SISTEMA DE INVENTÁRIO ---

class Inventario:
    """Classe que gerencia os itens de um personagem (Composição)."""
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
        if not self.itens:
            return "Inventário vazio."
        return [item.obter_detalhes() for item in self.itens]


# --- GRUPO DE PERSONAGENS ---

class Personagem:
    """Classe base para todos os personagens do jogo."""
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.inventario = Inventario()  # Uso da classe Inventario

    def mostrar_status(self):
        return f"{self.nome} - Vida: {self.vida}"


class Guerreiro(Personagem):
    """Classe de personagem focada em força."""
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida)
        self.forca = forca

    def habilidade_especial(self):
        return f"{self.nome} usou 'Golpe Esmagador' com força modificada em {self.forca}!"


class Mago(Personagem):
    """Classe de personagem focada em magia."""
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.mana = mana

    def habilidade_especial(self):
        return f"{self.nome} conjurou 'Bola de Fogo' gastando {self.mana} de mana!"


class Arqueiro(Personagem):
    """Classe de personagem focada em agilidade."""
    def __init__(self, nome, vida, precisao):
        super().__init__(nome, vida)
        self.precisao = precisao

    def habilidade_especial(self):
        return f"{self.nome} disparou uma 'Flecha Certeira' com {self.precisao}% de precisão!"


# --- Demonstração do Código funcionando ---
if __name__ == "__main__":
    # 1. Criando instâncias das classes de itens
    espada = Arma("Espada Longa", 4.5, 25)
    pocao_vida = Pocao("Poção Vermelha", 0.5, 50)

    # 2. Criando instâncias das classes de personagens
    guerreiro_arthur = Guerreiro("Arthur", 120, 18)
    mago_merlin = Mago("Merlin", 80, 100)
    arqueiro_robin = Arqueiro("Robin", 95, 90)

    # 3. Interagindo com o Inventário e ações
    guerreiro_arthur.inventario.add_item(espada)
    guerreiro_arthur.inventario.add_item(pocao_vida)

    print(guerreiro_arthur.mostrar_status())
    print("Inventário do Arthur:", guerreiro_arthur.inventario.listar_itens())
    print(espada.atacar())
    print(guerreiro_arthur.habilidade_especial())
    print(mago_merlin.habilidade_especial())
    print(arqueiro_robin.habilidade_especial())