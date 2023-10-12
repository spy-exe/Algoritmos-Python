# Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
# VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
# carros faz com um litro de combustível. Calcule e mostre:
# . O modelo do carro mais econômico;
# a. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de
# 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo
# segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo.
# Os dados são fictícios e podem mudar a cada execução do programa.
# Comparativo de Consumo de Combustível
# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5
# Relatório Final
# 1 - fusca - 7.0 - 142.9 litros - R$ 321.43
# 2 - gol - 10.0 - 100.0 litros - R$ 225.00
# 3 - uno - 12.5 - 80.0 litros - R$ 180.00
# 4 - vectra - 9.0 - 111.1 litros - R$ 250.00
# 5 - peugeout - 14.5 - 69.0 litros - R$ 155.17
# O menor consumo é do peugeout.

# Define listas para armazenar os modelos de cinco carros e seus respectivos consumos
modelos = []
consumo = []

# Pede entrada para cada modelo de carro e seu consumo
for i in range(5):
    modelo = input(f"Veículo {i+1}\nNome: ")
    km = float(input("Km por litro: "))
    modelos.append(modelo)
    consumo.append(km)

# Calcula o consumo de combustível e o custo para cada carro percorrer 1000 km
consumo_combustivel = [1000 / km for km in consumo]
custo_combustivel = [consumo * 2.25 for consumo in consumo_combustivel]

# Encontra o índice do carro com o menor consumo de combustível
indice_menor_consumo = consumo_combustivel.index(min(consumo_combustivel))

# Imprime o relatório final
print("Comparativo de Consumo de Combustível")
for i in range(5):
    print(f"{i+1} - {modelos[i]} - {consumo[i]} - {consumo_combustivel[i]:.1f} litros - R$ {custo_combustivel[i]:.2f}")
print(f"O menor consumo é do {modelos[indice_menor_consumo]}")