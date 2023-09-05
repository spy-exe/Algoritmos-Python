# 25) Um comerciante comprou um produto e quer vendê-lo com lucro de 5% se 
# o valor da compra for menor que 20,00; caso contrário, o lucro será de 
# 30%. Entrar com o valor do produto e imprimir o valor da venda.

product = float(input('Insira o valor do produto: R$'))

if product < 20:
    novo_valor = product + (product*0.05)
elif product > 20:
    novo_valor = product +(product*0.30)
print(f'Valor do produto: R${product:.2f}\n'
      f'Valor de venda:   R${novo_valor:.2f}\n')