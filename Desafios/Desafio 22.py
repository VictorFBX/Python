print('===DESAFIO 22===')

nome = input('DIGITE SEU NOME COMPLETO:').strip()
ns = nome.split()

len(ns)
print(f'Nome maiúsculo: {nome.upper()}')
print(f'Nome minúsculo: {nome.lower()}')
print("Quantas letras tem: {}".format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} '.format (ns[0]))