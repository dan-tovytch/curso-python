# Introdução às Generator Functions em Python
# generator = (n for n in range(100000))

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1 

        if n > maximum:
            return


gen = generator(n=0, maximum=100000)
for n in gen:
    print(n)