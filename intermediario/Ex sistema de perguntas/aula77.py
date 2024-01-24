# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

certas = 0
erradas = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for indice, opcao in enumerate(pergunta['Opções'], start=1):
        print(f"{indice:02d}) {opcao}")

    while True:
        try:
            opcao = int(input('Escolha uma opção: '))
            if opcao == pergunta['Opções'].index(pergunta['Resposta']) + 1:
                print('Você acertou 👍\n')
                certas += 1
                break
            else:
                print('Você errou 👎\n')
                erradas += 1
                break
        except ValueError:
            print('🚫 Insira uma opção válida!\n')

print(f"✅ Total de respostas corretas: {certas}")
print(f"❌ Total de respostas incorretas: {erradas}")