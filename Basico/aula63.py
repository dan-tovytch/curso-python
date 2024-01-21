"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""
import re
import sys

# cpf_env_user = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '') 
entrada = input('CPF [746.824.890-70]: ')
cpf_env_user = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_seq = entrada == entrada[0] * len(entrada)

if entrada_e_seq:
    print('Você enviou dados sequenciais')
    sys.exit()
nove_dgt = cpf_env_user[:9]
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

if cpf_env_user == cpf_ger_calcu:
    print(f'{cpf_env_user} é valido')
else:
    print('CPF inválido')
    