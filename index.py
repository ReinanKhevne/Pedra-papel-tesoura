# pedra(1) > tesoura(2) > papel(3) >
from random import randint
print('=-' * 20)
print('Jokepô')
print('=-' * 20)

jog1 = str(input('Pedra, papel ou tesoura?? ')).upper
jog2 = randint(1, 3)
# conversão de str para int para melhor digitação do usuário
if jog1 == 'PEDRA':
    usuario = 1
elif jog1 == 'TESOURA':
    usuario = 2
elif jog1 == 'PAPEL':
    usuario = 3
else:
    usuario = 'Você NÃO está utilizando as REGRAS do jogo corretamente!'

# possibilidades de derrota
if jog1 == 1 and jog2 == 3 or jog1 == 2 and jog2 == 1 or jog1 == 3 and jog2 == 2:
    print('NÃO FOI DESSA VEZ, eu joguei {} e você {}'.format(jog2, jog1))

# possibilidades de vitória
if jog1 == 1 and jog1 == 2 or jog1 == 2 and jog2 == 3 or jog1 == 3 and jog2 == 1:
    print('PARABÉNS, conseguiu me vencer! joguei {}.'.format(jog2))

# apresentação na tela
