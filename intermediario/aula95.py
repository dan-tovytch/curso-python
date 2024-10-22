# raise - lançando exeções (erros)

def nao_aceito_zero(d):
    if d == 0:
        raise ValueError('Não aceito valor zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (int, float)):
        raise ValueError(f'{n} deve ser int ou float '
                         f'"{tipo_n.__name__} enviado"')
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))