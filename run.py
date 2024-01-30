from tkinter import *
import random
from jeu_de_la_vie import Games 
import time

root = Tk()
root.title('Jeu de la Vie')
canvas = Canvas(root,  width=600, height=700, background='blue')
canvas.pack(fill='both', expand=True)

MIN_X = 0
MAX_X = 600
CELLULE_SIZE = 5
COLOR_BACKGROUND = 'red'
COLOR_SURVIVE_CELLULE = 'white'

# l e trait fine de separation des cellules
LINE_CELLULE_SEPARATOR = 'black'

initial = [(30, 35), (30, 36), (29, 36), (31, 36), (29, 37)]
#initial = [(50, 55), (50, 56), (49, 56), (51, 56), (49, 57)]
initial = [(2,1), (2,2), (3,1), (3,2)]
initial = [(7,5), (7,6), (8,5), (8,6), (9,3), (9,4), (10,3), (10,4)]
initial = [(7,5), (7,6), (7,7), (7,8), (7,9), (7,10), (7,11), (7,12), (7,13), (7,14)]
initial = [(i,j) for i in range(30,70) for j in range(30,70) ]
G = Games(initial, int(MAX_X/CELLULE_SIZE))

pause_simulation = True
started = False
iteration = 0

def cellule_vivant(list_cellule, CELLULE_SIZE):
	for cell in list_cellule:
		b, a = cell	
		r = (a*CELLULE_SIZE, b*CELLULE_SIZE, CELLULE_SIZE*(a+1), CELLULE_SIZE*(b+1))
		canvas.create_rectangle(r, width=1, fill=COLOR_SURVIVE_CELLULE)


def trace_cellule(CELLULE_SIZE, MIN_X, MAX_X):
	for i in range(MIN_X+CELLULE_SIZE, MAX_X, CELLULE_SIZE):
		canvas.create_line((i, MIN_X, i, MAX_X), width=1, fill=LINE_CELLULE_SEPARATOR)
		canvas.create_line((MIN_X, i, MAX_X, i), width=1, fill=LINE_CELLULE_SEPARATOR)


def simulation():
	canvas.delete('all')
	canvas.create_rectangle(MIN_X,MIN_X,MAX_X,MAX_X, width=1, fill=COLOR_BACKGROUND)
	v = refresh()
	cellule_vivant(v, CELLULE_SIZE)
	trace_cellule(CELLULE_SIZE, MIN_X, MAX_X)
	stats()
	if not pause_simulation:
		root.after(200,simulation)

def refresh():
	global started
	if not started:
		G.initialise_plateau()
		cell = initial
		started = True
	else:
		cell = G.update_cellule()
		G.update_plateau()
	return cell

def stats():
	global iteration
	t = f'Iteration : {iteration}'
	cell_dead = G.get_cellule_morte()
	cell_survive = G.get_cellule_naissance()
	if len(cell_dead)==0 and len(cell_survive) == 0:
		e = f'Stable after {iteration} iteration'
		canvas.create_text(0, 680, text=e, font=("Helvetica", 12), anchor="sw")
	else:
		iteration += 1
	t2 = f'Cellule Dead {len(cell_dead)}'
	t3 = f'Cellule Birth {len(cell_survive)}'
	canvas.create_text(0, 620, text=t, font=("Helvetica", 12), anchor="sw")
	canvas.create_text(0, 640, text=t2, font=("Helvetica", 12), anchor="sw")
	canvas.create_text(0, 660, text=t3, font=("Helvetica", 12), anchor="sw")
	
	
def play_pause():
    global pause_simulation
    pause_simulation = not pause_simulation
    if not pause_simulation:
        simulation()

start_simulation = Button(root, text='START/PAUSE', width=20, command=play_pause)
start_simulation.pack(side=LEFT, padx=10, pady=20)

exit_button = Button(root, text='EXIT', width=20, command=root.quit)
exit_button.pack(side=RIGHT, padx=10)

root.mainloop()
