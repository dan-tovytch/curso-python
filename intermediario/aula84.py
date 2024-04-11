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
print(lista)

# Mapeamento de dados em list comprehension
protutos = [
    { 'nome': 'p1', 'preco': 20 },  
    { 'nome': 'p2', 'preco': 10 },  
    { 'nome': 'p3', 'preco': 30 },  
]

novo_produto = [
    produto
    for produto in protutos
]

print(*novo_produto, sep='\n')