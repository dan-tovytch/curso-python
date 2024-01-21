"""calculadora com while"""
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite um número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
      numeros_validos = None

      if numeros_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando a sua conta. Confira o resultado abaixo')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=', num_1_float * num_2_float)
    else:
        print('Nunca deveria ter chegado aqui, finalizando cpu em: ')
        print('10')
        print('9')
        print('8')
        print('7')
        print('6')
        print('5')
        print('4')
        print('3')
        print('2')
        print('1')
        print('ADEUS!!')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
