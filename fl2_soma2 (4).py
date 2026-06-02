"""            Comentários de várias linhas     -     Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Meet:     vbc-shqr-wxd

- Problema:
- Crie uma função que receba dois valores e retorne a soma dos valores,
resulva usando função tradicional.

# Exemplo básico – soma de dois números      """
# 1. Função tradicional
def soma(x, y):
    calculo = x + y
    return calculo

if __name__ == '__main__':
    print("Resultado:", soma(2,3))          # Solução 1
    # Resultado: 5
""" --- Alterações:
a. Refaça o main com dois valores digitados pelo usuário.
b. Crie uma função que receba dois valores e retorne a soma dos valores,
resulva usando função lambda.
    --- Dicas:
if __name__ == '__main__':                          # a.
    valor1 = int(input("Valor 1: "))        # Solução 2
    valor2 = int(input("Valor 2: "))
    print("Resultado:", soma(valor1, valor2))
    print("Resultado:", soma(2,3))

- Sintaxe: função lambda equivalente                # b.
# nome_variavel = lambda argumentos : expressão
soma = lambda x, y: x + y
if __name__ == '__main__':
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))
    print("Resultado:", soma(valor1, valor2))
    print("Resultado:", soma(2,3))
    # Resultado: 5

"""
