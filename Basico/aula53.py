"""
enumerate - enumera interáveis (índices)
"""
# [(0, 'Daniel'), (1, 'Tuff'), (2, 'Kiwi'), (3, 'Amora')]
lista = ['Daniel','Tuff','Kiwi']
lista.append('Amora')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
