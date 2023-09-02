# 09) Cálculo de um salário líquido de um professor. Serão fornecidos valor da 
# hora aula, numero de aulas dadas e o % de desconto do INSS.

valor_hora = float(input('Insira o valor da hora aula: '))
aulas = int(input('Insira o valor de aulas dadas: '))
inss = float(input('Insira a % do valor do INSS: '))
inss *= 0.01
sal_liquido = (valor_hora * aulas) - ((valor_hora * aulas) * inss)
print(f'Salário líquido: ${sal_liquido}')