"""            Comentários de várias linhas - Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Programa:

- Projete um programa com duas funções:
A função principal (main) e a função calcula idade.

- Implemente a função (def) que calcula idade de uma pessoa. Ela recebe
o ano de nascimento de uma pessoa como parâmetro (valor), faz o cálculo
da idade e retorna a idade.

- A função principal (main) lê o ano de nascimento digitado pelo usuário,
chama a função calcula idade passando o argumento (valor lido) e mostra o
valor retornado pela função calcula idade.  """

def calcula_idade(ano_nascimento):  # Recebe o parâmetro (ano de nascimento)
    ano_atual = 2025  # Ano atual
    idade = ano_atual - ano_nascimento  # Calcula
    return idade                        # Retorna a idade

if __name__ == '__main__':
    # Leitura do ano de nascimento
    ano = int(input("Digite o ano de nascimento: "))
    v_idade = calcula_idade(ano)        # Chamada da função calcula_idade
    print("Idade da pessoa:", v_idade)
""" --- ALTERAÇÕES:
a. Na tela de saída, mostre também a ano de nascimento. 
b. No início do programa, leia também  o nome da pessoa. 
c. E no final, na tela de saida, mostre também o nome da pessoa.
d. Refaça, pegando o ano atual usando biblioteca do Python. 
    --- DICAS:
print("Ano de nascimento:", ano_nascimento)             # a.
nome = str(input("Nome: "))  # Lê string                # b.
nome = input("Nome: ")       # Lê string          
# Obs.: as duas linhas acima são equivalentes  
...                                                     # c.
print("Nome:", nome)
---
from datetime import date                               # d
def calcula_idade(ano_nascimento):      # Recebe o parâmetro (ano de nascimento)
    ano_atual = date.today().year       # ano_atual = 2025
    idade = ano_atual - ano_nascimento
    return idade                        # Retorna a idade

"""
