# 6. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um
# vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma
# função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

results = []

for i in range(100):
    roll = random.randint(1, 6)
    results.append(roll)

counts = [0, 0, 0, 0, 0, 0]

for roll in results:
    counts[roll - 1] += 1

for i in range(6):
    print(f"Número {i+1} foi lançado {counts[i]} vezes.")
