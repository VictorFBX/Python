from random import shuffle

print('=== Desafio 20 ===')
print('Ordem de apresentação dos trabalhos')

a1 = str(input('Qual o primeiro aluno? '))
a2 = str(input('Qaal o segundo aluno? '))
a3 = str(input('Qual o terceiro aluno? '))
a4 = str(input('Qual o quarto aluno? '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print('A ordem de apresentação é...')
print(lista)