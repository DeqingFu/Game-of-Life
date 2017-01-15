from logic import new_board, count_by_player, update_board, initial_player1, initial_player2
from appJar import gui
from Tkinter import *
from Tkinter import Tk, Canvas, Frame, Button
from Tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT


canvas_width = 600
canvas_height = 600
colors = ("red", "blue")
master = Tk()
master.title("Game of Life")
w = Canvas(master, width=canvas_width, height=canvas_height)

# app=gui()

board = new_board(20,20)
initial_player1()

def draw(L):
	r = len(L)
	c = len(L[0])
	for i in range(0,r):
		for j in range (0,c):
			if (L[i][j] == 0):
				w.create_rectangle(20*i, 20*j, 20*(i+1), 20*(j+1), fill = "red", outline = "black")
			else:
				w.create_rectangle(20*i, 20*j, 20*(i+1), 20*(j+1), fill = "blue", outline = "black")
	w.create_rectangle(40, 400, 160, 440, fill = "white", outline = "black")
	w.create_text(100, 420, text = "update")
	w.create_rectangle(240, 400, 360, 440, fill = "white", outline = "black")
	w.create_text(300, 420, text = "reset")

def reset():
	return new_board(20,20)

def click(event):
	x = event.x / 20
	y = event.y / 20
	if y >= 20:
		if x >= 2 and x <= 8:
			update_board(board)
		if x >= 12 and x <= 18:
			reset()
	elif board[x][y] == 0:
		board[x][y] = 1
	draw(board)
	report()

def report():
	a = 0
	b = 0
	r = len(board)
	c = len(board[0])
	for i in range(0,r):
		for j in range(0,c):
			if board[i][j] == 1:
				a = a + 1
			if board[i][j] == 2:
				b = b + 1
	w.create_rectangle(0, 460, 600, 480, fill = "white", outline = "white")
	w.create_text(200, 470, text = "Player 1 Cells: " + str(a))
	w.create_rectangle(0, 480, 600, 520, fill = "white", outline = "white")
	w.create_text(200, 500, text = "Player 2 Cells: " + str(b))

#w.bind("<Button-2>", handlekey)
w.bind("<Button-1>", click)
w.pack()

message = Label( master, text = "Press the mouse to draw" )
message.pack( side = BOTTOM )


mainloop()


# add a button
# app.addButton("One", update_board)

# app.go()

# function called by pressing the buttons
#def press(btn):
#    if btn=="Cancel":
#        app.stop()
#    else:
#        print("User:", app.getEntry('user'), "Pass:", app.getEntry('pass'))
