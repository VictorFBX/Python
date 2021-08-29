
print('=== DESAFIO 33 ===')
print('QUAL NUMERO É O MAIOR'.upper())

print("""VOCÊ IRA DIZER DOIS NUMEROS E
EU IREI DIZER QUAL DOS NÚMERO É O MAIOR""")

num1 = float(input('Fale o primeiro número: '))
num2 = float(input('Fale o segundo nùmero: '))

if num1 >= num2:
    print(f'{num1} é maior que o número {num2}')

else:
    print(f'{num2} é maior que o número {num1}')