"""
Exercícios
Exiba os índices da lista
0 Daniel
1 Tuff
2 Mary Eduarda
"""
lista = ['Daniel', 'Tuff', 'Mary Eduarda']
lista.append('Kiwi')


indices = range(len(lista))


for indice in indices:
    print(indice, lista[indice], type(lista[indice]))