# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
# fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
# mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
# aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá
# receber um número indeterminado de entradas, cada uma contendo: 
# um número de identificação do mouse e o tipo de defeito:
# o necessita da esfera;
# o necessita de limpeza; 
# necessita troca do cabo ou conector;
# a.quebrado ou inutilizado Uma identificação
# igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100
# Situação Quantidade Percentual
#
# 1- necessita da esfera 40 40%
# 2- necessita de limpeza 30 30%
# 3- necessita troca do cabo ou conector 15 15%
# 4- quebrado ou inutilizado 15 15%

total = 0
defeito = {
    'Necessita da Esfera': 0,
    'Necessita de Limpeza': 0,
    'Necessita da Troca de Cabo ou Conector': 0,
    'Quebrado ou Inutilizado': 0,
}

while True:
    identification = int(input('Insira a Identificacao do Defeito\n'
                                '1: Necessita da Esfera\n'
                                '2: Necessita de Limpeza\n'
                                '3: Necessita da Troca de Cabo ou Conector\n'
                                '4: Quebrado ou Inutilizado\n\n'
                                '0: Encerra o Programa\n'))
    if identification == 0:
        break
    elif identification == 1:
        defeito['Necessita da Esfera'] += 1
        
    elif identification == 2:
        defeito['Necessita de Limpeza'] += 1
        
    elif identification == 3:
        defeito['Necessita da Troca de Cabo ou Conector'] += 1
        
    elif identification == 4:
        defeito['Quebrado ou Inutilizado'] += 1
        
    else:
        print(f'Numero {identification} invalido!')
        break


    total += 1


# x = defeito * 100 / total

print(f'\nQuantidade de Mouses {total}\n\n'
      f'1 - Necessita da Esfera {defeito["Necessita da Esfera"]} {defeito["Necessita da Esfera"] * 100 / total:.2f}%\n'
      f'2 - Necessita de Limpeza {defeito["Necessita de Limpeza"]} {defeito["Necessita de Limpeza"] * 100 / total:.2f}%\n'
      f'3 - Necessita da Troca de Cabo ou Conector {defeito["Necessita da Troca de Cabo ou Conector"]} {defeito["Necessita da Troca de Cabo ou Conector"] * 100 / total:.2f}%\n'
      f'4 - Quebrado ou Inutilizado {defeito["Quebrado ou Inutilizado"]} {defeito["Quebrado ou Inutilizado"] * 100 / total:.2f}%\n')
    