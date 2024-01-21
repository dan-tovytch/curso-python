"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#entrada = input('Digite um número: ')

#try:    
 #   entrada_int = float(entrada)
  #  par_impar = entrada_int % 2 == 0
   # par_impar_texto = 'ímpar'

   # if par_impar:
    #    par_impar_texto = 'par'
#
 #   print(f'O número {entrada_int} é {par_impar_texto}')
#except:
 #   print('Você não digitou um número inteiro!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora: ')

# try:
#     hora = int(entrada)
#     if hora >= 0 and hora <= 5: 
#         print('Boa madrugada!')
#     elif hora >= 6 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Não sei que horas são essa')
# except:
#     print('Por favor, digite números inteiros!') 


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')

if nome:
    ...
else:
    print('Por Favor, digite seu nome!')
try:
    nome_len = len(nome)
    if nome_len >= 1 and nome_len <= 4:
        print('Seu nome é curto')
    elif nome_len >= 5 and nome_len <= 6:
        print('Seu nome é normal')
    elif nome_len >= 7:
        print('Seu nome é muito grande!')
except:
    ...