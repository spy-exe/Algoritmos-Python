# 14) Solicitar salário, prestação. Se prestação for maior que 20% do salário, 
# imprimir: Empréstimo não pode ser concedido. Senão imprimir empréstimo 
# pode ser concedido. 

salary = float(input('Insira seu salário: $'))
prest = float(input('Insira o valor da prestação: $'))

if prest > (salary+(salary*0.20)):
    print('Empréstimo não pode ser concedido\n'
         f'Prestação e maior que 20% do salário')
else:
    print('Empréstimo aprovado.')
