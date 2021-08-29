
print('=== DESAFIO 30 ===')
print('Impar ou par?'.upper())

n = int(input('Digite um numero inteiro e direi se é impar ou par: '))
r = n%2

if r != 0:
    print('Seu número é impar!')

else:
    print('Seu número é par!')