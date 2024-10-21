from random import randint
from random import choice
from time import sleep
lista_de_monstros = list()
monstro_escolhido = list()
class Monstros:
    @classmethod
    def __init__(self,nome=str,classe=str,nivel = int):
        self._nome = nome
        self._classe = classe
        self._nivel = nivel
        self._loucura = randint(10,200)*nivel
        lista_de_monstros.append(self)
    
    def __str__(self):
        return f'{self._nome}|{self._classe}'
    
    @classmethod
    def exibindo_monstro(cls):
        print('>>>>'*30)
        print('       CRIATURA SELECIONADA')
        print('>>>>'*30)
        print('...')
        sleep(0.7)
        for monstro in monstro_escolhido:
            print(f'NOME:{monstro._nome}\nCLASSE:{monstro._classe}\nLEVEL:{monstro._nivel}\nNIVEL DE LOUCURA:{monstro._loucura}')

    @classmethod
    def nivel_de_loucura(self):
        loucura = self._loucura        

monstro1 = Monstros('Nyarlathotep', 'Arauto', 95)
monstro2 = Monstros('Azathoth', 'Deus', 150)
monstro3 = Monstros('Shub-Niggurath', 'Deusa Antiga', 130)
monstro4 = Monstros('Dagon', 'Grande Antigo', 100)
monstro5 = Monstros('Ithaqua', 'Arauto', 85)
monstro6 = Monstros('Cthulhu', 'Antigo', 110)
monstro7 = Monstros('Byakhee', 'Fraco', 40)
monstro8 = Monstros('Ghoul', 'Fraco', 30)
monstro9  = Monstros('Tsathoggua', 'Antigo', 105)
monstro10 = Monstros('Yog-Sothoth', 'Deus', 140)
monstro11 = Monstros('Zhar', 'Grande Antigo', 100)
monstro12 = Monstros('Nodens', 'Deus', 125)
monstro13 = Monstros('Ghroth', 'Arauto', 90)
monstro14 = Monstros('Eihort', 'Antigo', 85)
monstro15 = Monstros('Ghatanothoa', 'Grande Antigo', 110)
monstro16 = Monstros('Atlach-Nacha', 'Antigo', 95)
monstro17 = Monstros('Yig', 'Grande Antigo', 100)
monstro18 = Monstros('Chaugnar Faugn', 'Grande Antigo', 105)
monstro19 = Monstros('Hydra', 'Fraco', 45)
monstro20 = Monstros('Mi-Go', 'Fraco', 50)
monstro21 = Monstros('Shoggoth', 'Médio', 75)
monstro22 = Monstros('Nightgaunt', 'Médio', 70)
monstro23 = Monstros('Star-Spawn of Cthulhu', 'Médio', 80)
monstro24 = Monstros('Flying Polyp', 'Forte', 95)
monstro25 = Monstros('Dimensional Shambler', 'Médio', 65)
monstro26 = Monstros('Deep One', 'Fraco', 40)
monstro27 = Monstros('Lloigor', 'Antigo', 115)
monstro28 = Monstros('Cyaegha', 'Antigo', 100)
monstro29 = Monstros('Byatis', 'Grande Antigo', 95)
monstro30 = Monstros('Glaaki', 'Antigo', 110)
monstro31 = Monstros('Rhan-Tegoth', 'Grande Antigo', 105)
monstro32 = Monstros('Bokrug', 'Antigo', 90)
monstro33 = Monstros('Zoth-Ommog', 'Grande Antigo', 115)
monstro34 = Monstros('Dhole', 'Forte', 100)
monstro35 = Monstros('Kassogtha', 'Antigo', 100)
monstro36 = Monstros('Rlim Shaikorth', 'Antigo', 90)
monstro37 = Monstros('Iod', 'Antigo', 95)
monstro38 = Monstros('Ubbo-Sathla', 'Grande Antigo', 120)
monstro39 = Monstros('Oorn', 'Antigo', 85)
monstro40 = Monstros('Yidhra', 'Antigo', 100)


monst =  choice(lista_de_monstros)
monstro_escolhido.append(monst)      
        
        
        
    
    
    
        