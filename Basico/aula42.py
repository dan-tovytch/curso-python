frase = 'Python é até que legal, porém prefiro java é ooooooooooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vazes = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes
        letra_apareceu_mais_vazes = letra_atual

    i += 1

print("A letra que apareceu mais vezes foi "
f'"{letra_apareceu_mais_vazes}" que apareceu '
f'{qtd_apareceu_mais_vezes}x')
