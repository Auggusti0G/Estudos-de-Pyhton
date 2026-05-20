#--------------------------------
#--------Estudos em python-------
#--------------------------------
#Como elabprara um print em python 

mundo = "Hello world"
print("A mensagem será",mundo)

print("hello world")
#Elaborando e estruturando o tipos de dados em python 
#Printando um dado do tio inyeiro 
a = 1 
print(a)
#Printando um dado do tipo real
b = 1.1
print(b)
#Printando um dado do tipo booleano
c = True
print(b)
#Printando um dado do tipo String
c = "rafa"
print(c)

#Printando dados e declarando type xomo uma tipagem 
#tipo de dado inteiro 
a1 = 12
print(type(a1))
#Tipo de dado real
b1 = 23.2
print(type(b1))
#Tipo de dado booleano
c1 = True
print(type(c1))
#Tipo de dado String
d1 = "String"
print(type(d1))

#Dentro da linguagem python temos diferentes formas fomras de fazer um input 
#Tanto quando colocando a arientacao de seus devidos tipos primiticos 

#Fazendo um input e puxando o valor com um F string
a = input("Digite algo")
print(f"Digita foi {a}")

#Elaborando um input com tipo de dado inteiro 
valor_inteiro = int(input("Digite um valor inteiro para mostrar:"))
print("O valor inteiro digitado foi ",valor_inteiro)
#Elaborando um input com o tipo de dado real 
valor_real = float(input("Dugite um valor real para que seja mostrado :"))
print("O valor real digitado foi o ",valor_real)
#Elaborando um input do tipo booleano 
valor_booleano = bool(input("Digite uma sentenca booleana:"))
print("O valor da sentença booleana digitada sera", valor_booleano)
#Elaborando um input do tipo string 
valor_string = str(input("Digite uma stringbpara que seja mostrada:"))
print("O valor da string digitada sera:",valor_string)

#----------------------------------------
# --------Operadores de comparacao------- 
#----------------------------------------

#Dentro de Python temos uma infinidade de operadores os quais sao os
# de comparacao , os de atribuicao , 


vet1 = 20
vet = 20
print(vet1 == vet)

vetorA = 20
vetorb = 90
print(vetorA != vetorb)

casa1 = 30
casa2 = 300
print( casa1 <= casa2)

casa10 = 30
casa20 = 300
print( casa10 >= casa20)

num1 = 20
num2 = 80
print(num1 > num2)


num10 = 20
num20 = 80
print(num10 < num20)

#----------------------------------------
# --------Operadores de Atribuicao------- 
#----------------------------------------

#Operadores de atribuicao
x = 10 
print(x)

y = 20     # y = 90
y += 2     # y = y + 10
print(y)   #print(y)

z = 90
z -= 12
print(z)

w = 20 
w *= 2
print(w)

o = 20
o **= 2
print(o)

f = 90
f /= 2
print(f)

g = 90
g //= 8
print(g)

l = 80
l %= 8
print(l)

#----------------------------------------
# --------Operadores de bites------------ 
#----------------------------------------
# Definindo dois números
vetor_01 = 5   # 101 em binário
vetor_02 = 3   # 011 em binário

print("vetor_01 =", vetor_01, "->", bin(vetor_01))
print("vetor_02 =", vetor_02, "->", bin(vetor_02))
print("-" * 40)

# AND
print("vetor_01 & vetor_02 =", vetor_01 & vetor_02, "->", bin(vetor_01 & vetor_02))

# OR
print("vetor_01 | vetor_02 =", vetor_01 | vetor_02, "->", bin(vetor_01 | vetor_02))

# XOR
print("vetor_01 ^ vetor_02 =", vetor_01 ^ vetor_02, "->", bin(vetor_01 ^ vetor_02))

# NOT
print("~vetor_01 =", ~vetor_01, "->", bin(~vetor_01))

# Shift à esquerda
print("vetor_01 << 1 =", vetor_01 << 1, "->", bin(vetor_01 << 1))

# Shift à direita
print("vetor_01 >> 1 =", vetor_01 >> 1, "->", bin(vetor_01 >> 1))
#----------------------------------------
# --------Operadores de aritmeticos------
#----------------------------------------
#Dentro de python temos varios operadores artitmeticos os quais serapo demostradoas a seguir 

#operador -- ( + )
#operador -- ( - )
#operador -- ( / )
#operador -- ( * )
#operador -- ( ** )
#operador -- ( // )
#operador -- ( %  )

elemento_de_conta_01 = 90
elemento_de_conta_02 = 900
print(elemento_de_conta_01 + elemento_de_conta_02)
print(elemento_de_conta_01 - elemento_de_conta_02)
print(elemento_de_conta_01 / elemento_de_conta_02)
print(elemento_de_conta_01 //  elemento_de_conta_02)
print(elemento_de_conta_01 ** elemento_de_conta_02)
print(elemento_de_conta_01 * elemento_de_conta_02)
print(elemento_de_conta_01 % elemento_de_conta_02)


#----------------------------------------
# --------Operadores de Logicos ---------
#----------------------------------------

#Dentro de Python temos tres operadores logicos em especificos 

#operador -- ( END )
#operador -- ( OR )
#operador -- ( NOT )

#Elaborando um exemplo simples de tabela verdade 
print("-"*50)
print("Tabela verdade em pyhton")
print("-"*50)

# Valores booleanos possíveis
valores = [True, False]

print(f"{'A':<6}{'B':<6}{'AND':<6}{'OR':<6}{'NOT A':<8}{'NOT B':<8}{'XOR (^ )':<10}")
print("-" * 50)

for A in valores:
    for B in valores:
        resultado_and = A and B
        resultado_or = A or B
        resultado_not_a = not A
        resultado_not_b = not B
        resultado_xor = A ^ B

        print(f"{A!s:<6}{B!s:<6}{resultado_and!s:<6}{resultado_or!s:<6}{resultado_not_a!s:<8}{resultado_not_b!s:<8}{resultado_xor!s:<10}")

#Elaborando exemplos mais simples apena com os operador not or and

variavel_01 = True 
variavel_02 = False
print(variavel_01 and variavel_02)

variavel_03 = True 
variavel_04 = False
print(variavel_03 or variavel_04)

variavel_05 = True 
variavel_06 = False
print(not variavel_05 or variavel_06)

# Estruturas de decisão permitem que o programa escolha caminhos 
# diferentes de execução com base em uma condição lógica (True ou False).

# |     if           |
# |     else         |
# |     elif         |
                    
#Estrutura de repticao (decisão simples) -> ( IF )

#Desenvolvendo uma estrutura de Decisao simples
idade = 40 
if idade >= 19:
    print("Voce é maior de idade sua idade é :",idade)
elif idade <= 15:
    print("Voce ainda é muito novo")
elif idade <= 17 :
    print("Voce esta quase la")
else:
    print("Voce é menor de idade")

#----------------------------------------
# --------Tudo sobre funcoes ------------
#----------------------------------------

#Desenvolvendo funcoes em python

#Estabelecendo uma Funcao de saudacao
def saudacao(nome):
    print('Ola é um prazer te conhecer',nome)
resultado = saudacao("rafael")

def sauda(nome):
    return "Ola é um prazer" + nome
resultante = sauda(" Rafa")
print(resultante)

def somadora(a,b):
    return a + b
resultado_soma01 = somadora(12,12)
print("A soma dos dois valores sera:", resultado_soma01)

def sumitrair(a,b,c):
    return a - b - c
resultado_subtracao = sumitrair(12,12,233)
print("o resultado da subiracao sera o seguinte",resultado_subtracao)

def multiplicacao(a,b,c,d):
    return a * b * c * d
resultado_multi = multiplicacao(12,21,21,2,)
print("o resultado da multiplucao sera",resultado_multi)

#Comparando o maximo valor entre tres numero com o def 
def maior_valor(a,b,c):
    if a >= b and b >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
resultado_maior = maior_valor(12,122,3232)
print("O maior dentr o valores sera",resultado_maior)

#Desenvolver

#Elaborando a media de 3 numeros 
a5 = float(input("Digite o valor: "))
b5 = float(input("Digite outro: "))
c5 = float(input("Digite outro valor: "))

def media_dos_tres():
    return (a5 + b5 + c5) / 3
print(media_dos_tres())

z0 = int(input("Digite um valor inteiro:"))
y0 = int(input("Digite um valor inteiro:"))
w0 = int(input("Digite um valor inteiro:"))
q0 = int(input("Digite um valor inteiro:"))
def media_quatro():
    return (z0 + y0 + w0 + q0)/4
print(media_quatro())

#   Comparanndo o maior entre dois numeros 
def maior_dois(a,b):
    if a > b:
        return a
    elif a <= b :
        return "Erro"
    else:
        return a
resultado = (maior_dois(12,21))
print(resultado)

#Comfirir se um numero é par ou impar 
n = int(input("Digite um valor inteiro:"))
def par_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "impar"
print("O numero digitdo é",par_impar(n))


#Calculando a soma de uma lista com a lista fora da funcao 
lista = [ 1 , 2 , 3, 4]
def soma_lista(lista):
    somador = 0
    for num in lista :
        somador += num
    return somador 
print("O resultado é ",soma_lista(lista))

a = int(input("Digite um numero inteiro"))
b = int(input("Digite um outro numero inteiro"))
def calculadora(a,b):
    op2 = input("qual conta sera:")
    if op2 == "+":
        return a + b
    elif op2 == "-":
        return a - b 
    elif op2 == "/":
        return a / b
    elif op2 == "*":
        return a * b
    elif op2 == "**":
        return a ** b 
    elif op2 == "//":
        return a // b 
    else:
        return "numeros igual a zer erro"
print(calculadora(a,b))

#Elaborando um numero que conta as vogais de uma palavra 
def quanridade_vogais(texto_01):
    vogais = "aeiouAEIOU"
    contador = 0 
    for letras in texto_01:
        if letras in vogais :
            contador = contador + 1
    return contador 
resultado =(quanridade_vogais("Palavra"))
print("O resultado sera ",resultado)

texto_palavra = str(input("Digite uma string:"))
def quantidade_vogais(texto_palavra):
    vogais = "aeiouAEIOU"
    contador = 0 
    for letras in texto_palavra:
        if letras in vogais :
            contador = contador + 1
    return contador 
print(quantidade_vogais(texto_palavra))

lista_01 = [1 , 2  ,3 ,4 ]
def soma_lista(lista_01):
    somadors = 0
    for num in lista_01:
        somadors = soma + num
    return somadors
resultado = soma_lista(lista_01)
print("O resultado da soma sera",resultado)

#Elaborando um codigo que soma todos os elementos de uma lsita solicitando a quantidade e os valores
quantidade = int(input("Digite a quantidade de elementos :"))
lista_elementos = []
for i in range (quantidade):
    valor_elementos = int(input("Digite cada elemento da lista:"))
    lista_elementos.append(valor_elementos)
def soma_lista_completa(lista_elementos):
    soma = 0 
    for num in lista_elementos:
        soma += num
    return soma 
resultado = soma_lista_completa(lista_elementos)
print("A soma de todos os valores da lista sera:",resultado)

#Elaborando uma funcao que calculao fatorial de maneira simples
def funcao_fatorial(n):
    resultado = 1 
    for i in range (1, n + 1):
        resultado *= i 
    return resultado
print(funcao_fatorial(5))

def tabuada(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
tabuada(7)

def inverter_lista(lista):
    return lista[::-1]

print(inverter_lista([1,2,3,4]))

def maior_lista(lista):
    maior = lista[0]

    for num in lista:
        if num > maior:
            maior = num

    return maior

print(maior_lista([3,8,2,10,5]))

def maior_lista(lista):
    return max(lista)

print(maior_lista([3,8,2,10,5]))

#---------------------------------------------------------
# --------Tudo sobre Estruturas de repetiçoes ------------
#---------------------------------------------------------

#Oque são estruturas de reptição ?

#São estruturas que possuem a capacidade de automatizar 
#tarefas repetitias dentro de agoritmos 

#|    sintaxe   |
#|              |
#|     while    |
#|      for     |

# { WHILE } --> Executa um bloc de codigo enquando uma 
# condição for verdadeira 

#Exemplo de um contador simples em while 
 
#maneira de escrever usando operadores aritimeticos 

#Iniciando uma estrutura de repticao em While
i = 0
while i <=10:
    print(i)
    i += 1

i = 0 
while i > 0:
    print("Seguencia",i)
    i += 1

i = 1 
while i > 10:
    print(i)
    i+=2

i = 0
while i <= 10:
    print(i)
    i+= 2

soma = 0 
contador = 0 
while True :
    notas = float(input("Digite a quantidade de notas:"))
    if notas == 0 :
        break
    soma += notas
    contador += 1
if contador == 0:
    print("O contador é nulo")
else:
    media = soma / contador
    print(f"A media das notas sera:{media}")

#------------------------------------------------
#----Elaborado estruturas de repticao com for----
#------------------------------------------------

#Para cada valor ddentro deum intervalo x execute 
for i in range(1 ,11):
    print(" Numero", i)

for i in range(0 ,11,2):
    print(i)

for i in range(1,10, 2):
    print(i)

somador = 0 
contadore = 0 
quantidade = int(input("Digite a quantidade de notas:"))
for i in range(quantidade):
    notas1 = float(input("Digite as notas em questao:"))
    if notas1 == 0:
        break
    somador = somador + notas
    contadore = contadore + 1
if contadore == 0:
    print("O ciontador é nulo")
else:
    media_aritmetica = somador / contadore
    print("A media aritmetica sera",media_aritmetica)

#-------------------------------------
#-------Referente a Listas------------
#-------------------------------------

# Uma lista (list) em Python é uma estrutura de dados ordenada, mutável e 
# indexada usada para armazenar múltiplos valores em uma única variável.

#Por exemplo em vez de escrevermos o codigo assim
a = 1
b = 2
c = 3
d = 4
#Podemos escrever de uma outra meneira
lista_exemplo = [ 1 , 2 , 3, 4]
#Lista pode ter mais de um tipo de elemneto 
#Ou sej as listas podem conter multiplos tipo de dados 
lista_mista = [True, False , 20, 20.3, "rafa"]
print(lista_mista)
#Listas e seus indices 
lista_abc = [ "a" , "b" , "c" , "d"]
print(lista_abc[0])

lista_abc = [ "a" , "b" , "c" , "d"]
print(lista_abc[-1])

lista_abc = [ "a" , "b" , "c" , "d"]
print(lista_abc[1])

lista_abdc = ["a","b","c","d","y"]
print(lista_abdc[3])

#Elaborando o indice negativo 
lista_abdc = ["a","b","c","d","y"]
print(lista_abdc[-2])

# ------------------------------------
#------- Criando uma lista -----------
#-------------------------------------

lista = [1, 2, 3]

lista = []

lista_nova = list((1,2,3))
print(lista_nova)

# | Método    | Função                       |
# | --------- | ---------------------------- |
# | append()  | adiciona elemento            |
# | extend()  | adiciona vários elementos    |
# | insert()  | insere em posição específica |
# | remove()  | remove valor                 |
# | pop()     | remove por índice            |
# | clear()   | limpa lista                  |
# | index()   | retorna posição              |
# | count()   | conta ocorrências            |
# | sort()    | ordena lista                 |
# | reverse() | inverte lista                |
# | copy()    | copia lista                  |

lista_adiciona_começo = [ 1, 2 ,3 ,4 ,5]
lista_adiciona_começo.append(12)
print(lista_adiciona_começo)

lista_varios = ["a","b","c","d"]
lista_varios.extend([1,3,4,56,6])
print("Os novos elementos da lista serao :",lista_varios)

lista_remove = [ 1, 2 ,3 ,3 ,4 ,5]
lista_remove.remove(1)
print(lista_remove)

lista_todos_fora = [ 12, 12, 2, 3 ,4 ,5]
lista_todos_fora.clear()
print("a lista sera", lista_todos_fora)

lista_insert = [ 12 , 12 , 23 , 23 ,233]
lista_insert.insert(4, 89)
print(lista_insert)

lista_pop = [ 90 , 12 , 23 , 23 ,33 ,2 ,1]
lista_pop.pop(0)
print("Remove pelo indice",lista_pop)

lista_posicao = [ 10 , 19 , 12 ,12 ]
print(lista_posicao.index(10))

lista_contagem = [11,11,11,1,1,1,1,12,2,22]
a = lista_contagem.count(1)
print("Quantas vezes",a)

lista_ordenagem = [ 5,4,3,2,1,3,4,5]
alinha = lista_ordenagem.sort()
print("A lista ordenada fica :", alinha)

lista_ord = [ 5,4,3,2,1]
lista_ord.sort()
print(lista_ord)

lista_invertida = [ 12 ,2 ,3 ,3 , 4 ,5]
lista.reverse()
print(lista_invertida)

lista_fonte = [1,2,3]
lista_copiada = lista_fonte.copy()
print(lista_copiada)

#. Funções built-in usadas com listas
# Estas não são métodos, mas funcionam com listas.

# | Função   | Função              |
# | -------- | ------------------- |
# | len()    | tamanho             |
# | max()    | maior valor         |
# | min()    | menor valor         |
# | sum()    | soma valores        |
# | sorted() | ordena              |
# | any()    | verifica True       |
# | all()    | verifica todos True |

lista_tamanho = [ 1, 2, 3, 4, 5,5]
print(len(lista_tamanho))

lista_max = [12 , 23, 23 ,236]
print(max(lista_max))

soma_todos_elementos = [ 12 , 23 ,23 ,23 ,8]
a = sum(soma_todos_elementos)
print("A soma de sodos os elementos da lista é",a)

lista = [10,20,30]
for numero in lista:
    print(numero)

lista_min = [1, 2, 3 ,4]
a = min(lista_min)
print(a)

lista_min = [1, 2, 3 ,4]
a = sorted(lista_min)
print(a)

lista_min = [1, 2, 3 ,4]
a = any(lista_min)
print(a)

lista_min = [1, 2, 3 ,4]
a = all(lista_min)
print(a)

# 2. Operadores Unários

z = -5.7

print(abs(z))           # Valor absoluto: 5.7
print(int(z))           # Converte para inteiro: -5 (trunca as casas decimais)
print(float(10))        # Converte para float: 10.0

# Nota: O tipo long(x) existia no Python 2. 
# No Python 3, todos os inteiros são 'long' por padrão.

# 4. Números Complexos e Potenciação

# Complexo: parte real 2 e imaginária 3 (2 + 3j)
c = complex(2, 3)
print(c)

# Potenciação (ambos resultam em 100)
print(10 ** 2)          # Operador
print(pow(10, 2))       # Função

#-------------------------------------
#---Operadores Relacionais------------
#-------------------------------------

# 1. Comparadores de Magnitude
a = 10
b = 20

print(a < b)   # Menor que: True
print(a <= 10) # Menor ou igual: True
print(a > b)   # Maior que: False
print(b >= 20) # Maior ou igual: True

# 2. Comparadores de Igualdade e Diferença
x = 5
y = 8

print(x == 5)  # Igual a: True
print(x != y)  # Diferente de: True

# Nota: O operador <> era usado no Python 2 como sinônimo de !=
# No Python 3 moderno, ele gera um erro de sintaxe.

# 3. Operadores de Identidade (is e is not)
# Diferente do == (que olha o valor), esses operadores
# verificam se dois nomes apontam para o mesmo objeto na memória.
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a

# Comparação de VALOR
print(lista_a == lista_b) # True (os números dentro são iguais)

# Comparação de IDENTIDADE (Objeto)
print(lista_a is lista_b)     # False (são duas listas diferentes em gavetas diferentes da memória)
print(lista_a is lista_c)     # True (lista_c é apenas um apelido para a lista_a)
print(lista_a is not lista_b) # True (confirma que não são o mesmo objeto)

#-----------------------------------------
#------ELABORANDO OS ESTUDOS DE ARRAYS----
#-----------------------------------------

# 1. O que é um Array em Python
# Um array é uma estrutura de dados usada para armazenar múltiplos valores do mesmo tipo em sequência na memória.

# Características principais:

# armazena elementos do mesmo tipo
# ocupa memória contígua
# permite acesso por índice
# geralmente é mais eficiente em memória que listas

# Exemplo conceitual:

# Índice:   0   1   2   3
# Array:   [10, 20, 30, 40]

# 4. Código de tipo (type code)
# Quando criamos um array precisamos informar o tipo de dado.

# | Código | Tipo             |
# | ------ | ---------------- |
# | b      | inteiro pequeno  |
# | B      | inteiro positivo |
# | i      | inteiro          |
# | I      | inteiro positivo |
# | f      | float            |
# | d      | double           |

import array 
numeros = array.array("i",[1,2,3,4,5])
print(numeros)
# array('i', [1, 2, 3, 4, 5])
numeros_f = array.array('f', [1.2, 2.3, 3.4])
print(numeros_f)

# Acessando elementos
import array
a = array.array('i',[10,20,30,40])
print(a[0])
print(a[2])
#Percorrendo um array
import array
a = array.array('i',[1,2,3,4])
for numero in a:
    print(numero)
#Alterando elementos
import array
a = array.array('i',[10,20,30])
a[1] = 99
print(a)

# 8. Métodos dos arrays
# Principais métodos:
# | Método        | Função             |
# | ------------- | ------------------ |
# | append()      | adiciona elemento  |
# | extend()      | adiciona vários    |
# | insert()      | insere em posição  |
# | remove()      | remove elemento    |
# | pop()         | remove pelo índice |
# | index()       | retorna posição    |
# | reverse()     | inverte array      |
# | buffer_info() | info da memória    |

# 19. Diferença entre List e Array
# | Característica    | List | Array |
# | ----------------- | ---- | ----- |
# | tipos diferentes  | sim  | não   |
# | mais flexível     | sim  | não   |
# | memória eficiente | não  | sim   |
# | padrão Python     | sim  | não   |

#------------------------------------
#-----------MATRIZES-----------------  
#------------------------------------

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

resultado = [[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            resultado[i][j] += A[i][k] * B[k][j]

print(resultado)




