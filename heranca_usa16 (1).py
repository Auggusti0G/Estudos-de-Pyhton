# Sintaxe:
# from nome_arquivo_sem_extensao import NomeClasse1, NomeClasse2
from heranca_classes16 import Funcionario, Gerente
if __name__ == '__main__':              # Atalho: mai <tab>
    f1 = Funcionario('Paulo', 1000.00)  # Cria o objeto, chama o construtor
    print(f1)                           # print(f1.__str__())
    # <__main__.Funcionario object at 0x00000159D5FFB2C8>
    f2 = Funcionario('Ana', 2000.00)  # Cria o objeto, chama o construtor
    print(f2)                # print(f1.__str__())      # Teste
    print(f'- Funcionário 1:\nNome: {f1.get_nome()}')   # Consulta
    print('Salário:', f1.get_salario())
    f1.set_nome('Vinícius')                             # Altera
    print(f'Nome alterado: {f1.get_nome()}')
    print(f'- Funcionário 2:\nNome: {f2.get_nome()}')
    print('Salário:', f2.get_salario())
    f2.set_nome('Emily')
    print(f'Nome alterado: {f2.get_nome()}')
    g1 = Gerente('Paula', 3000.0, 5)  # g1, objeto da classe Gerente
    print(g1)                         # print(g1.__str__()) # Teste
    # <heranca0_gerente.Gerente object at 0x000001C23ECFB0A0>
    g2 = Gerente('Paulo', 5000.0, 2)
    print(g2)
    print('- Gerente 1:\nNome:', g1.get_nome())
    print('Salário:', g1.get_salario())
    g1.set_nome('Alice')
    print(f'Nome alterado: {g1.get_nome()}')
    print('- Gerente 2:\nNome:', g2.get_nome())
    print('Salário:', g2.get_salario())

    print("Bonus func", f1.bonificacao())
    print("Bonus ger.", g1.bonificacao())

