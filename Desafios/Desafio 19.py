import random

print('=== Desafio 19 ===')
print('Escolha aleatoria')

p = input('Primeira coisa da lista: ')
s = input('Segunda coisa da lista: ')
t = input('Terceira coisa da lista: ')
q = input('Quarta coisa da lista: ')
lista = [p, s, t, q]

print('Escolhendo algum aleatoriamente....')

print('O item sorteado foi....')

print(random.choice(lista))
