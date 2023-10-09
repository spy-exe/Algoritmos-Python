# 08) Informar um preço de um produto e calcular novo preço com desconto de 9%

product_price = float(input('Insira o preço do produto: $'))
print(f'[9% OFF] Novo preço: ${product_price-product_price*0.09:.2f}')