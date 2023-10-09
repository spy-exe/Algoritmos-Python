# 2. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
# alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma
# projeção de quanto será gasto com o pagamento deste abono.
# o Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato
# laboral, chegou-se a seguinte forma de cálculo:
# o a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono
# será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor
# mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de
# casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário
# de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a
# digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a
# cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
# o O salário de cada funcionário, juntamente com o valor do abono;
# o O número total de funcionário processados;
# o O valor total a ser gasto com o pagamento do abono;
# o O número de funcionário que receberá o valor mínimo de 100 reais;
# o O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins
# ilustrativos. Os valores podem mudar a cada execução do programa.
# Projeção de Gastos com Abono
# ============================
# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0
# Salário - Abono
# R$ 1000.00 - R$ 200.00
# R$ 300.00 - R$ 100.00
# R$ 500.00 - R$ 100.00
# R$ 100.00 - R$ 100.00
# R$ 4500.00 - R$ 900.00
# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00

total_processed = 0
total_spent = 0
min_salary_count = 0
max_abono = 0

while True:
    salary = float(input("Salário: "))
    if salary == 0:
        break
    
    abono = max(salary * 0.2, 100)
    
    total_processed += 1
    total_spent += abono
    if abono == 100:
        min_salary_count += 1
    if abono > max_abono:
        max_abono = abono
    
    print(f"R$ {salary:.2f} - R$ {abono:.2f}")

print(f"Foram processados {total_processed} colaboradores")
print(f"Total gasto com abonos: R$ {total_spent:.2f}")
print(f"Valor mínimo pago a {min_salary_count} colaboradores")
print(f"Maior valor de abono pago: R$ {max_abono:.2f}")