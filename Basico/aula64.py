import random

for _ in range(100):
    nove_dgt = ''
    for i in range(9):
        nove_dgt += str(random.randint(0, 9))

    contador_regre_1 = 10

    resultado_digito_1 = 0
    for digito_1 in nove_dgt:
        resultado_digito_1 += int(digito_1) * contador_regre_1
        contador_regre_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_dgt = nove_dgt + str(digito_1)
    contador_regre_2 = 11 

    resultado_digito_2 = 0
    for digito in dez_dgt:
        resultado_digito_2 += int(digito) * contador_regre_2
        contador_regre_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_ger_calcu = f'{nove_dgt}{digito_1}{digito_2}'

    print(cpf_ger_calcu)
        