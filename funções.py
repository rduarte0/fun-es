import os
os.system("cls || clear")

 # Solicitando dados do usuário
numeros = []
for i in range(5):
    num = int(input(f"Informe o {i + 1}º número: "))
    numeros.append(num)


# Definindo valores das váriaveis
def calcular_estatisticas(numeros):
    quantidade_pares = 0
    quantidade_impares = 0
    quantidade_positivos = 0
    quantidade_negativos = 0
    soma_pares = 0
    soma_impares = 0
    soma_geral = 0
    maior_numero = float('-inf')
    menor_numero = float('inf')

    for numero in numeros:
        soma_geral += numero

        # Definindo pares e ímpares
        if numero % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero
        else:
            quantidade_impares += 1
            soma_impares += numero

        # Definindo positivos e negativos
        if numero < 0:
            quantidade_negativos += 1
        elif numero > 0:
            quantidade_positivos += 1

        # Definindo maior e menor número
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    # Calculando as médias
    media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
    media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
    media_geral = soma_geral / len(numeros)

    # Retornar os valores
    return {
        "quantidade_pares": quantidade_pares,
        "quantidade_impares": quantidade_impares,
        "quantidade_positivos": quantidade_positivos,
        "quantidade_negativos": quantidade_negativos,
        "soma_pares": soma_pares,
        "soma_impares": soma_impares,
        "soma_geral": soma_geral,
        "maior_numero": maior_numero,
        "menor_numero": menor_numero,
        "media_pares": media_pares,
        "media_impares": media_impares,
        "media_geral": media_geral
    }

# Exibindo numeros em ordem inversa
def exibir_ordem_inversa(numeros):
    print("\n=== Exibindo ordem inversa ===")
    for i, numero in enumerate(reversed(numeros)):
        print(f"{i + 1}º - {numero}")

# Exibindo dados
def exibir_estatisticas(estatisticas):
    print("\nEstatísticas dos números:")
    print(f"Quantidade de pares: {estatisticas['quantidade_pares']}")
    print(f"Quantidade de ímpares: {estatisticas['quantidade_impares']}")
    print(f"Quantidade de positivos: {estatisticas['quantidade_positivos']}")
    print(f"Quantidade de negativos: {estatisticas['quantidade_negativos']}")
    print(f"Maior número: {estatisticas['maior_numero']}")
    print(f"Menor número: {estatisticas['menor_numero']}")
    print(f"Média dos números pares: {estatisticas['media_pares']:.2f}")
    print(f"Média dos números ímpares: {estatisticas['media_impares']:.2f}")
    print(f"Média de todos os números: {estatisticas['media_geral']:.2f}")


estatisticas = calcular_estatisticas(numeros)
exibir_ordem_inversa(numeros)
exibir_estatisticas(estatisticas)