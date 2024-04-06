from emoji import emojize
from random import choice
from time import sleep

cont = 5
lifeat = cont
while lifeat > 0:
    pc_atack = [emojize(':punch:', language='alias')], [emojize(':right_facing_fist:', language='alias')],[emojize(':left_facing_fist:', language='alias')]
    ran = choice(pc_atack)
    #player
    player_atacks = [emojize(':arrow_left:',language='alias')],[emojize(':arrow_right:',language='alias')],[emojize(':shield:',language='alias')]
    print(emojize(':arrow_left:',language='alias'),'L',emojize('\n:arrow_right:',language='alias'),'R',emojize('\n:shield:',language='alias'),'G' )
    player_atack = input('Escolha[\033[34mL/R/G\033[m] ⇨ ').upper().strip()[0]
    sleep(1)
    #esquerda
    if player_atack == 'L' and ran == pc_atack[2]:
        print(player_atacks[0])
        print(ran)
        lifeat -= 1
        print('\033[31m-1 vida\033[m')
    #direita
    elif player_atack == 'R' and ran == pc_atack[1]:
        print(player_atacks[1])
        print(ran)
        lifeat -= 1
        print('\033[31m-1 vida\033[m')
    #defender
    elif player_atack == 'G' and ran == pc_atack[0]:
        print(player_atacks[2])
        print(ran)
        lifeat -= 2
        print('\033[31m-2 vida\033[m')
    else:
        print(ran)
        if player_atack == 'L':
            print(player_atacks[0])
        elif player_atack == 'R':
            print(player_atacks[1])
        else:
            print(player_atacks[2])
        print('')
    print(lifeat, emojize(':heart:',language='alias'))
    print('-='*10)
print('\033[31mFIM DE JOGO!\033[31m')
