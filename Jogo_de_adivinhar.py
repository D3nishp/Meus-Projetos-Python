nome = input('Qual e o seu nome ? ')
numero_secreto = 8
palpite = 0
while palpite != numero_secreto:
    palpite = int(input('qual é o seu número secreto ? '))
    if palpite > numero_secreto:
        print('chutou alto')
    elif palpite < numero_secreto:
        print('chutou baixo')
print('Parabéns {} você acertou o número'.format(nome))