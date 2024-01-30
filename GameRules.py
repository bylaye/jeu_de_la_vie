# @author Abdoulaye Niang
# @email : abdoulayeniang2010@gmail.com
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

from Neighbors import Neighbors

class GameRules:
    def __init__(self, initial, N_cellule = 12, SURVIVE='x', NO_SURVIVE=' '):
        self.initial = initial
        self.SURVIVE = SURVIVE
        self.NO_SURVIVE = NO_SURVIVE
        self.N_cellule = N_cellule
        # Plateau du jeu tableau carre 2 dimensions 
        self.plateau = [ [NO_SURVIVE]*N_cellule for _ in range(N_cellule) ]
        # stat etat liste des cellule morte ou naissance
        self.death_cells = []
        self.birth_cells = []
        self.survived_cells = []

    """ Decouverte des cellules voisines """
    def neighbors_cells(self, cellule):
        v = Neighbors(cellule, self.N_cellule)
        return v.neighbor_list()

    """initialisation plateau des cellules"""
    def initialise_plateau(self):
        for coordonnee in self.initial:
            x, y = coordonnee
            self.plateau[x][y] = self.SURVIVE

    """ Verifier si une cellule vivante doit rester en vie respectant 
        la regle de n'avoir que 2 ou 3 voisines vivantes
  	"""
    def cell_survive(self, cellule):
        neighbors_list = self.neighbors_cells(cellule)
        survive_neighbors = 0
        for v in neighbors_list:
            if v is not None:
                x, y = v
                if self.plateau[x][y] == self.SURVIVE:
                    survive_neighbors += 1
        return True if survive_neighbors in (2,3) else False

    """ Pour une cellule non vivant verifier s'il peut naitre respectant
     la regle seulement 3 voisines vivantes
    """    
    def cell_birth(self, cellule):
        neighbors_list = self.neighbors_cells(cellule)
        survive_neighbors = 0
        for v in neighbors_list:
            if v is not None:
                x, y = v
                if self.plateau[x][y] == self.SURVIVE:
                    survive_neighbors += 1
        return True if survive_neighbors == 3 else False

    """ Mettre a jour les cellules vivant ou non en fonction des regles"""
    def update_cells(self):
        new_cellule = []
        self.death_cells = []
        self.birth_cells = []
        self.survived_cells = []
        for x in range(self.N_cellule):
            for y in range(self.N_cellule):
                cellule = (x,y)
                if self.plateau[x][y] == self.SURVIVE:
                    if self.cell_survive(cellule):
                        new_cellule.append(cellule)
                        self.survived_cells.append(cellule)
                    else:
                        self.death_cells.append(cellule)
                else:
                    if self.cell_birth(cellule):
                        new_cellule.append(cellule)
                        self.birth_cells.append(cellule)
        return new_cellule

    """ Mise a jour du plateau du jeu apres mise a jour des cellules"""
    def update_plateau(self):
        new_cellule = self.update_cells()
        for x in range(self.N_cellule):
            for y in range(self.N_cellule):
                if (x,y) in new_cellule:
                    self.plateau[x][y] = self.SURVIVE
                else:
                    self.plateau[x][y] = self.NO_SURVIVE

    def get_plateau(self):
        return self.plateau

    def get_initial(self):
        return self.initial

    def get_survived_cells(self):
        return self.survived_cells
		
    def get_death_cells(self):
        return self.death_cells

    def get_birth_cells(self):
        return self.birth_cells
