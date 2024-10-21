import os
from arena.arena import Arena
from montros.monstros import Monstros
from montros.monstros import lista_de_monstros

loucura = Monstros._loucura


def main():
    Arena.arena_de_conflito()
    input('Aperte qualquer tecla para voltar ao menu inicial:')
    os.system('cls')
    #Monstros.exibindo_monstro()
    if loucura > 100:
        print('ficou louco')
    else:
        print('fuja')
    
    


if __name__ == '__main__':
    main()

