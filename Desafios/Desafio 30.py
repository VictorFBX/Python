
print('=== DESAFIO 31 ===')
print('Viagem'.upper())

d = float(input('Qual a distancia da viajem: '))
menos = float(d*0.50)
mais = float(d*0.45)

if d < 200:
    print(f"""Considerando que o valor da passagem seja
    0.50 centavos por quilometro (em viagens menores de 200km) o valor 
    a pagar seria: {menos}""")

else:
    print(f"""Considerando que o valor da passagem seja
    0.45 centavos por quilometro (em viagens maiores de 200km
    o valor apagar seri: {mais}""")