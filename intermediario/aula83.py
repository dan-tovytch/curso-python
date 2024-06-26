# Empacotamento e desempacotamento
a, b = 1, 2
a, b = b, a
# print(a, b)



# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# args e Kwargs
# args (já vimos)
# Kwargs - keyword arguments (argumentos nomeaveis)

def mostro_argumentos_nomeados(*args, **kwargs):
    print("NÃO NOMEADOS: ", args)
    for key, value in kwargs.items():
        print(key, value)
# mostro_argumentos_nomeados(1,2, nome='Joana', qlq=123)

configuracao = {
    'args1': 1,
    'args2': 2,
    'args3': 3,
    'args4': 4,
}
mostro_argumentos_nomeados(**configuracao)