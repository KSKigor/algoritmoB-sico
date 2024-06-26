import random
resposta = random.randint(1, 200)
pergunta = int(input('numero:'))
while resposta != pergunta:
    if pergunta < resposta:
        print('muito Baixo!')
    elif pergunta > resposta:
        print('muito alto!')
    pergunta = int(input('numero:'))
if pergunta == resposta:
    print('você acertou!')
