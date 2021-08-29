
print('=== DESAFIO 32 ===')
print('ANO BISSEXTO'.upper())

ano = int(input('Digite um ano e descobrirei se ele é bissexto: '))


if ano % 4 == 0 and ano % 100 != 0 or ano * 400 == 0:
    print(f'O ano {ano} é BISSEXTO')

else:
    print(f'O ano {ano} não é BISSEXTO')

