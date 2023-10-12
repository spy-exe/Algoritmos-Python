# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
# organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"
# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da
# mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não
# deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções
# devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá
# calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado
# pela empresa, e é o seguinte:
# Sistema Operacional Votos %
# ------------------- ----- ---
# Windows Server 1500 17%
# Unix 3500 40%
# Linux 3000 34%
# Netware 500 5%
# Mac OS 150 2%
# Outro 150 2%
# ------------------- -----
# Total 8800
# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo
# a 40% dos votos.

votos = { # Criando um dicionario com os sistemas operacionais - Melhor manipulacao de dados durante o codigo.
    'Windows Server': 0,
    'Unix': 0,
    'Linux': 0,
    'Netware': 0,
    'MacOS': 0,
    'Outro': 0
}

while True:
    voto = int(input('Qual o melhor S.O. para uso em servidores?\n=> '))
    if voto == 0: # Se o voto for = 0, encerrar programa
        break
    elif voto > 6 or voto < 0: # Se o voto for maior que 6 ou menor que 0 = Voto Invalido
        print('Voto inválido, tente novamente.')
        continue
    else:
        if voto == 1: # Se o voto for igual a 1 = Windows Server
            votos['Windows Server'] += 1
        elif voto == 2:
            votos['Unix'] += 1 
        elif voto == 3:
            votos['Linux'] += 1
        elif voto == 4:
            votos['Netware'] += 1
        elif voto == 5:
            votos['MacOS'] += 1
        elif voto == 6:
            votos['Outro'] += 1

total = sum(votos.values())     # Numero total de votos.

# Resultado da enquete
print("Sistema Operacional   Votos   %")
print("-------------------   -----   ---")
for sistema, voto in votos.items():
    percentual = (voto / total) * 100
    print(f"{sistema:20} {voto:6} {percentual:.1f}%")
print("-------------------   -----")
print(f"Total                {total}")

# S.O. vencedor da enquete
vencedor = max(votos.items(), key=lambda x: x[1])[0]
print(f"O S.O. mais votado foi o {vencedor}, com {votos[vencedor]} votos, correspondendo a {votos[vencedor] * 100 / total:1f}% dos votos.\n")