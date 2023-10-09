# 07) Informar um saldo e imprimir o saldo com reajuste de 1%
saldo = float(input('Insira seu saldo: R$'))
print(f'Saldo: R${saldo:.2f}\n Reajuste +1%: R${saldo*0.01+saldo:.2f}')