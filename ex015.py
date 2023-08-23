dias = float(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

pago = (dias * 60) + ( km * 0.15)

print('O preço a pagar é de {:.2f}'.format(pago))