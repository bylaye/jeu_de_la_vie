""" la classe voisine permet de determiner pour les voisines
 pour chaque cellule choisie vivante ou non
"""
class Neighbors:
    def __init__(self, cellule, N_cellule):
        self.cellule = cellule
        self.N_cellule = N_cellule
        self.x , self.y = cellule
        # Check si le x est bon et le y
        self.check_x = True if self.x < N_cellule and self.x >= 0 else False
        self.check_y = True if self.y < N_cellule and self.y >= 0 else False

    """Voisine de Gauche"""
    def neighbor_left_top(self):
        if self.x-1 >= 0 and self.y-1 >=0:
            return (self.x-1, self.y-1)
    
    def neighbor_left_center(self):
        if self.check_x and self.y-1 >=0:
            return (self.x, self.y-1)
    
    def neighbor_left_bottom(self):
        if self.x+1 < self.N_cellule and self.y-1 >=0:
            return (self.x+1, self.y-1)
    
    """Voisine de Centre"""
    def neighbor_center_top(self):
        if self.check_y and self.x-1 >=0:
            return (self.x-1, self.y)

    def neighbor_center_bottom(self):
        if self.check_y and self.x+1 < self.N_cellule:
            return (self.x+1, self.y)

    """Voisine de Droite"""
    def neighbor_right_top(self):
        if self.x-1 >=0  and self.y+1 < self.N_cellule:
            return (self.x-1, self.y+1)
    
    def neighbor_right_center(self):
        if self.check_x and self.y+1 < self.N_cellule:
            return (self.x, self.y+1)
    
    def neighbor_right_bottom(self):
        if self.x+1 < self.N_cellule and self.y+1 < self.N_cellule:
            return (self.x+1, self.y+1)

    def neighbor_list(self):
        out = []
        out.append(self.neighbor_left_top())
        out.append(self.neighbor_left_center())
        out.append(self.neighbor_left_bottom())
        out.append(self.neighbor_center_top())
        out.append(self.neighbor_center_bottom())
        out.append(self.neighbor_right_top())
        out.append(self.neighbor_right_center())
        out.append(self.neighbor_right_bottom())
        return out
