from os import system
from random import randint
from time import sleep


system('clear')

y = [27,91,49,59,51,50,109,102,101,105,116,111,32,112,111,114,58,27,91,109,32,27,91,49,59,51,49,109,104,116,116,112,115,58,47,47,103,105,116,104,117,98,46,99,111,109,47,109,97,105,108,115,111,110,115,118,27,91,109]

for x in y:
    print(chr(x), end='', flush=True)
    sleep(0.1)


# cores
vermelhor = "\033[1;31m"
verde = "\033[1;32m"
feixa_cor = "\033[m"



def jogar():
    '''\033[7;3;31mjoguinho simples pra jogar quando tive sem net
    escolhar sua opção pedra,papel ou tesoura,
    digite apenas numeros para nao ocorrer error\33[m'''

    global vermerlhor, verde,feixa_cor

    x = [10,9556,9552,9552,9552,9559,9556,9552,9552,9552,9559,9556,9552,9559,9556,9552,9559,9556,9552,9552,9552,9559,10,9553,9556,9552,9559,9553,9553,9556,9552,9559,9553,9553,9553,9562,9565,9553,9553,9553,9556,9552,9552,9565,10,9553,9553,9472,9562,9565,9553,9553,9472,9553,9553,9553,9556,9559,9556,9559,9553,9553,9562,9552,9552,9559,10,9553,9553,9556,9552,9559,9553,9562,9552,9565,9553,9553,9553,9553,9553,9553,9553,9553,9556,9552,9552,9565,10,9553,9562,9577,9552,9553,9553,9556,9552,9559,9553,9553,9553,9553,9553,9553,9553,9553,9562,9552,9552,9559,10,9562,9552,9552,9552,9565,9562,9565,9472,9562,9565,9562,9565,9562,9565,9562,9565,9562,9552,9552,9552,9565]

    for x in x:
        print(f"{verde}{chr(x)}{feixa_cor}", end='')
    
    itens = ('pedra', 'papel', 'tesoura')
    
    computador = randint(0, 2)
    

    print(f"""{verde}
    suas opçoes 
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA{feixa_cor}""")
    
    jogador = int(input(f"   {verde}qual e a sua jogadar?:{feixa_cor}"))
            
    animacao = "\tjoo\n\tken\n\tpow\n"
    for x in animacao:
        print(f'{verde}{x}{feixa_cor}', end='', flush=False)
        sleep(0.1)
    
    print(f"{vermelhor}{'-' * 40}{feixa_cor}\n\t{verde}computador jogou{feixa_cor} {vermelhor}{itens[computador]}{feixa_cor}\n\t{verde}jogador jogou{feixa_cor} {vermelhor}{itens[jogador]}{feixa_cor}\n{vermelhor}{'-' * 40}{feixa_cor}")
    
    if computador == 0:
        
        if jogador == 0:
            print(f'\t\t{verde} EMPATE {feixa_cor}')
        
        elif jogador == 1:
            print(f'\t\t {verde} JOGADOR VENCEU {feixa_cor}')

        elif jogador == 2:
            print(f'\t\t {verde} CONPUTADOR VENCEU {feixa_cor}')

        else:
            print(f'\t\t {verde} JOGADA INVALIDA {feixa_cor}')

    elif computador == 1:
        
        if jogador == 0:
            print(f'\t\t {verde} COMPUTADOR VENCE {feixa_cor}')
                
        elif jogador == 1:
            print(f'\t\t {verde} EMPATE {feixa_cor}')

        elif jogador == 2:
            print(f'\t\t {verde} JOGADOR VENCE {feixa_cor}')

        else:
            print(f'\t\t {vermelhor} JOGADA INVALIDA {feixa_cor}')

    elif computador == 2:
        
        if jogador == 0:
            print(f'\t\t {verde} JOGADOR VENCE {feixa_cor}')

        elif jogador == 1:
            print(f'\t\t {verde} COMPUTADOR VENCE {feixa_cor}')

        elif jogador == 2:
            print(f'\t\t{verde} EMPATE {feixa_cor}')

        else:
            print(f'\t\t{verde} JOGADA INVALIDA {feixa_cor}')

            
    novamente = input(f"{verde} sair [ s ] ajuda [ j ] jogar novamente [ n ]{feixa_cor}").lower()
    
    if novamente == 's':
        exit()
    
    elif novamente == 'j':
        print(jogar.__doc__)

    elif novamente == 'n':
        system('clear')
        jogar()

jogar()

