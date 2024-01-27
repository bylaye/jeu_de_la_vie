# @author Abdoulaye Niang 
# @date 2024-01-27

"""
# 						Regle du jeu
###############################################################################################
 1. Une cellule ne survivra au tour suivant s'il est entouré par 2 ou 3 voisines
 
 2. En dessous de 2 la cellule en meurt  d'isolement
 
 3. En dessus de 3 elle meurt de surpopulation
 
 4. Si une case vide est entouré par exactement 3 voisines elle devient vivante au tour suivant
################################################################################################ 
"""

class Games:

    def __init__(self, initial, N_cellule = 12, vie='x', non_vie='-'):
        self.initial = initial
        self.vie = vie
        self.non_vie = non_vie
        self.N_cellule = N_cellule
        # Plateau du jeu tableau carre 2 dimensions 
        self.plateau = [ [non_vie]*N_cellule for _ in range(N_cellule) ]

        # stat etat liste des cellule morte ou naissance
        self.cellule_morte = []
        self.cellule_naissance = []


    """ Decouverte des cellules voisines """
    def cellule_voisine(self, cellule):
        v = Voisine(cellule, self.N_cellule)
        return v.voisine()


    """initialisation plateau des cellules"""
    def initialise_plateau(self):
        for coordonnee in self.initial:
            x, y = coordonnee
            self.plateau[x][y] = self.vie


    def get_plateau(self):
        return self.plateau


    def get_initial(self):
        return self.initial

    def get_cellule_morte(self):
        return self.cellule_morte

    def get_cellule_naissance(self):
        return self.cellule_naissance

    """ Mettre a jour les cellules vivant ou non en fonction des regles"""
    def update_cellule(self):
        new_cellule = []
        self.cellule_morte = []
        self.cellule_naissance = []
        for x in range(self.N_cellule):
            for y in range(self.N_cellule):
                cellule = (x,y)
                if self.plateau[x][y] == self.vie:
                    if self.reste_en_vie(cellule):
                        new_cellule.append(cellule)
                    else:
                        self.cellule_morte.append(cellule)
                else:
                    if self.naissance(cellule):
                        new_cellule.append(cellule)
                        self.cellule_naissance.append(cellule)
        return new_cellule

    """ Mise a jour du plateau du jeu apres mise a jour des cellules"""
    def update_plateau(self):
        new_cellule = self.update_cellule()
        for x in range(self.N_cellule):
            for y in range(self.N_cellule):
                if (x,y) in new_cellule:
                    self.plateau[x][y] = self.vie
                else:
                    self.plateau[x][y] = self.non_vie

    """ Verifier si une cellule vivante doit rester un vie respectant 
        la regle de n'avoir que 2 ou 3 voisines vivantes
    """
    def reste_en_vie(self, cellule):
        les_voisines = self.cellule_voisine(cellule)
        voisine_vivant = 0
        for v in les_voisines:
            if v is not None:
                x, y = v
                if self.plateau[x][y] == self.vie:
                    voisine_vivant += 1
        return True if voisine_vivant in (2,3) else False


    """ Pour une cellule non vivant verifier s'il peut naitre respectant
     la regle seulement 3 voisines vivantes
    """    
    def naissance(self, cellule):
        les_voisines = self.cellule_voisine(cellule)
        voisine_vivant = 0
        for v in les_voisines:
            if v is not None:
                x, y = v
                if self.plateau[x][y] == self.vie:
                    voisine_vivant += 1
        return True if voisine_vivant == 3 else False


""" la classe voisine permet de determiner pour les voisines
 pour chaque cellule choisit vivante ou non
"""
class Voisine:
    def __init__(self, cellule, N_cellule):
        self.cellule = cellule
        self.N_cellule = N_cellule
        self.x , self.y = cellule
        # Check si le x est bon et le y
        self.check_x = True if self.x < N_cellule and self.x >= 0 else False
        self.check_y = True if self.y < N_cellule and self.y >= 0 else False

    """Voisine de Gauche"""
    def voisine_gauche_haut(self):
        if self.x-1 >= 0 and self.y-1 >=0:
            return (self.x-1, self.y-1)
    
    def voisine_gauche_centre(self):
        if self.check_x and self.y-1 >=0:
            return (self.x, self.y-1)
    
    def voisine_gauche_bas(self):
        if self.x+1 < self.N_cellule and self.y-1 >=0:
            return (self.x+1, self.y-1)
    
    """Voisine de Centre"""
    def voisine_centre_haut(self):
        if self.check_y and self.x-1 >=0:
            return (self.x-1, self.y)

    def voisine_centre_bas(self):
        if self.check_y and self.x+1 < self.N_cellule:
            return (self.x+1, self.y)

    """Voisine de Droite"""
    def voisine_droite_haut(self):
        if self.x-1 >=0  and self.y+1 < self.N_cellule:
            return (self.x-1, self.y+1)
    
    def voisine_droite_centre(self):
        if self.check_x and self.y+1 < self.N_cellule:
            return (self.x, self.y+1)
    
    def voisine_droite_bas(self):
        if self.x+1 < self.N_cellule and self.y+1 < self.N_cellule:
            return (self.x+1, self.y+1)

    def voisine(self):
        out = []
        out.append(self.voisine_gauche_haut())
        out.append(self.voisine_gauche_centre())
        out.append(self.voisine_gauche_bas())
        out.append(self.voisine_centre_haut())
        out.append(self.voisine_centre_bas())
        out.append(self.voisine_droite_haut())
        out.append(self.voisine_droite_centre())
        out.append(self.voisine_droite_bas())
        return out

# In[204]:
import time
import os


def play():
    G.update_cellule()
    G.update_plateau()
    return G.get_plateau()


def imprime_plateau(plateau):
    out = ''
    for e in plateau:
        out = out+str(e)+'\n'
    return out

""" des exemples de configuration d'initialisation """
initial_0 = [(2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (1,2)]
carre = [(2,1), (2,2), (3,1), (3,2)] # stable carre
balise = [(7,5), (7,6), (8,5), (8,6), (9,3), (9,4), (10,3), (10,4)]
fascinant = [(10,15), (10,16), (9,16), (11,16), (9,17)] 
ligne_10 = [(7,5), (7,6), (7,7), (7,8), (7,9), (7,10), (7,11), (7,12), (7,13), (7,14)]

initial = ligne_10
N_cellule = 25
G = Games(initial, N_cellule)
G.initialise_plateau()


os.system('cls||clear')
print('Initialisation')
print(f'Stat Cellule : Morte 0, Naissance 0')
print(imprime_plateau(G.get_plateau()))
time.sleep(2)
os.system('cls||clear')

iter=1
while True:
    p = play()
    u = imprime_plateau(p)
    morte = G.get_cellule_morte()
    naissance = G.get_cellule_naissance()
    print(f'Iter {iter}')
    print(f'Stat Cellule : Morte {len(morte)}, Naissance {len(naissance)}')
    print(u)
    time.sleep(0.7)
    iter += 1
    os.system('clear||cls')
