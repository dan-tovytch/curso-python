"""
split e join com list e str
slipt - devide uma string (list)
join - une uma string
"""
frase = '   Olha só que,     coisa interessante      '
lista_frase_crua = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())

# print(lista_frase_crua)
# print(lista_frase)
frase_unida = ', '.join(lista_frase)
print(frase_unida)