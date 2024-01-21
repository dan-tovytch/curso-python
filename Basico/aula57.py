"""
lista de lista e suas índices
"""
salas = [
    # 0        1
    ['Amora', 'Tuff', ],  # 0
    # 0
    ['Daniel', ],  # 1
    # 0       1       2
    ['Kiwi', 'Duda', 'Serola', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'sala é {sala}')
    for aluno in sala:
        print(aluno)