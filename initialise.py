"""
Initialisation du jeu:
Lors de son appel on a besoin de renseigne comme parametre 
seulement le milieu du plateau pour qu'on puisse initialiser 
a partir du milieu et gagner plus de place de chaque cote
"""
def initial(d_x, position=0):
    INITIAL = [
            [(d_x, d_x+1), (d_x, d_x+2), (d_x+1, d_x+1), (d_x+1, d_x+2)],
            [(d_x,d_x+1), (d_x,d_x+2), (d_x,d_x+3),(d_x+3, d_x+1), (d_x+3,d_x+2), (d_x+3, d_x+3)],
            [
                (d_x,d_x-5), (d_x,d_x-4), (d_x,d_x-3), 
                (d_x,d_x-2), (d_x, d_x-1), (d_x, d_x), 
                (d_x,d_x+1), (d_x,d_x+2), (d_x,d_x+3), (d_x,d_x+4)
            ],
            [(i,j) for i in range(d_x-20, d_x+20) for j in range(d_x-20, d_x+20)],
            [(d_x, d_x+1), (d_x, d_x+2), (d_x-1, d_x+2), (d_x+1, d_x+2), (d_x-1, d_x+3)]
    ]
    return INITIAL[position]

