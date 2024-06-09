# List comprehension
# List comprehension é uma forma concisa de criar listas
# a partir de interáveis.
lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)

# Mapeamento de dados em list comprehension
protutos = [
    { 'nome': 'p1', 'preco': 20 },  
    { 'nome': 'p2', 'preco': 10 },  
    { 'nome': 'p3', 'preco': 30 },  
]

novos_produto = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in protutos
]

# print(*novos_produto, sep='\n')

# lista = [n for n in range(10) if n < 5]
novos_produto = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in protutos
    if (produto['preco'] * 1.05) > 20
]

print(novos_produto)