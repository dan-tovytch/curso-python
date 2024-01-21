"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# adivinha_p = input("Nos diga qual é a palavra secreta: ")
# print(f'Você tentou adivinhar que era "{adivinha_p}"')
# for palavra in adivinha_p:
#     adivinha = adivinha_p
#     if adivinha_p == 'tuff':
#         print(f'A palavra secreta era {adivinha}')
#         break
#     elif adivinha == adivinha_p:
#         print('Você errou!') 

import os

palavra_sec = 'perfume'
letras_act = ''
numero_ten = 0

while True:

    letra_dgt = input('Digite uma letra: ')
    numero_ten += 1

    if len(letra_dgt) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_dgt in palavra_sec:
        letras_act += letra_dgt
    
    palavra_for = ''
    for letra_sec in palavra_sec:
        if letra_sec in letras_act:
            palavra_for += letra_sec
        else:
            palavra_for += '*'

    print('Palavra Formada', palavra_for)
    
    if palavra_for == palavra_sec:
        os.system('cls')
        print('Você ganhou!')
        print('A palavra era:', palavra_for)
        print('Tentativa:', numero_ten)
        letras_act = ''
        numero_ten = 0