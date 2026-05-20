#------------------------------------------
#-------Conceitos basicos Programação------
#------------------------------------------
#rafa
#como eu faço para printar algo ?

#No python ultilizamos o print
print("hello world")

#Dentro da programacao existem varios tipos de dados 
#Temos varias formas de printar os diferentes tipos de dados 

##Oque sao os tipos primitivos ?
#tipos primitivos sao tipos de dados simples que sao representados da seguinte maneira

#A forma mais simples de printar apenas com o print

#Printadno um tipo de dado inteiro
print(12) #inteiro - int

#Printando um tipo de dado real
print(1,23) #real - float

#Prinatando uma string
print("rafael") #string - str

#Printadno um tipo de dado Booleano
print(True) #Booleano - bool

#Agora é possivel tambem fazer um tipo de print de dados
#Ou seja print dos tipos primitivos com tipagem

#Prinatndo um int com type 
a = 12
print(type(a))
#Printando um Float com type
b = 9.8
print(type(b))
#Printando um bool com tipagem
c = True 
print(type(b))
#Printando uma string com type
c = "Rafael"
print(type(c))

#Bpm dentro de todas as linguagens de programacao temos tambem
# Os inputs e outputs 

#Oque são os inputs e outputs?
#Um input e a entrada de comando eum output sera oe saira

#Criando um input simples em python
#Podemos Fazer os inputs apenas buxando a variavel com um print

#Deste caso o output sera oque sera digitado
a = input("Digite algo:")
print(a)

#Criando um input com o tempo real 
b = float(input("Digite um numero real:"))
print(b)

#Criando um input com int
c = int(input("Digite um valor inteiro:"))
print(c)

#Crinado um input com bool
d = bool(int("Digite uma sentença real:"))
print(e)

#Criando um input com string
e = str(input("Digite uma string:"))
print(e)

#O quando digitamos um input e temos no print um type 
#Retornara o tipo de dado que foi digitado

#Input int com type
a = int(input("Digite um valor inteiro:"))
print(type(a))

#Input com float type
b = float(input("Digite um numero real:"))
print(type(b))

#Criando um input com str e type
c = str(input("Digite um nome:"))
print(type(c))

#tendo visto isso iremos para o basico 

# --------------------------------------
# -----Operadores de COMPARAÇÃO---------
# --------------------------------------

# Usados para comparar valores.
# O resultado sempre é True ou False.

# Operador	      Lê-se	        Significado

# | ==          igual a	            verifica se é igual
# | !=	        diferente de	    verifica se é diferente
# | >	        maior que	        compara tamanho
# | <	        menor que	        compara tamanho
# | >=       	maior ou igual	    maior ou igual
# | <=      	menor ou igual	    menor ou igual


#Exemplo simples usando igual a ( == )
a = 5
b = 5

print(type(a == b))

#Retornara True

#Exemplo simples usando diferente de ( != )

a = 3
c = 1

print(a != c)

#Exemplo simples usando maior que  ( > )

a = 90
c = 23

print(a > c)

#Exemplo simples usando menor que ( < )

a = 20
c = 80

print( a < c )

#Exemplo simples usando maior ou iqual ( >= )
a = 5
b = 5

print(a >= b)

#Exemplo simples usando menor ou iqual ( <= )

a = 3
b = 1

print( a <= b )

#--------------------------------------------
#-------Operadores de ATRIBUIÇÃO-------------
#--------------------------------------------

# Usados para guardar valores em variáveis.

# Operador  	Significado
 
# | =	       atribuição simples
# | +=	       soma e guarda
# | -=	       subtrai e guarda
# | *=	       multiplica e guarda
# | /=	       divide e guarda
# | %=	       resto e guarda

#  atribuição simples ( = )

x = 10
print(x)

#  soma quarda ( += )

x = 12
x += 2

print(x)

# Mesma forma de dizer ao computador

x = 10 
x = x + 4

print(x)

#  menos quarda (-=)

x = 14
x -= 2

print(x)

# Mesma coisa de dizer para o conputador 

x = 10
x = x - 12

print(x)

# multiplica o valor e quarda 

# operacao e quarda o valor msmo espaco memoria

a = 23
a *= 2

print(a)

#Da mesma forma podemos dizer

a = 12
a = a * 2

print(a)


#divide e qualrda (\=)

a = 12
a /= 2

print(a)

#da mesma forma podemos dizer

a = 12
a = a / 2 

print(a)

# resto e guarda 

x = 17
x %= 5

print(x)

#da mesma forma podemos dizer

x = 17
x = x % 5

print(x)

#-----------------------------------------------
#-----Montando a lista de operadores logicos----
#-----------------------------------------------

# Usados para juntar condições.

# | Operador	   Lê-se	  Função              |
# |                                               |
# | and            e	   tudo precisa ser True  |
# | or	           ou	   basta um ser True      |
# | not	           não	   inverte o valor        |

# Operador Logico ( and )
# Nessa condicao logica tudo precisa ser verdadeiro

print( idade >= 18 and ten_carteira)

#tudo sera verdadeiro

#Operador logico ( or )
#nessa condicao logica apenas uma sentensa tem que ser true

a = True
b = False

print( a or b)

#Operador logico ( not )

Ligado = True 
print( not ligado)

#----------------------------------------------
#----------Operadores Aritmetico---------------
#----------------------------------------------

#Simbolo            função

# +                adição
# -                subitracao
# /                divisão
# %                resto div
# *                multiplicação
# **               Pontenciação

#Ultilizando o operador aritmetico +
print(2 + 2)

#Ultilizando o operador aritmetico -
print(2 - 1)

#Ultilizando o operador aritmetico //
#Divisao inteira
print(20 / 2)

#Ultilizando o operador aritmetico /
#Divisao real
print(3 / 2 )

#Ultilizando o operador aritmetico %
print(10 % 4 )

#Ultilizando o operador aritmetico *
print(2 * 2)

#Ultilizando o operador aritmetico **
print(2 ** 8)

#-------------------------------------
#-----Estruturas de decisao-----------
#-------------------------------------

## Oque sao as estruturas de decisão ?

# Estruturas de decisão permitem que o programa escolha caminhos 
# diferentes de execução com base em uma condição lógica (True ou False).

# |     if           |
# |     else         |
# |     elif         |
                    
#Estrutura de repticao (decisão simples) -> ( IF )

#Desenvolvendo uma estrutura de Decisao simples
idade = 40
if idade >= 18:
    print("Voce é maior de idade", idade)
else:
    print("Voce é menor de idade")

#Criando uma estrutura de decisao com if else elif

idade = 18
if idade >= 18:
    print("Voce é maior de idade")
elif idade <= 17:
    print("Voce esta quase la")
else:
    print("Voce é menor de idade")

#Elaborando uma estrutura de decisao
#Estrutura de decisao com input e tipo primitivo
idade = int(input("Digite sua idade:"))
if idade >= 18 :
    print("Você é maior de idade")
elif idade <= 17:
    print("Voce esta quase la")
else:
    print("Voce é menor de idade")

#Desencolvend estrutura de decisao com dois inputs
a = float(input("Digite um valor real:"))
b = float(input("Digite o valor real"))
if a >= b :
    print("O valor maior é",a)
elif a <= b :
    print("O valor maior é", b)
else:
    print("Vaores sao iguais")

#Desenvolvendo estrutura de troca swap
a = int(input("Digite um numero inteiro:"))
b = int(input("Digite um numero inteiro:"))
if a >= b:
    a,b and b,a
print(f"O valores crescente serao: {a}, {b}")
#Opos termos visto todas essas estruturas vamor partir para repticoes

i = 0

i = 1                 #Contagem ira começar de 1
while i <= 10:        #Enquanto i <= 10 print i
    print(i)          #Ação que executa
    i += 1            #A cada rodagem no loop + 1

#Elaborando um while com print de palavra
i = 1 
while i <= 10:
    print("Numero", i)
    i += 1
#Elaborando um While decrescente 
i = 1
while i > 0:
    print(i)
    i -= 1

#Elaborando o while com os impares
i = 1
while i < 10:
    print(i)
    i += 2
#Elaborando o while com pares
i = 0
while i <= 10:
    print(i)
    i += 2
#Elaborando uma media aritmedica com while 
contador = 0     # de onde o contador vai comeca
soma = 0         # de onde a sonma vai partir

while True:    #enquanto uma condicao for verdadeira 
      numero = float(input("Digite as notas :"))
      
      if numero == 0:
        break

      soma += numero
      contador += 1

if contadpor == 0:
    print("Nenhum numero foi digitado")
else:
    media = soma / contador 
    print("Media das notas sera", media)

#------------------------------------------------
#----Elaborado estruturas de repticao com for----
#------------------------------------------------

#Para cada valor ddentro deum intervalo x execute 
for i in range(1,11):   
    print(i)

#Fazendo a mesma estrutura com um print
for i in range(1,11):
    print("Numero",i)

#Fazendo a repticao na ordem decrescente

#for in range(a,b,c)

#Dento dos intervalos 
# inter = { a = inicio, b = fim, c = passo}

for i in range(11,0,-1):  
    print(i)

#Dentro de um loop retornando impar

for i in range(1,10,2):
    print(i)

#Dentro de um loop retorno de pares

for i in range(0, 11, 2):
    print(i)

# media aritmetica com for
contador = 0
soma = 0

quantidade = int(input("Quantos números você deseja digitar? "))

for i in range(quantidade):
    numero = float(input("Digite um número (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    soma += numero
    contador += 1

if contador == 0:
    print("Nenhum número foi digitado.")
else:
    media = soma / contador
    print("Média aritmética =", media)

#Desenvolvendo funcoes em python

#Estabelecendo uma Funcao de saudacao
def saudacao(nome):
    print("Ola é um prazer te conhecer",nome)
resultado = saudacao("Rafael")

#Fazendo uma funcao de saudacao com return
def saudacao(nome):
    return "Olá" + nome
resultado = saudacao("Rafael")
print(resultado)

#Desenvolvendo uma funcao que soma
def soma(a,b):
    return a + b
resultado = soma(12,23)
print(resultado)

#Desenvolvendo uma funcao que retorna o maior valor dentre tres
def maior(a,b,c):
    if a >= b and b >= c:
        return a 
    elif b >= a and b >= c:
        return b
    else:
        return c
resultado = maior(122,32,344)
print("O maior valor dentro os tres sera :",resultado)

#Fazendo media com uma funcao while 
def media_while():
    contador = 0
    soma = 0

    while True:
        numero = float(input("Digite um número (ou 0 para sair): "))

        if numero == 0:
            break

        soma += numero
        contador += 1

    if contador == 0:
        print("Nenhum número foi digitado.")
    else:
        media = soma / contador
        print("Média aritmética =", media)
media_while()

#Fazendo uma funcao de media aritmedica for 
def media_for():
    contador = 0
    soma = 0

    quantidade = int(input("Quantos números você deseja digitar? "))

    for i in range(quantidade):
        numero = float(input("Digite um número (ou 0 para sair): "))

        if numero == 0:
            break

        soma += numero
        contador += 1

    if contador == 0:
        print("Nenhum número foi digitado.")
    else:
        media = soma / contador
        print("Média aritmética =", media)

#------------------------------------
#---------Elaborando listas----------
#------------------------------------

#Oque são listas em Python?
#estrutura de dados que armazena vários valores dentro de uma única variável

#Definicao da programacao 

#Listas em programação são estruturas de dados lineares que permitem armazenar, organizar e manipular uma coleção de elementos (dados) 
#em uma única variável. Elas são ordenadas, geralmente indexadas (começando pelo índice 0) e possuem tamanho dinâmico, podendo crescer ou diminuir conforme a necessidade

#Em vez de criarmos varias variaveis assim 
n1 = 10
n2 = 90
n3 = 12
#Podemos apenas construir da seguinte forma 

#Agora a variavel numero quarda varios dados
numeros = [10, 90, 12]

#Existem varios tipos de listas 

#Listas ordenadas 
lista_ordenada = [10, 20, 30]
#com os prints podemos devolver a posicao de um elemento na lista 
print(lista_ordenada[0])
print(lista_ordenada[1])
print(lista_ordenada[2])

#Listas mutaveis 

#Mudar um elemento da lista 
lista[1] = 99
print(lista)

#listas dinamicas crescem e diminuem
lista = [12,23,34,46]
lista.append(40)

# ✔️ Aceitam vários tipos de dados:
lista = [10, "Python", True, 3.14]

#Montando a estrutura de uma lista

#--------------------------------
#   lista = [ a, b , c, d ]
#--------------------------------

#Cada letra dentro dessa estrutrura representa um elemento da lista
#Ou seja uma representacao simples

#se temos os seguintes daddos 

#    A = 10
#    B = 20
#    C = 30

#Juntando eles numa lista ficara assim

#lista_ABC = [10 , 20 , 30]
#chamando os elementos da lista
#print(lista_ABC(0)) primeiro elemento zero

#ou apenas a sintaxe 

# lista = [ a, b , c]
# print(lista[0])
# print(lista[1])

# 🔷 Estrutura de uma Lista
nome_da_lista = [elemento1, elemento2, elemento3]
# Exemplo 
notas = [7.5, 8.0, 9.2]

#Tendo visto essa Teória primeiro vamos avancar

#-------------------------------------------------
#-------Funções Built-in e Métodos de Lista------
#-------------------------------------------------

# Funções Built-in (funções nativas)
# São funções que já existem no Python e funcionam com listas

#São elas as seguintes 

#--------------------------------
#  |  len()     Retorna o tamanho da lista
#  |  max()     Maior valor
#  |  min()     Menor valor
#  |  sum()     Soma dos elementos
#  |  sorted()  Ordena a lista (sem alterar a original)
#-----------------------------



#-----------------------------------------
#----Métodos de Lista (List Methods)------
#-----------------------------------------

# São funções que pertencem à própria lista.

# Ex:

# |   append() 
# |   insert()
# |   remove()
# |   pop()
#------------------------

#Conferindo o tamanho de uma lista 
lista_tamanho = [ 90 , 34 ,394 ,3434]
print(len(lista_tamanho))
#Retornando o valor maximo da lista 
lista_maximo = [ 23, 34,433, 4545]
print(max(lista_maximo))
#Retornando o menor valor da lista 
lista_menor = [ 90 , 92, 877, 2232]
print(min(lista_menor))
#Somando todos os elementos de uma lista 
lista_somando = [ 1, 2 , 3 , 4 ,45]
print(sum(lista_somando))

#   Elaborando os meytados de lista

#Ordenando a lista sem alterala (sorted)
lista = [67,67676,12,23,34,45,45]
print(sorted(lista))
#Ordenando de maneira decrescente 
lista_sorted_decrescente = [ 23, 34 ,343 ,34343,45655]
print(sorted(lista, reverse = True))

#Transfomando algo em lista 
lista = list("python")
print(lista)

#Conferi se existe um valor verdadeiro na lista 
lista = [0, 0, 1, 0]
print(any(lista))

#   Conferi se todos os elementos sao verdadeiro se sim retorna true 
lista = [1, 0, 1, 1, 1]
print(all(lista))


#Percorrera a lista e retornara os elementos e seus indices 
lista = [ 10, 20 , 39 ]
for i, v in enumerate(lista):
    print(i, v)

#Ultilizando a funcao zip para juntar duas listas 
lista_alfa = [1,2,3,4]
lista_beta = [23,13,45,43]
print(list(zip(lista_alfa, lista_beta)))

#-----------------------------------------
#-------Metados de lista em Python--------
#-----------------------------------------

#Adiciona um valor ao final da lista 
lista = [ 12 , 23 , 34 , 38 , 45]
lista.append(130)
print(lista)

#Adicionara um valor apos o outro 
lista = [ 1 , 2 , 3 ,4 ,5]
lista.insert(3, 29)
print("O resuktado da lista é ",lista)

#Retirando um termo da lista o primeiro respectivo 
lista = [1 , 3 , 4 ,5 , 5]
lista.remove(5)
print(5)

# rediradnpo pelo indice funcao pop
lista = [23 , 34 ,35 ,45 ,56]   #Valores da lista 
lista.pop(0)                    # Removendo pelo indice 
print(lista)                    #Print a lista 

#Usando uma funcao clear para limpar uma lista 
lista = [12, 23, 34 ,45,46]
lista.clear()
print(lista)

#Retornando o index ou seja a posicao de uma elevemnto 
lista = [ 12 , 24 ,34 ,345 ,343,34333, 45 ,455,56665, 56]
print(lista.index(34))

#Atraves da funcao do count vamos ver quantas vezes um elemnto aparece numa lista
lista = [89, 34 ,2, 2, 2,2,2,2, 344 ,121, 788,23]
print(lista.count(2))

#Ordenadno uma lista de maneira crescente 
lista = [ 12 , 23 ,34 ,33, 3 ,2 ,56]
lista.sort()
print(lista)

#Ordenando uma lista de maneira descrecente 
lista = [23, 35, 45, 67, 56]
lista.sort(reverse=True)

print(lista)

#Com a funcao reverse invert a ordem dos elementos da lista 
lista = [ 12, 23, 233]
lista.reverse()
print(lista)

#Criando duas listas diferentes que sao compostas pelo mesmos elementos 
lista = [12, 23, 345, 3554]
nova = lista.copy()

print(lista)
print(nova)

#Usando a funcao extend para unir duas listas 
lista_1 = [23, 23, 34, 344]
lista_2 = [12, 83, 334, 34334]

lista_1.extend(lista_2)

