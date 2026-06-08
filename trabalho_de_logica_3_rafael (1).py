#atividade 03 de lógica de programação

#aluno: Rafael Gil         #RA: 22508717

# Problema 1: Leitura de valores reais e cálculo de estatísticas
quantidade = 0
soma = 0
maiores_que_20 = 0

while True:
    valor = float(input("Digite um valor (ou -1 para sair): "))
    if valor == -1:
        break
    quantidade += 1
    soma += valor
    if valor > 20:
        maiores_que_20 += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade de valores digitados: {quantidade}")
    print(f"Soma dos valores digitados: {soma}")
    print(f"Média aritmética: {media:.2f}")
    print(f"Quantidade de valores maiores que 20: {maiores_que_20}")
else:
    print("Nenhum valor foi digitado.")


    # Problema 2: Aprovados e reprovados
    def analisar_notas():
        aprovados = 0
        reprovados = 0
        total_alunos = 0

        while True:
            try:
                nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
                if nota == -1:
                    break
                if nota >= 5:
                    aprovados += 1
                else:
                    reprovados += 1
                total_alunos += 1
            except ValueError:
                print("Por favor, digite uma nota válida.")

        print(f"Quantidade de alunos aprovados: {aprovados}")
        print(f"Quantidade de alunos reprovados: {reprovados}")
        print(f"Quantidade total de alunos: {total_alunos}")

        # Problema 3: Média de pares e ímpares
        def calcular_medias():
            soma_pares = soma_impares = 0
            cont_pares = cont_impares = 0

            while True:
                try:
                    num = int(input("Digite um número (0 para sair): "))
                    if num == 0:
                        break
                    if num % 2 == 0:
                        soma_pares += num
                        cont_pares += 1
                    else:
                        soma_impares += num
                        cont_impares += 1
                except ValueError:
                    print("Por favor, digite um número inteiro válido.")

            media_pares = soma_pares / cont_pares if cont_pares > 0 else 0
            media_impares = soma_impares / cont_impares if cont_impares > 0 else 0

            print(f"Média dos números pares: {media_pares:.2f}")
            print(f"Média dos números ímpares: {media_impares:.2f}")

        # Chamadas de funções (descomente para testar cada uma separadamente)
        # analisar_valores()
        # analisar_notas()
        # calcular_medias()


