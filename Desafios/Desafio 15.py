print('=== Desafio 15 ===')
print('Aluguel de carro')

d = int(input('Por quantos dias o carro foi alugado? '))
k = float(input('Qual a quantidade de quilometros percorridos? '))

rd = float(d*60)
rk = float(k*0.15)

r = float(rd + rk)

print(f'Você tem a pagar R${r}')