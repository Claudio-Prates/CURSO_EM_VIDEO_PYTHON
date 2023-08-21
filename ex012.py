prod = float(input('Digite o valor do produto: '))
taxa_desconto = (float(input('Digite o percentual de desconto: ')))

valor_desconto = prod - (prod * taxa_desconto)

print('O valor do seu produto na liquidação é de {}'.format(valor_desconto))