import time
import os
from GameRules import GameRules

TOTAL_CELLS = 25
dx = int(TOTAL_CELLS/2)
initial = [(dx, dx+1), (dx, dx+2), (dx+1, dx+1), (dx+1, dx+1), (dx+2, dx+1)]
G = GameRules(initial, TOTAL_CELLS)
G.initialise_plateau()

def play():
    G.update_cells()
    G.update_plateau()
    return G.get_plateau()

def imprime_plateau(plateau):
    out = ''
    for e in plateau:
        out = out+str(e)+'\n'
    return out

os.system('cls||clear')
print('Initialisation')
print(f'Stat Cellule : Morte 0, Naissance 0')
print(imprime_plateau(G.get_plateau()))
time.sleep(1)
os.system('cls||clear')

iter=0
started = True
while started:
    p = play()
    u = imprime_plateau(p)
    dead = G.get_death_cells()
    birth = G.get_birth_cells()
    survived = G.get_survived_cells()
    if len(birth) == 0 and len(dead) == 0:
    	started = False
    else:
    	iter += 1
    print(f'Iter {iter}')
    print(f'Stat Cells : Dead {len(dead)}, Birth {len(birth)}, Survived {len(survived)}')
    print(u)
    time.sleep(0.7)
    if started:
    	os.system('clear||cls')
    else:
    	print(f'Stable structure after {iter} iteration(s)')
    	exit (0)
