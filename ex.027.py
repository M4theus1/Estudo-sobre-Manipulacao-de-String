n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em conhecê-lo, {}'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

