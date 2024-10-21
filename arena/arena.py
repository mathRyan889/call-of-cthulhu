from random import choice
lista_de_arenas = list()
arena_escolhida = list()
class Arena:
    def __init__(self,local,clima):
        self._local = local
        self._clima = clima
        
        lista_de_arenas.append(self)
        
    def __str__(self):
        return f'{self._local}:{self._clima}'
    
    @classmethod
    def arena_de_conflito(cls):# Metodo para escolher em qual cenario ocorrerá o  conflito
        print('¨¨'*50)
        print('Local de batalha')
        print('¨¨'*50)
        print(f'{'LOCAL'.ljust(19)} | {'CLIMA'}')
        for arena in arena_escolhida:
            print(f'{arena._local} | {arena._clima}')
        

# Criação das instâncias de Arena
arena1 = Arena('Floresta Negra', 'Chuvoso e escuro')
arena2 = Arena('Pântano dos Golens', 'Úmido e seco')
arena3 = Arena('Montanha Sombria', 'Frio e ventoso')
arena4 = Arena('Deserto Perdido', 'Quente e árido')
arena5 = Arena('Vale dos Dragões', 'Místico e nebuloso')
arena6 = Arena('Caverna das Sombras', 'Escuro e úmido')
arena7 = Arena('Ilha Fantasma', 'Brumoso e misterioso')
arena8 = Arena('Floresta Encantada', 'Calmo e mágico')
arena9 = Arena('Vulcão Ativo', 'Quente e perigoso')
arena10 = Arena('Ruínas Antigas', 'Silencioso e sombrio')

are = choice(lista_de_arenas) # Vai escolher uma arena aleatoria da lista_de_arenas
arena_escolhida.append(are) #Vai adicionar a arena escolhida a lista arena_escolhida