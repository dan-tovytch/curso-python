"""
Higher Orde Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f"{msg}, {nome}!"

def executa(funcao, *args):
    return funcao(*args)



v = executa(saudacao, 'Bom dia', 'Daniel')
print(v)