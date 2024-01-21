# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Tuff', 'Daniel', 1, 2, 3, 'Alexandre']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Amora', 'Tuff', ],  # 0
    # 0
    ['Daniel', ],  # 1
    # 0       1       2
    ['Kiwi', 'Duda', 'Serola', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Tuff', 'Daniel', 1, 2, 3, 'Alexandre')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')