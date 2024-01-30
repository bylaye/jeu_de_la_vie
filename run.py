from tkinter import *
from GameRules import GameRules
import initialise

COLOR_BACKGROUND_CELLULE = 'red'
COLOR_BACKGROUND_CANVAS = 'blue'
COLOR_SURVIVE_CELLULE = 'white'
LINE_CELLULE_SEPARATOR = 'black'
IS_CELLULE_LINES = True
INTERVAL_TIME_SIMULATION = 200 # unite en milliseconde
MIN_X = 0 #A ne pas changer
MAX_X = 500
CELLULE_SIZE = 5
TOTAL_CELLULE = int(MAX_X/CELLULE_SIZE)
TEXT_FONT = 'Helvetica'
TEXT_CANVAS_ANCHOR = 'sw'

pause_simulation = True
started = False
iteration = 0
d_x = int(TOTAL_CELLULE/2)
initial = initialise.initial(d_x, 4)
G = GameRules(initial, TOTAL_CELLULE)

root = Tk()
root.title('Jeu de la Vie')
canvas = Canvas(root,  width=MAX_X, height=MAX_X+100, background=COLOR_BACKGROUND_CANVAS)
canvas.pack(fill='both', expand=True)

def cellule_survive(list_cellule, CELLULE_SIZE):
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
	canvas.create_rectangle(MIN_X,MIN_X,MAX_X,MAX_X, width=1, fill=COLOR_BACKGROUND_CELLULE)
	cellule_survive(refresh(), CELLULE_SIZE)
	if IS_CELLULE_LINES:
		trace_cellule(CELLULE_SIZE, MIN_X, MAX_X)
	stats()
	if not pause_simulation:
		root.after(INTERVAL_TIME_SIMULATION, simulation)

def refresh():
	global started
	if not started:
		G.initialise_plateau()
		cell = initial
		started = True
	else:
		cell = G.update_cells()
		G.update_plateau()
	return cell

def stats():
	global iteration
	t = f'Iteration : {iteration}'
	cell_dead = G.get_death_cells()
	cell_birth = G.get_birth_cells()
	cell_survived = G.get_survived_cells()
	if len(cell_dead)==0 and len(cell_birth) == 0:
		e = f'Stable after {iteration} iteration'
		canvas.create_text(0, MAX_X+80, text=e, font=(TEXT_FONT, 12), anchor=TEXT_CANVAS_ANCHOR)
	else:
		iteration += 1
	t2 = f'Cellule Dead {len(cell_dead)}'
	t3 = f'Cellule Birth {len(cell_birth)}'
	t4 = f'Cellule Survived {len(cell_survived)}'
	canvas.create_text(0, MAX_X+20, text=t, font=(TEXT_FONT, 12), anchor=TEXT_CANVAS_ANCHOR)
	canvas.create_text(0, MAX_X+35, text=t2, font=(TEXT_FONT, 12), anchor=TEXT_CANVAS_ANCHOR)
	canvas.create_text(0, MAX_X+50, text=t3, font=(TEXT_FONT, 12), anchor=TEXT_CANVAS_ANCHOR)
	canvas.create_text(0, MAX_X+65, text=t4, font=(TEXT_FONT, 12), anchor=TEXT_CANVAS_ANCHOR)
	
	
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
