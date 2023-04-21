# pedra(1) > tesoura(2) > papel(3) >
from random import randint
print('=-' * 20)
print('Jokepô')
print('=-' * 20)

jog = int(input('Pedra(1), tesoura(2) ou papel(3) '))
pc = randint(1, 3)

# possibilidades de vitória

if jog == 1 and pc == 2 or jog == 2 and pc == 3 or jog == 3 and pc == 1:
    print('PARABÉNS! Você venceu eu joguei {}'.format(pc))

# possibilidades de empate

elif jog == 1 and pc == 1 or jog == 2 and pc == 2 or jog == 3 and pc == 3:
    print('Jogamos iguais! Vamos de novo.')

else:
    print('NÃO FOI DESSA VEZ! Te venci com {}'.format(pc))
