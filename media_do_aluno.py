n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
media = (n1 + n2 + n3) / 3
if media <= 5:
    print('REPROVADO!')
elif media == 6:
    print('EXAME')
else:
    print('APROVADO')