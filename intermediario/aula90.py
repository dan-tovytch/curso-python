import sys

# Generator expression, Iterables e Iteradores em Python
interable = ['Eu', 'Tenho', '__iter__']
iterator = iter(interable) # tem __iter__ e __next__
lista = [n for n in range(10)] 
generetor = (n for n in range(10))
print(sys.getsizeof(lista))
print(sys.getsizeof(generetor))